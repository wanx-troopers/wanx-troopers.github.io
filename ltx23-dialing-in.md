# Dialing In LTX 2.3 Workflow

Main article: [LTX 2.3](ltx23.md)

## 2026.05

Nekodificador on avoiding blurry mess instead of motion

> changing sigmas helps a lot
> try karras or exponential
> at least on a second pass

huddadudd, on the setup that allowed generation of nice turning humans:

> exponential/etdrk2_2s clownshark 8 steps

## 2026.04.27

> 1.1 distilled in mxfp8 which seems good

> Q: in ltx [does] using varying models of gemma affects the output?
> A: between the fp8 and bf16 versions, it's minimal difference

Dev + the Distill LoRa 1.1 seems better than Distill 1.1.

> Q: why would the dev + LoRa be slower?
> A: because you can't apply lora in fp8 it has to do the upcast to apply, then downcast to fp8 to do the matmul;
> a checkpoint with the lora applied at half strength would probably be useful;
> ... when you use fp8 checkpoint + bf16 lora, the lora is higher quality

David Snow:
> if you use the distill lora on a second pass using a negative weight, it reduces the plastic skin greatly.
> so when using it for upscale set strength to a negative?
> Yeah. -0.4 is a good starting point.

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

PhoenixRisen:
> Seems euler_ancenstral_cfg_pp is the best for prompt adherence; [Mark]: runs like a dog on mine so I dont go near cfg_pp version

[Mark](https://markdkberry.com):
> I switched to euler_ancestral recently was using lcm but find it best in the wf I use.

## cfg_pp Samplers

[Drozbay](hidden-knowledge.md#drozbay):
> fyi: any of the cfg_pp samplers will always run both a positive and negative conditioning pass even on cfg 1.0.
> So if you're comparing euler_ancestral at cfg 1.0 to euler_ancestral_cfg_pp at cfg 1.0, the latter will always be 2x slower

[Mark](https://markdkberry.com):
> its way more than x2 slower on my rig ...
> ... it runs ... NAG as well so would that mean it is x4 slower?
> (audio and video conditioning in NAG)

[Drozbay](hidden-knowledge.md#drozbay):
> NAG is definitely not going to be as much extra compute as CFG since it only operates on cross-attention;
> CFG is literally just twice as slow, it runs two fully separate calls at the same step.
> Also, I dunno if NAG even runs for the negative pass
