# News

2025.11.16 Kijai implemented [TimeToMove](wan-i2v-tricks.md#timetomove) mockup in wrapper

2025.11.16 Community is exploring [PainterI2V](wan-i2v-tricks.md#painteri2v) and [PainterLongVideo](wan-i2v-tricks.md#painterlongvideo) nodes for more dynamic and longer generations with Wan 2.2 I2V

2025.11.15 [drozbay](https://github.com/drozbay) has created [GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments) repository dubbed `WanEx`; it contains his nodes
for working with [HuMo](humo.md), [SVI-shot](svi.md#svi-shot) and native WF [BindWeave](bindweave.md)

2025.11.15 [drozbay](https://github.com/drozbay) has shared a HuMo continuation workflow;
please see [HuMo](humo.md) section

2025.11.15 [BindWeave](bindweave.md) nodes merged to `main` branch in [GH:kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

2025.11.14 [Kandinsky-5](k5.md) Pro model weights made public: 5sec I2V, 5sec T2V, 10sec T2V; no implementation in ComfyUI yet allowing to run on consumer hardware

2025.11.11 Ovi 1.1 capable of 10sec video+sound generation weights have been upoloaded to HuggingFace

2025.11.10 UniLumos relight model integration into wrapper is being tested; [sample workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_1_3B_UniLumos_relight_example_01.json)

2025.11.10 --disable-pinned-memory option recommended when launching latest version of Comfy UI

2025.11.06 ChronoEdit released - model/workflow to generate a short clip making changes to an initial image with the goal of picking one frame that represents edited image, limited to the resolution Wan models work at, [link](https://aistudynow.com/chronoedit-comfyui-workflow-compare-with-qwen-image-edit-2509/); [rodent youtube tutorial](www.youtube.com/watch?v=ZdGpgs2qFWY)

2025.10.30 [1030](loras/part-01.md#2025-Oct-10) I2V high noise lora released superceeding 1022 and MoE

2025.10.25 [LongCat](longcat.md) models released; early experimentation in ComfyUI; promise of long and fast generations, 6 sec fragements stitched with 11 frame overlap; when continuation is used 11 frames is the only context possible, reference images are not taken

2025.10.24 [HoloCine](holocine.md) model released; early experimentation in ComfyUI;
15sec multi-scene videos generated with characters consistent within those generations

2025.10.22 [SVI](svi.md) LoRa-s released; Wan I2V models now can extend videos using 5 frame overlap with SVI-film; other LoRa-s provide a new way to supply a reference image to I2V generations

2025.10.22 Kijai uploaded adapted Qwen Image VAE to [Kijai/QwenImage_experimental](https://huggingface.co/Kijai/QwenImage_experimental/tree/main); more details; only works for single images so far  
2025.10.22 New wan2.2 i2v lightx2v 4step [1022](loras/part-01.md) LoRa-s have been released  
2025.10.22 "Rollingforce" based on Wan 1.3B promises long generations; current experiments are yilding very modest results however

2025.10.21 [MoCha](wan-animate-mocha.md#mocha) Wan 2.1 T2V 14B-derived human replacement full-fat model released and adapted inside Wrapper   
2025.10.21 A bug fixed around using [WanVideo Context Options](what-plugs-where/context-options.md) with `Uni3C` ControlNet (in VACE workflows?)  
2025.10.21 [Krea Realtime](loras/both-ways.md#krea-realtime) Wan 2.1 T2V 14B distill difficult to use but realistic; works as a "full-fat" model, not as a LoRa


2025.10.20 Kijai adapted [Ditto](loras/part-02.md#ditto) LoRas for VACE; these allow converting realistic videos to animated styles

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

2025.10.15 Ovi has been proven to work with [Controlnets](ovi.md#controlnets)

2025.10.14 Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/high released: Kijai's [Fix](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v)  
low model released is 2.1 so one of old LoRAs advised; also as [full models](https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/distill_models)  
could use lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors on low

2025.10.13 Kijai fixed a bug causing clip embeds to be ignored when working with [Wan Animate](wan-animate-mocha.md#wan-animate)

2025.10.10 Latest version of Kiaji's nodes now supports [Tiny VAE](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors); not as good; "essentially a 'preview' VAE"

2025.10.10 Kijai extracted [rCM](loras/part-02.md#rcm) distilled loras

2025.10.10 [Cseti](https://github.com/cseti007) published [Kinestasis](loras/alchemy.md#special-use) LoRA and [limited-context-options-wan2.2](tricks.md#cseti) process