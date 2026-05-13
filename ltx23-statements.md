# LTX 2.3 Statements

Main article: [LTX 2.3](ltx23.md)

## 2026.05

David Show: "I am using the lora loader advanced, with audio and audio to video set to 0, but that's about it." 

## 2026.05 NFT

[zghhui.github.io/OmniNFT](https://zghhui.github.io/OmniNFT/) [HF:zghhui/OmniNFT](https://huggingface.co/zghhui/OmniNFT)
some sort of reinforcement learning on LTX 2.0? - nope that LoRa doesn't work directly in ComfyUI.. 

David Show: "should still work just fine if it was trained for LTX-2"

Copy of LoRa converted to ComfyUI style keys: [HF:VasiliyWeb/OmniNFT_ComfyUI](https://huggingface.co/VasiliyWeb/OmniNFT_ComfyUI)

PhoenixRisen: "Yeah, I think it was made for t2v"

DavidShow: "T2V with LTX has a very strong colour hue by default, and if nothing else, this lora improves that greatly."  

## 2026.04.23

> Q: are you guys getting like a dot/grain pattern?
> A: that's not from the HDR lora, that's what happens if you don't use upscaler [Richard Servello]

> Q: is the ltx spatial upscaler not supposed to be sharp?
> A: if used correctly it's very sharp

## 2026.04.21

PhoenixRisen:
> motions seems to be accurate in the early steps but by the time u get to step 8 a lot of that motion is greatly removed.
> Like somebody walking seems more fluid in the early steps, walking seems much dulled down by step 8. I am using distilled saftenors 1.1.
> I noticed increasing the cfg to 2.0 helps.

## 2026.04.16

Zueuk on LTX audio latents:
> latent cut; y axis; which is unobvious;
> LTX Add Latents can combine them, but only if none -or- both of them have mask, otherwise it fails

[Ckinpdx](https://github.com/ckinpdx) on `LTX Audio Latent Trim` node:
> I added a strip mask to the audio latent trim to address that

Richard Servello:
> LTX union ic-lora was trained on a distilled sigma schedule. So you have to use their exact gradient for it to work

## LTX 2.3 Distilled V1.1

- LTX 2.3 distilled v1.1 released by LightBricks - model and LoRa - LoRa trained separately from model - LoRa allows to adjust strength - more flexible
- Motion Track & Union Control IC LoRas update

`LTXV Chunk FeedForward (for low VRAM)` - "don't touch the chunk size, it's mostly testing param and in practice 2 is enough"
"it chunks the feedforward layer (ffn) calculation, doing it in 2 chunks already puts it below other VRAM peaks
and default non-chunked is a huge spike that can be multiple GB of higher peak VRAM at larger inputs".

grimm1111: "The v1.1 distill is a noticeable improvement.  The details and coherence are improved.
I typically run the distill model with the distill lora at neg 0.2 or so. 15 steps, CFG 1; Also I only ever do single pass, that's just me.  And no temporal upscale or anything like that.
my favorite aesthetic is "movie shot in the 1990's" so I don't really go for the super HD stuff.  I like the softer analog camera look over the super-digitized look"

> distill 1.0. I feel the colours are a lot more natural. maybe just a saturation node will be enough.

mamad8:
> Using split sigmas with the distill Lora (strength 0.5) to set cfg 2 for the first 2 steps and cfg 1 for the remaining 6 steps helps A LOT, especially audio but also overall coherence and motion"

> distill 1.1 as lora str 0.6 and just works
