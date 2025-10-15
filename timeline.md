# News

2025.10.16 [oct0rdho/triton-windows](https://github.com/woct0rdho/triton-windows) project merged F8E4M3 and F8E5M2 fixes for RTX30xx to 3.4.x-windows and 3.5.x-windows branches:
[link1](https://github.com/woct0rdho/triton-windows/pull/140), [link2](https://github.com/woct0rdho/triton-windows/commit/ffb47c28144b89935208b42c50cdf1f09eb42aba);
this is part of `triton-windows 3.5.0.post21` release

2025.10.16 Kijai added nodes and an [example workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_FlashVSR_upscale_example.json) for FlashVSR upscaler  
Very fast, 1 step, but likely lesser quality than slow upscalers

2025.10.15 Ovi has been proven to work with [Controlnets](ovi.md#controlnets)

2025.10.14 Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/high released: Kijai's [Fix](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v)  
low model released is 2.1 so one of old LoRAs advised; also as [full models](https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/distill_models)  
could use lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors on low

2025.10.13 Kijai fixed a bug causing clip embeds to be ignored when working with [Wan Animate](WanAnimate.md)

2025.10.10 Latest version of Kiaji's nodes now supports [Tiny VAE](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors); not as good; "essentially a 'preview' VAE"

2025.10.10 Kijai extracted [rCM](LoRA-alchemy.md#rcm) distilled loras

2025.10.10 [Cseti](https://github.com/cseti007) published [Kinestasis](LoRA-alchemy.md#special-use) LoRA and [limited-context-options-wan2.2](tricks.md#cseti) process