# LTXV

## Capabilities

>  Our APIs support up to 20s at 25fps at the moment. Depending on hardware of course.

## Setup

- Main model [HF:Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2/tree/main)
    - ltx-2-19b-distilled
    - ltx-2-19b-dev-fp8
    - ltx-2-19b-distilled-lora-384
- Text Encoder
  - [HF:google/gemma-3-12b-it-qat-q4_0-unquantized](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main) for custom node, see bellow
  - [HF:Comfy-Org/ltx-2:split_files/text_encoders](https://huggingface.co/Comfy-Org/ltx-2/tree/main/split_files/text_encoders) `gemma_3_12B_it` adapted by team Comfy
  - [HF:unsloth/gemma-3-12b-it-GGUF](https://huggingface.co/unsloth/gemma-3-12b-it-GGUF/tree/main) `gemma-3-12b-it-Q4_K_S.gguf` possibly not suitable?
- Alternatively [HF:GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn](https://huggingface.co/GitMylo/LTX-2-comfy_gemma_fp8_e4m3fn/tree/main)
  - `gemma_3_12B_it_fp8_e4m3fn` - The fp8 converted text encoder from comfy, goes in CLIP folder
  - `ltx-2-19b-dev-fp4_projections_only` - Extracted projections from LTX-2 model to allow loading with DualClipLoader node, goes in CLIP folder
  - `ltx-2-19b-dev-fp4_video_vae` - The video vae, can be loaded with VaeLoader node, goes in VAE folder
  - `ltx-2-19b-dev-fp4_vocoder` - The vocoder model, not useful separately currently
- If using Comfy native nodes and workflows
  - code and template workflows merged to ComfyUI main branch (nightly)
  - Comfy native workflows do not require custom nodes from `Lightricks/ComfyUI-LTXVideo`
- If using LTX developers' nodes and workflows
  - [GH:Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/) nodes
  - [GH:Lightricks/ComfyUI-LTXVideo:example_workflows](https://github.com/Lightricks/ComfyUI-LTXVideo/tree/master/example_workflows)
  - [docs.ltx.video/open-source-model/integration-tools/comfy-ui](https://docs.ltx.video/open-source-model/integration-tools/comfy-ui)
  - still need Comfy nightly (likely)


> does the model go in diffusion_models folder?
> no, in checkpoints folder

> what folder does the spatial upscaler go in
> `models/latent_upscale_models`

From LTX developers:

> If you are using the custom node (from the LTXVIDEO repository)
> you must download the entire model folder from Hugging Face:
> [HF:google/gemma-3-12b-it-qat-q4_0-unquantized](https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized/tree/main)
> after downloading, place the folder in your models directory and configure the ComfyUI node to point to:
> `gemma-3-12b-it-qat-q4_0-unquantized/model-00001-of-00005.safetensors`
> Do not delete or move the other `model-0000X-of-00005.safetensors` files. 

## Advice

> euler simple or ddpm 2 karras are safe combos

> Using the full model with the distill lora at 0.6 makes skin far more natural than just using the distill model. Shame it's so RAM heavy.

## Tools For LTX-2

- [HF:Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left)

# Outdated Tools For LTX 0.9

- [HF:Lightricks/LTX-Video-ICLoRA-depth-13b-0.9.7](https://huggingface.co/Lightricks/LTX-Video-ICLoRA-depth-13b-0.9.7)
- [HF:Lightricks/LTX-Video-ICLoRA-detailer-13b-0.9.8](https://huggingface.co/Lightricks/LTX-Video-ICLoRA-detailer-13b-0.9.8)
- Simple WAN refiner workflow which can be used after LTX main run and upscaler: [Experiment_upscaler_wrapper.json](workflows/ltx/Experiment_upscaler_wrapper.json)
