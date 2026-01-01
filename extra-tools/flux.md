# Flux Image Generation Models

- [HF:silveroxides/FLUX.2-dev-fp8_scaled/tree/main](https://huggingface.co/silveroxides/FLUX.2-dev-fp8_scaled/tree/main) model weights.
  Now includes weights for "turbo" flavor - the distilled version.
- [HF:fal/FLUX.2-dev-Turbo/tree/main/comfy](https://huggingface.co/fal/FLUX.2-dev-Turbo/tree/main/comfy) flux.2 dev turbo as a LoRA
- [HF:Comfy-Org/flux2-dev:loras](https://huggingface.co/Comfy-Org/flux2-dev/tree/main/split_files/loras) flux.2 dev turbo LoRA repackaging that will surely work in Comfy

Both base and distilled are distributed under a non-commerical license.


Flux 2 is using Mistral as CLIP similar to [z-image-turbo](z-image.md).
This is an 18Gb download named `mistral_3_small_flux2_fp8`.
`bf16` version is 35.6Gb. Main model weights in fp8 are 35Gb.

> amazing prompt adherence

> flux2 fp8 it ran under 280 sec for 720x350 image [on RTX3060]

> Flux 2 ran with fancy clownsampler can be slower than HunyuanImg3;
> at least HunyuanImg3 is just LLM speed


## Notable Flux 2 LoRa-s

- Boring Reality


## Misc

- [Prompting Guide](https://docs.bfl.ai/guides/prompting_guide_flux2)
