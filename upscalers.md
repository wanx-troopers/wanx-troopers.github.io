# Upascalers

## FL13

[FL13-WAN_Ultimate_I2V_Upscaler](workflows/FL13-WAN_Ultimate_I2V_Upscaler.json)
Reportedly 10 minutes on 4090 to upscale 5 sec video to 2k


## FlashVSR

[Example workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json)

Very fast, 1 step, but likely lesser quality than slow upscalers.
Context options allow longer than 81 frames upscaling at the cost of minor glitches.
No sageattn, use spda.
Reducing strength can help with oversharpening.
Upscaling from 720x512x720 was kind of ok.

Kijai:
> it's basically 4x upscaler, at least 2x or it's bad results;
> would be fine if the input was tiny video, like their examples were 384x384, which is what the workflow used to test

Mads:
> At least it does not try to resolve motion blur, like most upscalers does

Can use with Cinescale lora and possibly with [RoPE Scaling](hidden-knowledge.md#rope)

## FlashVSR v1.1

> The new Flash VSR 1.1 upscaler is significantly better than v1;
> `Image Median Blur` size=4;
> `FlashVSR_Ultra_Fast` model=FlashVSR-v1.1 mode=tiny scale=2;
> good after `FL RIFE Frame Interpolation` rife49 from [GH:filliptm/ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes) multiplier=3;
> I use `Image Median Blur` to make results less sharp, I find FlashVSR to be too sharp

> waiting for Kijai to update it cuz others not optimized for low vram

> new vsr model works in kj wr but its bad

## What Plugs Where

VSR safetensors loaded by `WanVideo Extra Model Select` plugged into `extra_model` input of `WanVideo Model Loader` loading Wan 2.1 T2V `safetensors`.

Very specific wording to be used in `WanVideo TextEncode`.

## seedvr2

...
