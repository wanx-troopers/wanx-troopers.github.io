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

> Q: Is it possible to merge a lora into a GGUF model ?  
> A: Would need to do that to bf or fp16 model and then conver that to GGUF

## rCM

Kijai extracted LoRA from a new distillation of WAN 2.1 T2V done by NVidia-associated developers: [Kijai/WanVideo_comfy LoRAs/rCM](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/rCM).
Can be used with WAN 2.1 and possibly 2.2 T2V models.
User:
> rcm at strength 4.0 on high has been working pretty decent for me; I'm using rank148 rcm at high 4.0 shift 7 + lightning at 1.0 on low. 4 steps dpm++sde

Not recommended for I2V, a user:
> I work mostly in I2V and I found that the rCM Lora changes stuff too much when used in Low.
> Identify shifts .. don't think it really helped in High either.
> If I get the strength high enough that it starts having an effect it starts creating more artifacts.
> In theory an I2V version can be trained, but Nvidia said they weren't going to do it.

## Noteworthy Loras

Kijai 2025-Oct-14 (this refers to high noise wan 2.2 too):
> well the thing is that nothing beats the old 2.1 lightx2v still"  
> 6 steps, split in middle and first step with cfg 2.0  
> strength 3.0 for high and 1.0 for low

Kijai 2025-Oct-18
> There are only 3 options for the low noise:
> * original 2.1
> * lightx2v
> * 2.2 Lightning rCM

> If we don't count accvid/fast wan etc. That, in my opinion, changes the output too much from original
> Though with that criteria I'd forget the 2.2 Lightning as well pretty much

Kijai 2025-Oct-19
> Q: Kijai, which one are you using still the i2v 480 or t2v rank 64 and 3.0 with high and 1 with low?..  
> A: Something like that  
> Q: and a pinch of cfg on high, right?  
> A: First step at least

| Repo | Lora | Generation | Comment |
| --- | --- | --- | --- |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_HIGH_Lightning_4steps_lora_250928_rank128_fp16 | 2.2 T2V | new, recommended |
| Kijai/WanVideo_comfy | LoRAs/Wan22-Lightning/<br>Wan22_A14B_T2V_LOW_Lightning_4steps_lora_250928_rank64_fp16 | 2.2 T2V | - |
| Kijai/WanVideo_comfy | [LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/Wan22_Lightx2v/Wan_2_2_I2V_A14B_HIGH_lightx2v_MoE_distill_lora_rank_64_bf16.safetensors) | 2.2 I2V |  new, recommended, only high,<br>worthy of attention;<br>ghosting with simple scheduler but not linear quadratic?<br>can do good motion and camera motion |
| Kijai/WanVideo_comfy | LoRAs/rCM/<br>Wan_2_1_T2V_14B_rCM_lora_average_rank_148_bf16 | 2.1 T2V | new from NVidia, give it a try? should preserve motion |
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
| high: [256 rank lightx2v lora](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank256_bf16.safetensors)<br>low: unknown|high: [new distill 4 step I2V base model](https://huggingface.co/lightx2v/Wan2.2-Distill-Models)<br>low:regular Wan 2.2 I2V Low?|accidentally combining seems to massively amp up the amount of motion in shots that just the distill or just the lora doesnt achieve on their own|


Note: "dyno" model does patching which cannot be done by a lora.

## Reward Loras

Re HPS and MPS "reward" loras: "if it's not human-domain these loras are not going to well well do to rewards heavily biased towards people aesthetics. So say, doing a demon, it'll be more human than demon".

## Special Use

Wan 2.1 and 2.2 LoRA-s:

* [Cseti/wan2.2-14B-Kinestasis_concept-lora-v1](https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1)
* [Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1](https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1) aka Walgro
* [Charlietooth/wan2.1-14B-lora-punk-style](https://huggingface.co/Charlietooth/wan2.1-14B-lora-punk-style/tree/main) - a mix of cartoonish and realistic look
* Nebsh's [Lazy Susan Rotation Wan 2.2](https://www.runninghub.ai/model/public/1979104800396709889) trained on I2V but works on T2V too. (Simple but costly way to train: https://wavespeed.ai/models/wavespeed-ai/wan-2.2-i2v-lora-trainer, this one at 150steps was $7.5, trained on 6 videos from Higgsfield).	
* Car/Clorth/Product consistency: [drnighthan on HuggingFace](https://huggingface.co/drnighthan)

## Both Ways

A number of models exist both as models and as LoRA-s.

| Model | Notes |
| --- | --- |
| Dyno | T2V Wan 2.2 High |
| Wan 2.2 I2V Moe Distill Lightx2v | I2V Wan 2.2 High only |
| CauseVid | Wan 2.1, can be used as Wan 2.2 Low |

## Idea For High CFG

Skimmed CFG from [Extraltodeus/Skimmed_CFG](https://github.com/Extraltodeus/Skimmed_CFG).
High CFG in the sampler helps to follow the prompt, skimming prevents the burn issue.

## Some Interesting Words

> Lora = low-rank matrix factorisation  
> Loha = hadamard product matrix factorisation   
> Lokr = kronecker product matrix decomposition  
> In bongmath language