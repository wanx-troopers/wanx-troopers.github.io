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

## rCM

New distillation of WAN 2.1 from NVidia associated developers: [code](https://github.com/NVlabs/rcm), [data](https://huggingface.co/worstcoder/rcm-Wan/tree/main). Kijai has extracted a LoRA which can be used with WAN 2.1 and possibly 2.2 models.

## Noteworthy Loras

| Repo | Lora | Generation | Comment |
| --- | --- | --- | --- |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_HIGH_Lightning_4steps_lora_250928_rank128_fp16 | 2.2 | new, recommended |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_LOW_Lightning_4steps_lora_250928_rank64_fp16 | 2.2 | - |
| Kijai/WanVideo_comfy | [LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors) | 2.2 |  new, recommended, only high worthy of attention |
| Kijai/WanVideo_comfy | LoRAs/rCM/<br>Wan_2_1_T2V_14B_rCM_lora_average_rank_148_bf16 | 2.1 | new from NVidia, give it a try? should preserve motion |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16 | 2.1 | Old but good, worth a try on 2.2 |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16 | 2.1 | - |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16 | 2.1 | some artists find this good on 2.2 |
| Kijai/WanVideo_comfy | FastWan/<br>FastWan_T2V_14B_480p_lora_rank_128_bf16 | 2.1 | very old but worth a try |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Wan2.1_T2V_14B_FusionX_LoRA | 2.1 | very good for 2.1 |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Wan2.1_I2V_14B_FusionX_LoRA | 2.1 | very good for 2.1 |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Phantom_Wan_14B_FusionX_LoRA | 2.1 | real trooper for 2.1 |

## Allegedly Good

Combinations of LoRAs and models that allegedly produced good results for some artists.
Vastly incomplete.

| LoRAs | Models | Notes | HF fp8_e4m3 | HF bf16/fp16 |
| :--- | :--- | :--- | :--- | :--- |
| high:none<br>low:Wan22_A14B T2V_LOW Lightning_4steps_lora 250928_rank64_fp16 | high:Wan2.2-T2V-A14B-4steps-250928-dyno-high-lightx2v<br>low:some wan 2.2 | Good motion | high:[Kijai/WanVideo_comfy_fp8_scaled/T2V](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V) | high:[lightxv2/Wan2.2-Lightning/dyno](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno)<br>low:[Kijai/WanVideo_comfy/LoRAs/Wan22-Lightning](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning)|
| both high/low: lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors | Wan 2.2 T2V High/Low | - | - | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v) |
| high: lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16<br>low: ?|  Wan 2.2 T2V High/Low | 2.5 str on high | - | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v) |

## Special Use

Car/Clorth/Product consistency: [drnighthan on HuggingFace](https://huggingface.co/drnighthan)

Cseti/wan2.2-14B-Kinestasis_concept-lora-v1: [Cseti/wan2.2-14B-Kinestasis_concept-lora-v1](https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1)