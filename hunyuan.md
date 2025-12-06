# Hunyuan

## 2025.12.05

Distilled version of 480 model released by Tencent and repackaged for Comfy:
[link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/diffusion_models/hunyuanvideo1.5_480p_i2v_step_distilled_fp16.safetensors)
Both cfg and step distilled, allows generations in 4-12 steps.

> seems to need at least 8 steps most of the time, shift 7.0;
> avoid the fp8 unless you have to use it;
> full model, but possibly Lora could be extracted;
> no 720 distilled model yet

Note: "sr" in model names on [HF](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/tree/main/split_files/diffusion_models) means "super resolution", e.g. upscaler

## Summary

Latest is version 1.5 up to 10 sec generations.

Load models from [HF:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/tree/main/split_files)
Place into ComfyUI folder names following the structure on HF.

Native Comfy implementation available in latest `main` branch

SageAttention supposedly better quality than EasyCache