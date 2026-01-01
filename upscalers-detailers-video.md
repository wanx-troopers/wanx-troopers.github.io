# Video Upscalers and Detailers

## FL13

- [FL13-WAN_Ultimate_I2V_Upscaler.20251123](workflows/FL13-WAN_Ultimate_I2V_Upscaler.20251123.json)
- [FL13-WAN_Ultimate_I2V_Upscaler](workflows/FL13-WAN_Ultimate_I2V_Upscaler.json)

Reportedly 10 minutes on 4090 to upscale 5 sec video to 2k

## FlashVSR

> but flashvsr is not good quality wise, they made a lot of poor decisions that compromise quality for speed;
> tiny attention windows that prevent proper motion tracking so details swim;
> also the vae is worse but you can use the original vae instead, it's just slower

[Example workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json)

Very fast, 1 step, but likely lesser quality than slow upscalers.
Context windows allow longer than 81 frames upscaling at the cost of minor glitches.
No sageattn, use spda.
Reducing strength can help with oversharpening.
Upscaling from 720x512x720 was kind of ok.

Kijai:
> it's basically 4x upscaler, at least 2x or it's bad results;
> would be fine if the input was tiny video, like their examples were 384x384, which is what the workflow used to test

Mads:
> At least it does not try to resolve motion blur, like most upscalers does

Can use with Cinescale lora and possibly with [RoPE Scaling](hidden-knowledge.md#rope)

> The new Flash VSR 1.1 upscaler is significantly better than v1;
> `Image Median Blur` size=4;
> `FlashVSR_Ultra_Fast` model=FlashVSR-v1.1 mode=tiny scale=2;
> good after `FL RIFE Frame Interpolation` rife49 from [GH:filliptm/ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes) multiplier=3;
> I use `Image Median Blur` to make results less sharp, I find FlashVSR to be too sharp

> waiting for Kijai to update it cuz others not optimized for low vram

> new vsr model works in kj wr but its bad

Implementations:

- [GH:filliptm/ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes)
- [lihaoyun6/ComfyUI-FlashVSR_Ultra_Fast](https://github.com/lihaoyun6/ComfyUI-FlashVSR_Ultra_Fast)

### Wiring FlashVSR

VSR safetensors loaded by `WanVideo Extra Model Select` plugged into `extra_model` input of `WanVideo Model Loader` loading Wan 2.1 T2V `safetensors`.

Very specific wording to be used in `WanVideo TextEncode`.

## SeedVR2

Can also do images, has been used on z-image-turbo produced images.
...

## SpacePxl Experimental Latent Upascaler

Experimental.

- [GH:spacepxl/ComfyUI-VAE-Utils](https://github.com/spacepxl/ComfyUI-VAE-Utils)
- [HF:spacepxl/Wan2.1-VAE-upscale2x/tree/main](https://huggingface.co/spacepxl/Wan2.1-VAE-upscale2x/tree/main)

> 2x spatial upscale only, works on images and video

> something like LUA could be much better, but this is at least a huge improvement over bilinear/bislerp

## Drozbay's Impact Pack SEGS Detailer For Wan Video And VACE

Highly experimental, requires a lot of work to use.

This is Drozbay's private fork of `Impact Pack` set of ComfyUI nodes, not merged into the original project:
[GH:drozbay/ComfyUI-Impact-Pack](https://github.com/drozbay/ComfyUI-Impact-Pack).
Includes example workflows.

Allows selecting part of generated video like a vace or a complete character, upscale it
to the resolution at which AI video generating models - those which take references;
say WAN + Phantom - or Humo - work best - run generations, downscale and integrate
result back into the original video.

Supports temporal blending across generated video fragments using VACE and context windows.

## Notable Image Upscalers

- "SeedVR is actually kind of insane"
- [Clarity Upscale](https://github.com/roblaughter/comfyui-workflows)
