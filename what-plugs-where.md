# What Plugs Where

A big table analysing workflows available online to take note of which embeds node can be used with which model (.safetensors).
Very similar workflows apply both to VACE 2.1 and Wan 2.2 Fun Vace.

## Native

### VACE [kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

* `Diffusion Model Selector` (VACE safetensors; -> `extra_state_dict` input of `Diffusion Model Loader KJ`)
* `Diffusion Model Loader KJ` (Wan 2.2 .. T2V ..)
* `LoraLoaderModelOnly` (some speed lora; can chain after the above)

Supplementary; chain after model loader

* `TorchCompileModelWanVideo`
* `Patch Sage Attention KJ`

### Embeds In Native

| Embeds Node | Inputs | Model | Bonuses |
| :-- | :-- | :-- | :-- |
| `WanVaceToVideo` | `control_video`, `masks`, `ref_image`, `pos/neg` | VACE + Wan | `trim_latent` from `WanVaceToVideo` to `TrimLatentNode` |

Bonus nodes: `Create Video`, `Save Video`, `Points Editor`, `(Down)Load SAM2Model`, `Sam2Segmentation`, `GrowMask`, `Preview Animation`, `Empty Image` (color 8421504), `ImageComposeMask`.

Not entirely clear if inpainted area needs to be gray-ed out in `control video` input to `WanVaceToVideo`

## Wrapper

### VACE [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

* `WanVideo VACE Module Select` (Wan2_2_Fun_VACE..; -> `vace_input` of `VanVideo Model Loader`)
* `WanVideo Lora Select Multi` (say lightx2v_T2V_14B_ .. v2..; -> `lora` input of `VanVideo Model Loader`)
* `WanVideo Model Loader` (Wan 2.2 .. T2V ..)

Supplementary

* `WanVideo VAE Loader`
* `WanVideo Torch Compile Settings` (-> `compile_args` input of `WanVideo Model Loader`)
* `WanVideo Set Block Swap` (chain after `WanVideo Model Loader`)
* `WanVideo Lora Block Edit` (switching off block 0 might help remove 1st frame flash)

### Embeds In Wrapper

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
| - | - | `WanVideo VACE Encode` | / `input_frames`, `input_masks`, `ref_images`<br>-> `vace_embeds` | VACE + Wan T2V family | `image_embeds` |
| - | - | `WanVideo ImageToVideo Encode` | / `start_image`, `end_image`, `control_embeds`?, `temporal_mask`?, `extra_latents`, `add_cond_latents`?<br>-> `image_embeds` | Wan I2V family | `image_embeds` |
| - | - | `Multi/Infinite Talk Wav2vec Embeds` | `wav2vec_model`, ... |  Wan 2.1 I2V family | `image_embeds` |

Note: ? denotes parts which are not clear enough.

### WanVideo VACE Start To End Frame

* inputs: `start_image`, `end_image`, `num_frames` and, confusingly, `control_images` and `inpaint_mask`
* outputs: `images`, `masks`

Can be used to prepare `input_frames` for `WanVideo VACE Encode`.
Bonus nodes:

* `Solid Mask`
* `Repeat Masks`

More bounuses:

* `Image Preview`
* `Mask Preview`

#### Wiring

```
WanVideo VACE Start To End Frame --------------------> | Replace Images  |
                                                       | In Batch        | --> Preview Image,
LoadImage  ---> ResizeImage ---> RepeatImageBatch ---> |                 |     WanVideo VACE Encode --> ..
                                                       |                 |
SolidMask  ---> RepeatMask --------------------------> |                 |
```

## [Wan Animate](WanAnimate.md#what-plugs-where) Section

## [Ovi](ovi.md) Section
