# LoRa-s, Part II

## LoRa-s Table Of Contents

* [Loras Alchemy](alchemy.md)
* [LoRa-s Part I](part-01.md)
* LoRa-s Part II; this document
* [Both Ways](both-ways.md)

Some LoRa-s that attracted attention; mostly in *reverse* order of arrival, new at the top.

## Ditto

Warning: *non-commerical license*;
Kijai's [adaptation](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Ditto);
[github](https://github.com/EzioBy/Ditto). Three LoRas:
* global
* global_style
* sim2real

Mora LoRa-s are [promised](https://github.com/EzioBy/Ditto/issues/3) in the future.

Each works on top of for VACE + WAN 2.1 + CausVid;
testing yielded mixed results;
can convert videos containing humans into animated styles, etc;
often insert a human if there isn't one already.

> Ditto is vace minus controlnet, pretty much a restyle

The node chain is VACE -> Wan 2.1 -> Ditto; VACE strength 0.975 recommended;
[example prompts](https://github.com/EzioBy/Ditto/blob/main/inference/example_prompts.txt).

> Q: is it possible to use ditto with sec for segmentation to isolate the thing we wanna change?  
> A: Yes, just like normal vace masking

Artist:
> I've done a minute w/ditto; well 20s (~600 frames); "Make it the Simpsons style";
> That's not perfect, but didn't play w/ it all that much,
> and Simpsons style was never mentioned so might just be a lucky thing it knows;
> I found the native WF worked better (at least how I was doing it);
> I did accidentally set the model to VACE (the full VACE Wan2.1 27gb model)
> instead of Wan2.1 t2v and that did seem to be be stronger somehow;
> I do have 24gb VRAM and 128gb sysram - the sysram def helps for going longer

> Make it psychedelic; as usual closeups work much better than non-closeups

> Ditto can be almost used to fix problems with Ovi generations. Ovi has major issues with mouth etc that the Ditto can fix; prompt: Make it better; ditto kinda destroys colors always

> same as vace but edit directly no need for depth video or edit first frame in edit mode like kontext

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




