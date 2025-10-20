# LoRa-s In The Order Of Arrival

..[Lora Alchemy](LoRA-alchemy.md), part II;
some LoRa-s that attracted attention; mostly in *reverse* order of arrival, new at the top.

## Ditto

Warning: *non-commerical license*;
Kijai's [adaptation](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto);
[github](https://github.com/EzioBy/Ditto). Three LoRas:
* global
* global_style
* sim2real

Each works on top of for VACE + WAN 2.1 + CausVid;
testing yielded mixed results;
can convert videos containing humans into animated styles, etc;
often insert a human if there isn't one already.

The node chain is VACE -> Wan 2.1 -> Ditto; VACE strength 0.975 recommended;
[example prompts](https://github.com/EzioBy/Ditto/blob/main/inference/example_prompts.txt).

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

## Reward Loras

Re HPS and MPS "reward" loras: "if it's not human-domain these loras are not going to well well do to rewards heavily biased towards people aesthetics. So say, doing a demon, it'll be more human than demon".




