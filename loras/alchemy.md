# Lora Alchemy

## LoRa-s Table Of Contents

* Loras Alchemy; this document
* [LoRa-s Part I](part-01.md)
* [LoRa-s Part II](part-02.md)
* [Both Ways](both-ways.md)

## Trivia

LoRAs often work with models they were not designed for.

People sometimes experience a placebo effect - using LoRAs that neither enhance nor hinder good results.

If several LoRa-s are used together the order of application does not matter.

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

## Some Interesting Words

> Lora = low-rank matrix factorisation  
> Loha = hadamard product matrix factorisation   
> Lokr = kronecker product matrix decomposition  
> In bongmath language

## Special Use

Wan 2.1 and 2.2 LoRA-s:

* [Cseti/wan2.2-14B-Kinestasis_concept-lora-v1](https://huggingface.co/Cseti/wan2.2-14B-Kinestasis_concept-lora-v1)
* [Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1](https://huggingface.co/Cseti/LTXV-13B-LoRA-Wallace_and_Gromit-v1) aka Walgro
* [Charlietooth/wan2.1-14B-lora-punk-style](https://huggingface.co/Charlietooth/wan2.1-14B-lora-punk-style/tree/main) - a mix of cartoonish and realistic look
* Nebsh's [Lazy Susan Rotation Wan 2.2](https://www.runninghub.ai/model/public/1979104800396709889) trained on I2V but works on T2V too. (Simple but costly way to train: https://wavespeed.ai/models/wavespeed-ai/wan-2.2-i2v-lora-trainer, this one at 150steps was $7.5, trained on 6 videos from Higgsfield).	
* Car/Clorth/Product consistency: [drnighthan on HuggingFace](https://huggingface.co/drnighthan)
