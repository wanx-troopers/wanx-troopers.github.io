# Flux Image Generation Models

## 2026.06

[GH:42lux/ComfyUI-42lux-Hildegard-Refiner](https://github.com/42lux/ComfyUI-42lux-Hildegard-Refiner) tile-based FLUX.2 Klein refiner

Nekodificator:
- [YT:8wBXI-QCy0w](https://youtu.be/8wBXI-QCy0w) Klein tools by Nekodificator
- [CA:2684849/nkd-haze-slider](https://civitai.com/models/2684849/nkd-haze-slider)
- [CA:2620811/nkd-focal-length-slider](https://civitai.com/models/2620811/nkd-focal-length-slider)

Other LoRAs:
- [HF:gilfoyle0813/flux2_klein_9b_depth_control](https://huggingface.co/gilfoyle0813/flux2_klein_9b_depth_control)

## 2026.05

[GH:ethanfel/Comfyui-PainterKleinImageEdit](https://github.com/ethanfel/Comfyui-PainterKleinImageEdit)
"node for FLUX.2 [klein] (4B / 9B) image editing and text-to-image generation"

[GH:cosmicrealm/ComfyUI-Flux-FaceIR](https://github.com/cosmicrealm/ComfyUI-Flux-FaceIR) confusing tool for restoring faces on damaged photos.

David Shows frame by frame cleanup wf using Klein: [david-show-klein-frame-by-frame-cleanup](../workflows/imagens/david-show-klein-frame-by-frame-cleanup.png),
[david-show-klein-frame-by-frame-cleanup-2](../workflows/imagens/david-show-klein-frame-by-frame-cleanup-2.png).

[GH:supermansundies/comfyui-klein-edit-composite](https://github.com/supermansundies/comfyui-klein-edit-composite)
Klein edit composite node to mitigate color shift. Scf: "Sounds like you can do the same with masked inpainting in lanpaint"

[Mark DK Berry](https://markdkberry.com) on Kein:
> took me months to realise it doesnt need speed upo loras. Klein changed my life. but license is meh.

> 4b - not good, 9b - good

if Klein is used for editing not creating images it seems the licensing becomes more of a grey area ... 9b is non-commerical only

Klein can be used for editing

[HF:wikeeyang/Flux2-Klein-9B-True-V2](https://huggingface.co/wikeeyang/Flux2-Klein-9B-True-V2) a Klein finetune?

[GH:Lakonik/ComfyUI-piFlow](https://github.com/Lakonik/ComfyUI-piFlow) nodes for running AsymFLUX.2, a direct to pixels (PiD) flavor of Flux.2 dev?

Character trainer for flux: [R:using_depth_maps_and_weight_noising_to_get_better](https://www.reddit.com/r/StableDiffusion/comments/1tplsmr/using_depth_maps_and_weight_noising_to_get_better/)

Flux Identity Adjuster V2 - node [GH:Magirad/Flux_ID_Adjuster_V2](https://github.com/Magirad/Flux_ID_Adjuster_V2),
[R:flux_identity_adjuster_v2](https://www.reddit.com/r/StableDiffusion/comments/1tsxd9r/flux_identity_adjuster_v2/)

## 2026.04

[CA:2318844/klein-9b-body-weight-slider](https://civitai.com/models/2318844/klein-9b-body-weight-slider) concept slider from thin to fat

## Older

- [HF:silveroxides/FLUX.2-dev-fp8_scaled/tree/main](https://huggingface.co/silveroxides/FLUX.2-dev-fp8_scaled/tree/main) model weights.
  Now includes weights for "turbo" flavor - the distilled version.
- [HF:fal/FLUX.2-dev-Turbo/tree/main/comfy](https://huggingface.co/fal/FLUX.2-dev-Turbo/tree/main/comfy) flux.2 dev turbo as a LoRA
- [HF:Comfy-Org/flux2-dev:loras](https://huggingface.co/Comfy-Org/flux2-dev/tree/main/split_files/loras) flux.2 dev turbo LoRA repackaging that will surely work in Comfy

Both base and distilled are distributed under a non-commerical license.

## Flux.2 [klein]

This is the faster model. Available in 4B and 9B, both distilled and base.

> klein distilled is for converging in 8 steps. You might have augment the instruct with additional syntences to keep hair etc accurate.

## Flux.2 [dev]

This is the slow model.

Flux 2 is using Mistral as CLIP similar to [z-image-turbo](z-image.md).
This is an 18Gb download named `mistral_3_small_flux2_fp8`.
`bf16` version is 35.6Gb. Main model weights in fp8 are 35Gb.

> amazing prompt adherence

> flux2 fp8 it ran under 280 sec for 720x350 image [on RTX3060]

> Flux 2 ran with fancy clownsampler can be slower than HunyuanImg3;
> at least HunyuanImg3 is just LLM speed


### Notable Flux 2 LoRa-s

- Boring Reality


### Misc

- [Prompting Guide](https://docs.bfl.ai/guides/prompting_guide_flux2)
