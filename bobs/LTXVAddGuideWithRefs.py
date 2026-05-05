class LTXVAddGuideWithRefs:
    """
    IC-LoRA guide injection with separate reference images (Kijai/SCAIL approach).

    Encodes each reference image independently through the VAE as a single frame —
    avoiding temporal compression mixing with the guide video.
    Then concatenates [ref_1 | ref_2 | ... | guide] in latent space and injects
    the combined tensor as guide conditioning via the standard keyframe_idxs mechanism.

    Inputs:
        positive / negative : CONDITIONING
        vae                 : VAE (LTX-2)
        latent              : LATENT (target noisy latent, from EmptyLTXVLatentVideo)
        guide_frames        : IMAGE  [F, H, W, C]  — the guide video frames
        ref_images          : IMAGE  [N, H, W, C]  — N reference images (one per "slot")
        strength            : float  — conditioning strength (1.0 = exact)
        ref_strength        : float  — how strongly ref latents are injected (default 1.0)

    Sequence inside sampler:
        [ref_1_lat | ref_2_lat | ... | guide_lat | noisy_target_lat]
    All ref + guide positions get timestep=0 (clean conditioning).
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "positive":     ("CONDITIONING",),
                "negative":     ("CONDITIONING",),
                "vae":          ("VAE",),
                "latent":       ("LATENT",),
                "guide_frames": ("IMAGE",),
                "ref_images":   ("IMAGE",),
                "strength": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01,
                     "tooltip": "Guide conditioning strength."},
                ),
            },
            "optional": {
                "ref_strength": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01,
                     "tooltip": "Ref image conditioning strength (usually same as strength)."},
                ),
            },
        }

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "LATENT")
    RETURN_NAMES = ("positive", "negative", "latent")
    FUNCTION = "apply"
    CATEGORY = "video/ltx"

    def apply(self, positive, negative, vae, latent, guide_frames, ref_images,
              strength=1.0, ref_strength=1.0):
        import comfy.utils
        import comfy_extras.nodes_lt as nodes_lt

        scale_factors = vae.downscale_index_formula
        time_sf, w_sf, h_sf = scale_factors

        latent_image = latent["samples"]          # [B, C, F_target, H_lat, W_lat]
        noise_mask   = nodes_lt.get_noise_mask(latent)

        _, lat_h, lat_w = latent_image.shape[2], latent_image.shape[3], latent_image.shape[4]
        px_h = lat_h * h_sf
        px_w = lat_w * w_sf

        # ── 1. Encode guide video (normal VAE with temporal compression) ────────
        guide_px = comfy.utils.common_upscale(
            guide_frames.movedim(-1, 1), px_w, px_h, "bilinear", "disabled"
        ).movedim(1, -1)[:, :, :, :3]
        # Trim frames to valid temporal length: (F-1) must be divisible by time_sf
        n_guide = guide_px.shape[0]
        n_guide = (n_guide - 1) // time_sf * time_sf + 1
        guide_px = guide_px[:n_guide]
        guide_lat = vae.encode(guide_px)              # [1, C, F_guide_lat, H_lat, W_lat]

        # ── 2. Encode each ref image separately (single frame — no temporal mixing) ─
        n_refs = ref_images.shape[0]
        ref_lats = []
        for i in range(n_refs):
            # Take single image: [H, W, C] → [1, H, W, C]
            ref_px = ref_images[i:i+1]
            ref_px = comfy.utils.common_upscale(
                ref_px.movedim(-1, 1), px_w, px_h, "bilinear", "disabled"
            ).movedim(1, -1)[:, :, :, :3]
            ref_lat = vae.encode(ref_px)              # [1, C, 1, H_lat, W_lat]
            ref_lats.append(ref_lat)

        # ── 3. Concatenate: [ref_1 | ref_2 | ... | guide] in temporal dim ─────
        # Refs first → temporal 0..N_ref-1 
        # Guide after  → temporal N_ref, N_ref+1, ... (distinct from target, out-of-band)
        # This matches training: ref encoded separately before the guide.
        all_guide_parts = ref_lats + [guide_lat]
        combined_guide = torch.cat(all_guide_parts, dim=2)  # [1, C, N_ref+F_guide_lat, H_lat, W_lat]

        # ── 4. Inject combined guide and fix temporal coordinates ──
        # We need the token sequence to be [ref | guide] to match training context.
        # But the ref tokens must receive temporal coordinates from *after* the guide.
        # We achieve this by calling add_keyframe_index separately before concatenating.
        
        time_sf = scale_factors[0]
        F_guide_lat = guide_lat.shape[2]
        F_guide_pixel = (F_guide_lat - 1) * time_sf + 1  # Temporal position after the guide

        ref_lats_tensor = torch.cat(ref_lats, dim=2)
        
        # 4a. Add positional embeddings for refs (placed at F_guide_pixel)
        # Using causal_fix=False to match the exact temporal coordinates generated by training.
        # Training creates 6 frames with causal_fix=True and uses the 6th frame's coords [33, 41].
        # In ComfyUI, a 1-frame latent with causal_fix=False gets [0, 8] -> [33, 41].
        positive = nodes_lt.LTXVAddGuide.add_keyframe_index(positive, F_guide_pixel, ref_lats_tensor, scale_factors, causal_fix=False)
        negative = nodes_lt.LTXVAddGuide.add_keyframe_index(negative, F_guide_pixel, ref_lats_tensor, scale_factors, causal_fix=False)
        
        # 4b. Add positional embeddings for guide (starts at 0)
        positive = nodes_lt.LTXVAddGuide.add_keyframe_index(positive, 0, guide_lat, scale_factors, causal_fix=True)
        negative = nodes_lt.LTXVAddGuide.add_keyframe_index(negative, 0, guide_lat, scale_factors, causal_fix=True)
        
        # 4c. Concatenate latents and noise masks
        if latent_image.shape[1] > combined_guide.shape[1]:
            pad_len = latent_image.shape[1] - combined_guide.shape[1]
            combined_guide = torch.nn.functional.pad(combined_guide, pad=(0, 0, 0, 0, 0, 0, 0, pad_len), value=0)
            
        latent_image = torch.cat([latent_image, combined_guide], dim=2)
        
        mask = torch.full(
            (noise_mask.shape[0], 1, combined_guide.shape[2], noise_mask.shape[3], noise_mask.shape[4]),
            1.0 - strength,
            dtype=noise_mask.dtype,
            device=noise_mask.device,
        )
        noise_mask = torch.cat([noise_mask, mask], dim=2)
        
        # Track this guide for per-reference attention control
        pre_filter_count = combined_guide.shape[2] * combined_guide.shape[3] * combined_guide.shape[4]
        guide_latent_shape = list(combined_guide.shape[2:])  # [F, H, W]
        positive, negative = nodes_lt._append_guide_attention_entry(
            positive, negative, pre_filter_count, guide_latent_shape, strength=strength,
        )

        return (positive, negative, {"samples": latent_image, "noise_mask": noise_mask})