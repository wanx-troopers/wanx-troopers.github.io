# Training

## Captioning Example

zz134ab woman with long brown hair, wearing a white dress with sheer puffed sleeves and front buttons, stands indoors in a spacious room with wooden ceilings and large windows, posing by adjusting her hair and placing hands on her hips under natural, bright lighting

## Baseline

artificial_fungi:

> The speedrun/baseline idea is that you start with the lowest and most conservative settings first.
> This ensures that your settings are correct, your paths work, your models work, and your environment is functioning.
> The baseline is the minimum necessary to produce a functional LoRA.
> It is not a compromise, it is a foundation to build on.

> The LoRA you train at [256,256] on 25 images at batch 1, GAS 1, repeats 1, DIM/ALPHA 16/16, LR 0.0001, using bucketing, in dual-mode, for 35-40 epochs will work. 
> I'm not sharing this to confuse or mislead people, and I gain nothing either way.

> Use the speedrun settings, even if you own a 5090. Then adjust for your data and goals and hardware.

> Some observed speedrun durations:  
> 3060 12gb: 1 hour and 41 minutes  
> 4060 ti 16gb: 56 minutes  
> 3090: 36 minutes  
> 5090: 14 minutes
