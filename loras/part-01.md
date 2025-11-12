# LoRa-s, Part I

## LoRa-s Table Of Contents

* [Loras Alchemy](alchemy.md)
* LoRa-s Part I; this document
* [LoRa-s Part II](part-02.md)
* [Both Ways](both-ways.md)

## Noteworthy Loras

### 2025-Oct-10

There's
- 2.1 Lightx2v, that works fine with 2.2 low noise
- 2.2 Lightning for both high and low (and it's different versions), has exposure issue and not best motion
- 2.2 Lightx2v 4 step distill for high noise, that has 3 versions so far:
  - the initial called "MoE"
  - 1022 date update
  - 1030 date update

### 2025-Oct-14 (this refers to high noise wan 2.2 too):

> well the thing is that nothing beats the old 2.1 lightx2v still  
> 6 steps, split in middle and first step with cfg 2.0  
> strength 3.0 for high and 1.0 for low

### 2025-Oct-18

> There are only 3 options for the low noise:
> * original 2.1
> * lightx2v
> * 2.2 Lightning rCM

> If we don't count accvid/fast wan etc. That, in my opinion, changes the output too much from original.
> Though with that criteria I'd forget the 2.2 Lightning as well pretty much

### 2025-Oct-19
> Q: which one are you using still the i2v 480 or t2v rank 64 and 3.0 with high and 1 with low?..  
> A: Something like that  
> Q: and a pinch of cfg on high, right?  
> A: First step at least

### 2025-?-?

Users chatting:

> Q: what the best lora for t2v ? lightx?  
> A: lightx quantile 0.15 Lora from Kijai, its very good; for high 3.0 low 1.0 Strength

### In A Table

| Repo | Lora | Generation | Comment |
| --- | --- | --- | --- |
| [HF:Kijai/WanVideo_comfy:LoRAs/Wan22_Lightx2v](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v) | Wan\_2\_2\_I2V\_A14B\_HIGH\_lightx2v\_4step\_lora\_v1030_rank_64_bf16: [link](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_4step_lora_v1030_rank_64_bf16.safetensors) | 2.2 I2V high only | new and reportedly much better with prompt adherence |
| [HF:lightx2v/Wan2.2-Distill-Loras](https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/tree/main) | wan2.2\_i2v\_A14b\_ (high/low) noise\_lora\_rank64\_lightx2v\_4step\_1022 | 2.2 I2V | new; high superceeded by 1030 |
| [HF:Kijai/WanVideo_comfy:LoRAs/Wan22_Lightx2v](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_Lightx2v) | Wan\_2\_2\_I2V\_A14B\_HIGH\_lightx2v\_MoE\_distill\_lora\_rank\_64\_bf16: [link](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors) | 2.2 I2V high only |  superceeded by 1022 and 1030<br> ghosting with simple scheduler but not linear quadratic?<br>can do good motion and camera motion |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_HIGH_Lightning_4steps_lora_250928_rank128_fp16 | 2.2 T2V | - |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_LOW_Lightning_4steps_lora_250928_rank64_fp16 | 2.2 T2V | - |
| Kijai/WanVideo_comfy | LoRAs/rCM/<br>Wan_2_1_T2V_14B_rCM_lora_average_rank_148_bf16 | 2.1 T2V | new from NVidia, give it a try? should preserve motion |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16 | 2.1 I2V | Old but good, worth a try on 2.2 |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16 | 2.1 T2V | - |
| Kijai/WanVideo_comfy | Lightx2v/<br>lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16 | 2.1 T2V | some artists find this good on 2.2 |
| Kijai/WanVideo_comfy | FastWan/<br>FastWan_T2V_14B_480p_lora_rank_128_bf16 | 2.1 T2V | very old but worth a try |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Wan2.1_T2V_14B_FusionX_LoRA | 2.1 T2V | very good for 2.1 |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Wan2.1_I2V_14B_FusionX_LoRA | 2.1 I2V | very good for 2.1 |
| vrgamedevgirl84/Wan14BT2VFusioniX | FusionX_LoRa/<br>Phantom_Wan_14B_FusionX_LoRA | 2.1 T2V | real trooper for 2.1 |

## Allegedly Good

Combinations of LoRAs and models that allegedly produced good results for some artists.
Vastly incomplete.

| LoRAs | Models | Notes | HF fp8_e4m3 | HF bf16/fp16 |
| :--- | :--- | :--- | :--- | :--- |
| high:none<br>low:Wan22_A14B T2V_LOW Lightning_4steps_lora 250928_rank64_fp16 | high:Wan2.2-T2V-A14B-4steps-250928-dyno-high-lightx2v<br>low:some wan 2.2 | Good motion | high:[Kijai/WanVideo_comfy_fp8_scaled/T2V](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V) | high:[lightxv2/Wan2.2-Lightning/dyno](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main/Wan2.2-T2V-A14B-4steps-250928-dyno)<br>low:[Kijai/WanVideo_comfy/LoRAs/Wan22-Lightning](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22-Lightning)|
| both high/low: lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors | Wan 2.2 T2V High/Low | - | - | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v) |
| high: lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank256_bf16<br>low: ?|  Wan 2.2 T2V High/Low | 2.5 str on high | - | [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lightx2v) |
| high: [256 rank lightx2v lora](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors)<br>low: unknown|high: [new distill 4 step I2V base model](https://huggingface.co/lightx2v/Wan2.2-Distill-Models)<br>low:regular Wan 2.2 I2V Low?|accidentally combining seems to massively amp up the amount of motion in shots that just the distill or just the lora doesnt achieve on their own|


Note: "dyno" model does patching which cannot be done by a lora.

## Special Use

Wan 2.1 and 2.2 LoRA-s:

* Wan 2.2 Smartphone LoRa
* [Cseti/wan2.2-14B-Kinestasis_concept-lora-v1](https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1)
* [Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1](https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1) aka Walgro
* [Charlietooth/wan2.1-14B-lora-punk-style](https://huggingface.co/Charlietooth/wan2.1-14B-lora-punk-style/tree/main) - a mix of cartoonish and realistic look
* Nebsh's [Lazy Susan Rotation Wan 2.2](https://www.runninghub.ai/model/public/1979104800396709889) trained on I2V but works on T2V too. (Simple but costly way to train: https://wavespeed.ai/models/wavespeed-ai/wan-2.2-i2v-lora-trainer, this one at 150steps was $7.5, trained on 6 videos from Higgsfield).	
* Car/Clorth/Product consistency: [drnighthan on HuggingFace](https://huggingface.co/drnighthan)
* [Gouache](https://www.oxen.ai/shadowworks/public/dir/main) - lora and workflows, for Wan 2.1 14B I2V