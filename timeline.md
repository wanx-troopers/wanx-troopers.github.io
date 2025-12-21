# News

2025.12.20 Integration of [LongCat Avatar](talkies/longcat-avatar.md) into ComfyUI has started; this is a promising successor/alternative to InfiniteTalk/HuMo promising very long video generation without burning;
reportedly from the same team that created MultiTalk/InfiniteTalk

2025.12.16 Advanced Context Windows worflows by [Drozbay](hidden-knowledge.md#drozbay) are now supported by ComfyUI native, [details](what-plugs-where/context-windows.md#20251216).

2025.12.13 Progress on integrating [SCAIL](wan-animates.md#scail) into ComfyUI; single character pose detection working, two character pose detection in progress [a WanAnimate analogue capable of generating two characters according to pose skeletons];
SCAIL project is encouraging happy users to put starts on the official github [repo](https://github.com/zai-org/SCAIL)

2025.12.14 [Wan-Move](wan-move.md) released and officially added to native ComfyUI; confirmed to work with [Uni3C](control.md#uni3c) camera control; works with [Context Windows](what-plugs-where/context-windows.md)

2025.12.13 Hugely popular [Z-Image-Turbo](extra-tools/z-image.md) 6B image generation model which has had a working ControlNet implementations in ComfyUI since 2025.12.03
has now received a `Union 2.0` ControlNet upgrade adding inpainting ability

2025.12.13 [preview](screenshots/kj-wrapper-v2-preview.webp) of Kijai's V2 nodes for wrapper; main idea is to make the list of inputs on the sampler shorter

2025.12.06 [Kandinsky-5](k5.md) Pro video AI model (5sec I2V, 5sec T2V, 10sec T2V) released 2025.11.14 and now supported in ComfyUI native have received official distillations

2025.12.09 NVidia released Wan 2.2 I2V [rCM](loras/part-01.md#22-i2v) speed LoRA

2025.12.09 [One-to-All-Animation](wan-animates.md#one-to-all-animation) similar to WanAnimate support added to Kijai's Wrapper, fp16 and fp8 weights uploaded to HF

2025.12.06 A [number](extra-tools/other-image-models.md) of image generation models have been released in December 2025 which failed to gain a lot of attention: 
LongCat (now all of image/image edit/video), Ovis 7B

2025.11.05 [Hunyuan 1.5](hunyuan.md) 5-10sec/24fps videos released 2025.11.21 received distilled 480 model version (no 720 version yet)

2025.12.05 [Z-Image-Turbo](extra-tools.md#z-image-turbo) tested with "Gabliterated" version of Qwen3-4B (which is the model's CLIP) and an alternative VAE

2025.12.05 Version 2.0 of [SVI-shot](svi.md#20251204) combining SVI-shot (reference) and SVI-flim (5 frames overlap) released for Wan 2.1; also Wan 2.2 Version 2.0 only supporting SVI-shot functionality

2025.12.04 `sageattn_ultravico` option added to [Wrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) supporting one of the newer [RifleX](https://github.com/thu-ml/DiT-Extrapolation)
methods to generate videos with a greater number of frames without looping; a not so bad result has been demostrated with [Kandinsky-5](k5.md) but results with Wan did not look particularly good.

2025.12.03 Flux.2 Dev released under non-commerical license earlier on 2025.11.25 to enthusiasm of some and unhappiness of others (high VRAM usage, long generations)
has received a ControlNet [model](https://huggingface.co/alibaba-pai/FLUX.2-dev-Fun-Controlnet-Union); status of integration into ComfyUI unknown

2025.11.30 Kijai's [commit](https://github.com/kijai/ComfyUI-WanVideoWrapper/commit/99c3978da4a55a03249669bef5647d7dbda7a5d1) to [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
"Reduce peak VRAM usage when not using torch.compile (and some even with it)"

2025.11.30 [Steady Dancer](wan-animates.md#steady-dancer) support merged to ComfyUI `main`

2025.11.29 [GH:ModelTC/ComfyUI-LightVAE](https://github.com/ModelTC/ComfyUI-LightVAE) alternative WAN VAE-s: faster and less VRAM, are now working in native WF-s in ComfyUI

2025.11.20 Community is experimenting with Facebook's [SAM3](auxiliary.md#sam3) segmentation/depth map model

2025.11.20 New LoRa-s to supply subjects/objects and background all in 1st frame image for Wan 2.2 I2V: [FFGO](wan-i2v-advanced.md#ffgo)

2025.11.16 Kijai implemented [TimeToMove](wan-i2v-advanced.md#timetomove) mockup in wrapper

2025.11.16 Community is exploring [Painter I2V](wan-i2v-advanced.md#painter-i2v) and [PainterLongVideo](wan-i2v-advanced.md#painterlongvideo) nodes for more dynamic and longer generations with Wan 2.2 I2V

2025.11.15 [drozbay](hidden-knowledge.md#drozbay) has created [GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments) repository dubbed `WanEx`; it contains his nodes
for I2V and continuations with [HuMo](humo.md), using [SVI-shot](svi.md#svi-shot) and for building a native [BindWeave](bindweave.md) WF

2025.11.15 [drozbay](hidden-knowledge.md#drozbay) has shared a HuMo continuation workflow;
please see [HuMo](humo.md) section

2025.11.15 [BindWeave](bindweave.md) nodes merged to `main` branch in [GH:kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)

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

2025.10.21 [MoCha](wan-animates.md#mocha) Wan 2.1 T2V 14B-derived human replacement full-fat model released and adapted inside Wrapper   
2025.10.21 A bug fixed around using [Context Windows](what-plugs-where/context-windows.md) with `Uni3C` ControlNet (in VACE workflows?)  
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

2025.10.16 Kijai added nodes for [FlashVSR upscaler](upscalers-detailers-video.md#flashvsr)

2025.10.15 Ovi has been proven to work with [Controlnets](ovi.md#controlnets)

2025.10.14 Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/high released: Kijai's [Fix](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v)  
low model released is 2.1 so one of old LoRAs advised; also as [full models](https://huggingface.co/lightx2v/Wan2.2-I2V-A14B-Moe-Distill-Lightx2v/tree/main/distill_models)  
could use lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors on low

2025.10.13 Kijai fixed a bug causing clip embeds to be ignored when working with [Wan Animate](wan-animates.md#wan-animate)

2025.10.10 Latest version of Kiaji's nodes now supports [Tiny VAE](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/taew2_2.safetensors); not as good; "essentially a 'preview' VAE"

2025.10.10 Kijai extracted [rCM](loras/part-02.md#rcm) distilled loras

2025.10.10 [Cseti](https://github.com/cseti007) published [Kinestasis](loras/alchemy.md#special-use) LoRA and [limited-context-options-wan2.2](tricks.md#cseti) process

? [Lynx](lynx.md) Facility to introduce character likeness from a single reference image for Wan 2.1 T2V
