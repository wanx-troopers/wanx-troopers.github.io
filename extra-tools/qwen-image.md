# Qwen

## 2025.12.23

Highly anticipated Qwen Image Edit 2511 is out

- official release is split .safetensors so probably not directly useable
- [HF:unsloth/Qwen-Image-Edit-2511-GGUF](https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF/tree/main) first repo to offer BF16, FP16, Q3-Q8 "city96 unet loader ofc"
- [GH:city96/ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) loader to load GGUF files
- [HF:Comfy-Org/Qwen-Image-Edit_ComfyUI:split_files/diffusion_models](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/tree/main/split_files/diffusion_models) Comfy-Org adaptation, BF16
- lightx2v LoRA-s: [HF:lightx2v/Qwen-Image-Edit-2511-Lightning](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/tree/main)

Official workflow embedded in this image:

![qie2511](../workflows/qie2511.png)

[qie2511](../workflows/qie2511.png)

> They seemed to have added a lot more color. The greens are popping and the color does not seem so washed out.

## 2025.12.13

[GH:gajjar4/ComfyUI-Qwen-Image-i2L](https://github.com/gajjar4/ComfyUI-Qwen-Image-i2L) so called "I2L", "image to LoRA", a super-lightweight approach to extracting
a Qwen (Image Edit?) LoRA from an image; resulting LoRA is pretty weak

Qwen Edit Multiple angles LoRA good to create one image with views of the same character from different sides

## Qwen Image Edit

Supposedly has affinity to Wan models since both come from Alibaba.

| HF Space | Model |
| --- | --- |
| Comfy-Org/Qwen-Image-Edit_ComfyUI | split_files/diffusion_models/qwen_image_edit_2509_bf16 |
| Comfy-Org/Qwen-Image_ComfyUI | split_files/vae/qwen_image_vae |
| Comfy-Org/Qwen-Image_ComfyUI | split_files/text_encoders/qwen_2.5_vl_7b |
| lightx2v/Qwen-Image-Lightning | Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16 |
| lightx2v/Qwen-Image-Lightning | Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16 |

Interesting: an [attempt](https://www.reddit.com/r/QwenImageGen/comments/1p3c0r6/controlnet_openpose_qwen_image_edit_2509/) to rig a ControlNet on top of QIE 2509.

## Notable Loras For Qwen Image Edit

Generates 1st frame for next scene in same location with same character.
Sample workflow on HF next to LoRA.

| HF Space | LoRA |
| --- | --- |
| lovis93/next-scene-qwen-image-lora-2509 | next-scene_lora_v1-3000.safetensors |

Text editing similar to Nano Banana (dataset [visualizer](https://snazzy-selkie-ebdccf.netlify.app/), [dataset](https://github.com/apple/pico-banana-400k))

| HF Space | LoRA |
| --- | --- |
| [eigen-ai-labs/eigen-banana-qwen-image-edit](https://huggingface.co/eigen-ai-labs/eigen-banana-qwen-image-edit/tree/main) | eigen-banana-qwen-image-edit-2509-fp16-lora.safetensors |

## Qwen Piflow

[PiFlow](../hidden-knowledge.md#20251215-piflow)

## Face Consistency With Qwen?

[WithAnyone](https://doby-xu.github.io/WithAnyone/)

[PuLID](https://huggingface.co/guozinan/PuLID) ?

## Notable LoRA-s

- [HF:dx8152/Qwen-Edit-2509-Light-Migration](https://huggingface.co/dx8152/Qwen-Edit-2509-Light-Migration) relight / light-migration for QIE 2509; [examples](https://x.com/dx8152/status/1997124533116141818?s=46)

