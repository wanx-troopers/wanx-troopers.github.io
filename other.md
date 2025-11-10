# Other Things to Check Out

* [SVI](https://github.com/vita-epfl/Stable-Video-Infinity) continuation method for I2V; I2V gens chained, with 5 start frames

* [Wan 2.1 T2V Transparent Background](https://github.com/WeChatCV/Wan-Alpha)
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
* [DiT360](https://fenghora.github.io/DiT360-Page/) open-source AI tool (flux lora?) to generate panaroamic images
* [KangLiao/Puffin](https://huggingface.co/KangLiao/Puffin) open-source AI model which understands camera angles and can transform images
* [dvlab-research/DreamOmni2](https://github.com/dvlab-research/DreamOmni2) a flux lora? to help combine up to 4 image references or do image style transfer
* `Qwen3-VL-4B-Instruct-FP8.safetensors` loaded by `QwenVL (Advanced)` node can generate video description according to a prompt

## Deliberately Not Covered

* Palingenesis, any and all loras, models and code from Eddy1111111

## Unlikely

* [casterpollux/MiniMax-bmo](https://github.com/casterpollux/MiniMax-bmo) 1.3B model, somehow 30Gb download

## Promising But Not Immediately Useful