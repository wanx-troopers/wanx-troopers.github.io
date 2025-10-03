# Lora Alchemy

## Trivia

LoRAs often work with models they were not designed for.

People sometimes experience a placebo effect - using LoRAs that neither enhance nor hinder good results.

## Kijai on Merging vs Unmerged LoRAs

> Normal ComfyUI behaviour with loras is to merge the weights to the model before inference,
> which can't be done to GGUF models as it would be too slow operation, so instead the lora
> weights are just added to the dequantized GGUF weight when it's used

> merging loras:
> * no VRAM hit
> * slower first run init after changing lora/lora strength
> * precision loss if using lower main model precision than the lora

> unmerged loras (GGUF or the option in the wrapper):
> * uses more VRAM
> * no init time ever
> * better lora quality as it's used directly at base precision
> * allows runtime lora strength adjusting

## Allegedly Good

Combinations of LoRAs and models that allegedly produced good results for some artists.
Vastly incomplete.

| LoRAs | Models | Notes | HF f8_e4m3 | HF bf16/fp16 |
| :--- | :--- | :--- | :--- | :--- |
| high:none<br>low:Wan22_A14B T2V_LOW Lightning_4steps_lora 250928_rank64_fp16 | high:Wan2.2-T2V-A14B-4steps-250928-dyno-high-lightx2v<br>low:some wan 2.2 | Good motion | high:[Kijai/WanVideo_comfy_fp8_scaled/T2V](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V) | high:[lightxv2/Wan2.2-Lightning/dyno](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno)<br>low:[Kijai/WanVideo_comfy/LoRAs/Wan22-Lightning](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning)|

## Noteworthy Loras

Car consistency: [drnighthan/CarConsistency-Wan2.2-I2V-ConsistencyLoRA1](https://huggingface.co/drnighthan/CarConsistency-Wan2.2-I2V-ConsistencyLoRA1/tree/main)
