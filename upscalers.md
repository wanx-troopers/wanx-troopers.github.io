# Upascalers

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

## What Plugs Where

VSR safetensors loaded by `WanVideo Extra Model Select` plugged into `extra_model` input of `WanVideo Model Loader` loading Wan 2.1 T2V `safetensors`.

Very specific wording to be used in `WanVideo TextEncode`.

## seedvr2

...
