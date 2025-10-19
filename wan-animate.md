# Wan Animate

[kijai/ComfyUI-WanAnimatePreprocess](https://github.com/kijai/ComfyUI-WanAnimatePreprocess) highly recommended esp. [example workflow](https://github.com/kijai/ComfyUI-WanAnimatePreprocess/tree/main/example_workflows).

```bash
hf download Kijai/sam2-safetensors sam2.1_hiera_base_plus.safetensors # models/sam2
hf download Kijai/WanVideo_comfy_fp8_scaled Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors # models/diffusion_models
hf download Kijai/WanVideo_comfy WanAnimate_relight_lora_fp16.safetensors # models/diffusion_models
```

Important:

* either have both BG and mask connected (background from driving video)
* or have both BG and mask disconnected (background from reference image)

There are two ways to produce longer videos in a batched manner: with and without [WanVideo Context Options](what-plugs-where/context-options.md):

|Option|`WanVideo Animate Embeds`|`WanVideo Context Options`|
|:---|:---|:---|
|A|set `frame_window_size` to you batch size, say 77<br>set `num_frames` to the length of the video you want to generate|do not connect to `WanVideo Sampler`|
|B|set both `frame_window_size` and `num_frames` to the length of the video you want to generate|set `context_frames` to your batch size, say 77 or 81<br>4 is possibly correct value for `stride` effectively setting it to 'disabled'|

With Kijai's nodes face video can be simply disconnected. In native nodes one may need to connect a black image/video.
Yes, the mask has to be blocky. Sometimes increasing blocks size can make things better.
Blocky mask bleeding into produced video might get fixed if face is connected.

Kijai on WanAnimate with Uni3C:
> I've had it work before, so it definitely can work

Untested but it is possible `WanAnimate` can take up to 4 reference images.

Apparently can be used with [Lynx](lynx.md).

## WanAnimate V2 .safetensors File

Kijai:

> I named the fixed scaled fp8 model v2, which in hindsight was a mistake as people are taking it too literally  
> it's a bugfix for native workflows since there was pretty drastic noise issue in the initial fp8 scaled in native  
> [original version, so called v1 is] very slightly better in the wrapper as the face encoder layers are in bf16  

> [so-called V3 from Eddy1111111] is probably just Lora merge or something

## What Plugs Where

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `WanVideo ClipVision Encode` | `clip_vision`, `image_1`, `image_2`<br>-> `image_embeds`  | `Wan VideoAnimate Embeds` | `clip_embeds` / `ref_images`, `pose_images`, `face_images`, `bg_images`, `mask` | Wan 2.1 I2V family | `image_embeds` |
