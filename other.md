# Other Things to Check Out

## Promising For Comfy

* [GH:DAVIAN-Robotics/EgoX](https://github.com/DAVIAN-Robotics/EgoX), [keh0t0.github.io/EgoX](https://keh0t0.github.io/EgoX/) convert any video to 1st person view; Wan 2.1 I2V 480p LoRA: [HF:DAVIAN-Robotics/EgoX](https://huggingface.co/DAVIAN-Robotics/EgoX/tree/main)
* [GH:caiyuanhao1998/Open-OmniVCus](https://github.com/caiyuanhao1998/Open-OmniVCus) build a video from ingredients; [HF:CaiYuanhao/OmniVCus](https://huggingface.co/CaiYuanhao/OmniVCus/tree/main)
  "it's VACE module ... needs some new code probably ... loads without issues and technically works ... just.. doesn't do anything"

## Use With Caution

A fix has been performed in `ComfyRMBG` repository once this issue was raised: [151](https://github.com/1038lab/ComfyUI-RMBG/issues/151).
Please `git pull` the code.

The code was patching core functions in `pytorch`, disabling security on loading `.safetensors` and interfering with operation of other nodes inside ComfyUI installation in other ways.
Caution remains in place for all `1038lab` owned repositories.

* [1038lab/ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG) remove background
* [1038lab/ComfyUI-QwenVL](https://github.com/1038lab/ComfyUI-QwenVL) node to use qwen vl 3 for generating image and video prompts; [tutorial](https://www.youtube.com/watch?v=3j9c_-mRKfg)
* [1038lab/ComfyUI-WildPromptor](https://github.com/1038lab/ComfyUI-WildPromptor)

## Big List

* [GH:NewBieAI-Lab/NewBie-image-Exp0.1](https://github.com/NewBieAI-Lab/NewBie-image-Exp0.1) NewBie image generator, seems good for anime; Lumina family, with Gemma3 +  Jina clip models and Flux VAE
* [GH:martijnat/comfyui-previewlatent](https://github.com/martijnat/comfyui-previewlatent) quick latent preview w/o VAE
* [worldcanvas](https://worldcanvas.github.io/) a new model in footsteps of ATI and to some degree VACE
* [InfCam](https://github.com/emjay73/InfCam?tab=readme-ov-file) wan 2.1 based video-to-video moving camera according to a set trajectory
* 2025.12.23 HuMo/Phantom team have released their 133Gb training [dataset](https://modelscope.cn/datasets/leoniuschen/HuMoSet); such a nice Christmap present, well help a lot of projects
* 2025.12.23 NVidia has released a technology called NVFP4 for RTX50xx users; NVFP4 compatible adaptations of Wan 2.1 I2V 480 14B and Wan 2.1 T2V 1.3B have been made [available](https://huggingface.co/lightx2v/WanNVFP4); fast generations are expected


* [gumroad.com:ciojz] blender bones compatible with OpenPose
* [GH:sumitchatterjee13/nuke-nodes-comfyui](https://github.com/sumitchatterjee13/nuke-nodes-comfyui) Nuke style nodes for ComfyUI
* Comfy Native has got `Adjust Contrast` node

* [GH:alibaba-damo-academy/Lumos-Custom](https://github.com/alibaba-damo-academy/Lumos-Custom) relighting article
* [GH:MeiGen-AI/LongCat-Video-Avatar](https://github.com/MeiGen-AI/LongCat-Video-Avatar) from same team as InfiniteTalk, no degradation?
* [OmniPSD](https://showlab.github.io/OmniPSD/) separate poster into layers
* [GH:refkxh/bico](https://github.com/refkxh/bico) model for combining visual concepts from different images/videos; some links to Wan
* [GH:inclusionAI/TwinFlow](https://github.com/inclusionAI/TwinFlow), [HF:Suzu008/TwinFlow_Repackaged](https://huggingface.co/Suzu008/TwinFlow_Repackaged/tree/main) a new framework for 1 step generation for qwen image
* [GH:wildminder/ComfyUI-DyPE](https://github.com/wildminder/ComfyUI-DyPE) a node to push image generation into even higher resolutions - like 4K
* [GH:Moooonet/ComfyUI-Align](https://github.com/Moooonet/ComfyUI-Align) tools to help ComfyUI align and color nodes

* [GH:dagthomas/comfyui_dagthomas?tab=readme-ov-file#-qwenvl-nodes-local-vision](https://github.com/dagthomas/comfyui_dagthomas?tab=readme-ov-file#-qwenvl-nodes-local-vision) node for running QwenVL locally

* [SpatialTracerV2](https://spatialtracker.github.io/)

* [GH:chengzhag/UCPE](https://github.com/chengzhag/UCPE) Unified Camera Positional Encoding for Controlled Video Generation
* [GH:knightyxp/VideoCoF](https://github.com/knightyxp/VideoCoF) Unified Video Editing with Temporal Reasoner

* [GH:westNeighbor/ComfyUI-ultimate-openpose-editor:issues-31](https://github.com/westNeighbor/ComfyUI-ultimate-openpose-editor/issues/31) issue about open poser node being broken to the point of ComfyUI crashing
* [GH:maybleMyers/H1111/tree/svi] non-ComfyUI way to generate videos using Wan models with SVI 2.0 LoRA-s

* [GH:huchenlei/ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse) semi-transparent images with Comfy?
* [Wan 2.1 T2V Transparent Background](https://github.com/WeChatCV/Wan-Alpha)

* [GH:Jonseed/ComfyUI-Detail-Daemon](https://github.com/Jonseed/ComfyUI-Detail-Daemon) tool to adjust sigmas while image generation to improve details

* [Steady Dancer](https://mcg-nju.github.io/steadydancer-web/) now with basic ComfyUI support
* [Infinity Rope](https://infinity-rope.github.io/) based on Wan 1.3B so not paticularly powerful but holds promise for future

* [GH:PozzettiAndrea/ComfyUI-MotionCapture](https://github.com/PozzettiAndrea/ComfyUI-MotionCapture) [reddit intro](https://www.reddit.com/r/StableDiffusion/comments/1p4pkbk/release_comfyuimotioncapture_full_3d_human_motion/) full human body 3d motion capture
* [GH:PozzettiAndrea/ComfyUI-UniRig](https://github.com/PozzettiAndrea/ComfyUI-UniRig) ComfyUI tools for rigging a skeleton

* [GH:amao2001/ganloss-latent-space:workflow](https://github.com/amao2001/ganloss-latent-space/tree/main/workflow) lots of example workflows in the repo including Wan 2.1 Uni3C + Sam3D
* Depth-Anything 3 model can generate point clouds out of images
* koboldcpp an external app that can run gguf of qwen3-vl q8 and its mmoj part (llama more prone to hog vram)
* allegedly Holocine/PUSA(merge) + FunVACE (module) & Krea (module) via Extra jacks is possible?..
* [ComfyUI-Wan22FMLF](https://github.com/wallen0322/ComfyUI-Wan22FMLF) node to implement Wan 2.2 FMLF - first, middle, last frame
* [SVI](https://github.com/vita-epfl/Stable-Video-Infinity) continuation method for I2V; I2V gens chained, with 5 start frames

* [LanPaint](https://github.com/scraed/LanPaint)
* [Low-VRAM-High-RAM-Ostris-AI-Toolkit-Lora-Training](https://x.com/ostrisai/status/1975642220960072047)
* Unianimate - apparently that is a LoRa?
* ATI, Uni3c
* [SeC 4B](https://github.com/9nate-drake/Comfyui-SecNodes) Video Segmentation; Kijail: "still SAM2.1, just extra guidance for it"
* ToonComposer, [Educational Website](https://tooncomposer.com/)

* [GalaxyTimeMachine's canceller](https://gist.github.com/blepping/99aeb38d7b26a4dbbbbd5034dca8aca8)
* Chinese Diffsync Studio - a diffuser-based alternative to ComfyUI
* [StepVideo Repo](https://github.com/hao-ai-lab/FastVideo) it has a sliding window attn kernel for H100s
* `Pad Image Batch Interleaved` node from Kijai to generate intermediate frames with Wan 2.2
* `Pusa`: a LoRA "that allows Wan T2V model to use input images, it can do I2V or frame extentions"
* [TaylorSeer](https://github.com/philipy1219/ComfyUI-TaylorSeer) like TeaCache but better; 50 steps 50% faster; native not Kijai; not for small # of steps
* [cubiq/ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) contains some useful nodes like `Image Enhance Difference`
* [Create Any 3D and 4D Scenes from a Single Image](https://github.com/wenqsun/DimensionX) Kijai: this was released today after 10 month wait, and honestly it was always pretty damn good
* fspy, you can make 3d models from 2d images
* Musubi Trainer for Wan 2.2/2.1, AI Toolkit for 5B?
* [DiT360](https://fenghora.github.io/DiT360-Page/) open-source AI tool (flux lora?) to generate panoramic images
* [KangLiao/Puffin](https://huggingface.co/KangLiao/Puffin) open-source AI model which understands camera angles and can transform images
* [dvlab-research/DreamOmni2](https://github.com/dvlab-research/DreamOmni2) a flux lora? to help combine up to 4 image references or do image style transfer
* `Qwen3-VL-4B-Instruct-FP8.safetensors` loaded by `QwenVL (Advanced)` node can generate video description according to a prompt

## Deliberately Not Covered

* Palingenesis, any and all loras, models and code from Eddy1111111

## Unlikely

* [casterpollux/MiniMax-bmo](https://github.com/casterpollux/MiniMax-bmo) 1.3B model, somehow 30Gb download

* [https://civitai.com/models/2113025/cinematic-fast-cutting-previously-quick-cuts](https://civitai.com/models/2113025/cinematic-fast-cutting-previously-quick-cuts) only for wan high noise
* [https://huggingface.co/neph1/cinematic_quick_cuts_wan](https://huggingface.co/neph1/cinematic_quick_cuts_wan) multi-scene LoRa
* [https://huggingface.co/neph1/hard_cut_wan_lora](https://huggingface.co/neph1/hard_cut_wan_lora) cut LoRa ([same](https://discord.com/channels/1076117621407223829/1342763350815277067/1446907437717127178) ?)

## Promising But Not Immediately Useful
