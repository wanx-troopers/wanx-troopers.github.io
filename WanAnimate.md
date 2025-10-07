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

With Kijai's nodes face video can be simply disconnected. In native nodes one may need to connect a black image/video.
Yes, the mask has to be blocky. Sometimes increasing blocks size can make things better.
Blocky mask bleeding into produced video might get fixed if face is connected.

Kijai on WanAnimate with Uni3C:
> I've had it work before, so it definitely can work

Apparently can be used with [Lynx](lynx.md).
