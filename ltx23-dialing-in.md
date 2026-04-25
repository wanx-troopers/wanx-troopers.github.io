# Dialing In LTX 2.3 Workflow

Main article: [LTX 2.3](ltx23.md)

## 2026.04.24

[Ckinpdx](https://github.com/ckinpdx) on [GH:ckinpdx/ComfyUI-LTXAVTools](https://github.com/ckinpdx/ComfyUI-LTXAVTools):
> My looping sampler needs work to handle a second pass but the standard looping sampler can do it.
> Drop down the ltvx looping sampler, I use simple guider, res2s sampler and basic scheduler with beta 2 steps `.37` denoise.
> I also recently added a tiled latent upsampler as I was getting oom at that part of the process.
> If you have a recent pull of my nodes it's searchable with "tiled upsampler".
> You can give it the full AV latent, don't need to separate the latent going in.
> You do need to separate the latent going into the ltxv looping sampler though,
> only send video in and send the audio around it to final decode.
> In my v2v any to real wf i just replaced that lora with the edit anything lora ... it did work.

Advice from Torny on how to get sharp videos out of LTX 2.3:
> forget T2V (it is frustrating) go with I2v use latest kijai distilled model, 2x ver 1.1 upscaler, any of the latest Runexx workflows

## 2026.04.18

Huddadudd answering on how a good detailed 1536x832 3sec 25fps clip with a nice face in the distance:
> i've been cobbling and updating my clownshark wf for a while now, its a hodgepodge of outdated and new stuff that i just tinker with;
> currently its 4steps gauss legendre then euler 8 steps, 2nd pass is eulerancestralcfgpp
> just a basic sampler;
> run the dev model, .3 distill lora first stage .5 second stage;
> thats also without any of the uprez or refinement passes;
> zimage is the image, just standard sampling, clownshark is stage 1, which is the bulk of the sampling;
> i mostly just modify versions of able's workflows

[Ckinpdx](https://github.com/ckinpdx):
> pretty standard as far as generation parameters, one stage, dev w/ 0.6 distill, euler, linear quadratic 8 steps

## Samplers

> res_2s is good with teeth

[Ckinpdx](https://github.com/ckinpdx):
> res2s is good for quality but also handles higher fps better ... i started out with eulers, then lcm, then settled on res2s;
> the manual sigmas describe 3 steps, which works for euler in the second stage but is too many for res2s.
> for the second stage to use res2s without overbaking i use basi scheduler beta 0.34 denoise 2 steps.
> i run dev with distill and drop the distill down to 0.5 from the standard 0.6 in the second pass
![ckinpdx-ltx-dimension-calculator](screenshots/nodes/ckinpdx-ltx-dimension-calculator.webp)

Hevi:
> lcm for first stage much faster than anything else imo

`res_multistep` might be better for sound generation than `euler` with distilled.
