# News

2025.10.22 wan2.2 i2v lightx2v 4step [1022 loras](loras/part-01.md) seems to be produced same way  
           as how Kijai extracted earlier under Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE name

2025.10.22 "Rollingforce" based on Wan 1.3B promises long generations

2025.10.21 [MoCha](wan-animate-mocha.md#mocha) Wan 2.1 T2V 14B-derived human replacement full-fat model released and adapted inside Wrapper   
2025.10.21 A bug fixed around using [WanVideo Context Options](what-plugs-where/context-options.md) with `Uni3C` ControlNet (in VACE workflows?)  
2025.10.21 [Krea Realtime](loras/both-ways.md#krea-realtime) Wan 2.1 T2V 14B distill difficult to use but realistic; works as a "full-fat" model, not as a LoRa


2025.10.20 Kijai adapted [Ditto](loras/part-02.md#ditto) LoRas

2025.10.19 Kijai added `total_pixels` mode to `Resize Image v2` node in [kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

2025.10.19 Note [loras](loras/alchemy.md#special-use): Walgro, Charlietooth/punk, Lazy Susan

2025.10.18 Issues causing increased VRAM usage and excessive/failing triton compilations have hopefully been resolved
in latest ComfyUI and Wrapper; advice on torch version from Kijai:
> 2.8.0 problematic, 2.9 and 2.10.0-dev should be fine with latest Comfy and Wrapper

2025.10.17 [lightx2v/Wan2.2-Distill-Loras](https://huggingface.co/lightx2v/Wan2.2-Distill-Loras) HF repo has been re-organized; files moved; fp8 versions for some of the files were added;
some of the distillations which were previously only available as loars are now offered as full-fat models; some of the loras are offered both in comfy and safetensor compatible versions

2025.10.16 [oct0rdho/triton-windows](https://github.com/woct0rdho/triton-windows) project merged F8E4M3 and F8E5M2 fixes for RTX30xx to 3.4.x-windows and 3.5.x-windows branches:
[link1](https://github.com/woct0rdho/triton-windows/pull/140), [link2](https://github.com/woct0rdho/triton-windows/commit/ffb47c28144b89935208b42c50cdf1f09eb42aba);
this is part of `triton-windows 3.5.0.post21` release

2025.10.16 Kijai added nodes for [FlashVSR upscaler](upscalers.md#flashvsr)

nodes and an [example workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json) for FlashVSR upscaler;
very fast, 1 step, but likely lesser quality than slow upscalers; context options allow longer than 81 frames upscaling at the cost of minor glitches; no sageattn, use spda;
reducing strength can help with oversharpening; not really meant to go as high as 2560x1536; upscaling from 720x512x720 was kind of ok
can use with Cinescale lora and possibly with [RoPE Scaling](hidden-knowledge.md#rope); alternatives: seedvr2.

2025.10.15 Ovi has been proven to work with [Controlnets](ovi.md#controlnets)

2025.10.14 Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/high released: Kijai's [Fix](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v)  
low model released is 2.1 so one of old LoRAs advised; also as [full models](https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/distill_models)  
could use lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors on low

2025.10.13 Kijai fixed a bug causing clip embeds to be ignored when working with [Wan Animate](wan-animate-mocha.md#wan-animate)

2025.10.10 Latest version of Kiaji's nodes now supports [Tiny VAE](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors); not as good; "essentially a 'preview' VAE"

2025.10.10 Kijai extracted [rCM](loras/part-02.md#rcm) distilled loras

2025.10.10 [Cseti](https://github.com/cseti007) published [Kinestasis](loras/alchemy.md#special-use) LoRA and [limited-context-options-wan2.2](tricks.md#cseti) process