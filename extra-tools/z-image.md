# Z-Image-Turbo

## 2025.12.06

>  found the biggest benefit to running z-image came from having qwen 8b instruct write the prompts;
> 4b instruct is a close second

> Can anyone suggest the best k-sampler settings for realistic outputs?
> Euler ancestral and bong tangent are a killer combo. Possibly er_sde & sgm_uniform

ZIT is said to have "ruts" - tendency for repetition: "ruts are medium shot, certain people, certain angles" - because it is distilled.

> using a model like Josie that isn't 'the same old', causes Zimage to hit 'less' ruts.  It's reintroducing triggering tokens finding remaining less used paths that aren't gone but are avoided in favor of the rut.

## 2025.12.05

Z-Image-Turbo consists of 3 parts

- variant of Qwen3 LLM - prompt is passed through most of LLM layers and results are taken out after meaning has been encoded but before they were used to guess the next word
- Z-Image-Turbo core - that's where image generation happens
- VAE - converts results from latent space to pixel space

[Scruffy](https://huggingface.co/scruffynerf) has suggested using alternative flavor of Qwen3 and an alternative VAE in order to improve Z-Image-Turbo results.
His currently preferred LLM is
[Josiefied-Qwen3-4B-Instruct-2507-gabliterated-v2](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-Qwen3-4B-Instruct-2507-gabliterated-v2)
and his currently preferred VAE is
[G-REPA/Self-Attention-W2048-3B-Res256-VAEFLUX-Repa0.5-Depth8-Dinov2-B_100000 VAE](https://huggingface.co/AlekseyCalvin/Custom_VAE-Z-image-FLUX.1-by-G-REPA).

Apparently these can be downloaded separately.
Scruffy has also assembled all three components into a all-in-one 33 Gb `.safetensors` which he called [JoZiMagic](https://huggingface.co/scruffynerf/JoZiMagic).

Note: had we not been limited by VRAM on present generation of consumer video cards we could have used a bigger version of LLM, namely
`Goekdeniz-Guelmez/Josiefied-Qwen3-14B-abliterated-v3`. Note: Z-Image-Turbo uses Flux.1 style VAE. Flux.2 VAE meanwhile is apache licensed
and likely to get used for new models in the future.

Mysterious "shift" formula from Scruffy:
> (\<base_shift\> - \<max_shift\>) / (256 - ((\<image_width\> * \<image_height\>) / 256)) * 3840 + \<base_shift\>

Decrease in image quality and composition has been reported above 2048 resolution.

## 2025.12.03

[Z-Image-Turbo-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union)
support for Z-Image-Turbo has been added to ComfyUI.
Technically the new facility is closer to VACE than to ControlNet-s of the past in its architecture.
The new `Controlnet-Union` supports Pose, Canny, Hed, and Depth guidance.

Limitation: only one LoRa can be successfully applied. Applying a combination leads to bad results, probably because Z-Image-Turbo is highly distilled.

## 2025.11.26

6B `Z-Image-Turbo` is a distilled image generation model released under Apache license. Community is raving :) Model re-uses Flux VAE but appears not be based on Flux.
[Model page](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) promises non-distilled and edit versions to be released. "beats flux 2 .. at a fraction of the size ... less plastic than qwen image".

The stock ComfyUI workflow for z-image is quite traditional: `Clip Encoder` users `qwen_3_4b` to encode user prompt and feed it to `KSampler`.
The surprise is that `Z-Image-Turbo` had been trained on conversation sequences which have then been encoded by `qwen_3_4b`.

A number of projects have emerged to help take advantage of this.
Most prominently there is [GH:fblissjr/ComfyUI-QwenImageWanBridge](https://github.com/fblissjr/ComfyUI-QwenImageWanBridge).
As the [explanation](https://github.com/fblissjr/ComfyUI-QwenImageWanBridge/blob/main/nodes/docs/z_image_intro.md) says:

> There's no LLM running here. Our nodes are text formatters - they assemble your input into the chat template format,
> wrap it with special tokens, and pass it to the text encoder. The "thinking" and "assistant" content is whatever text YOU provide.

If using an LLM the project recommends using "Qwen3-0.5B through Qwen3-235B" because they also use `qwen_3_4b` and tokens produced by them are passed without re-encoding.

Then there are other projects which do make use of LLM-s to help generate the prompt.
One is discussed [here](https://www.reddit.com/r/StableDiffusion/comments/1parzxf).

## Qwen-3B Layers

Qwen-3B has been described as passing the text through the following layers

```
Input tokens
      ↓
  [Embedding layer]
      ↓
  Layer 1  (-36)  ← earliest, closest to raw input
  Layer 2  (-35)
  ...
  Layer 18 (-19)  ← middle
  ...
  Layer 35 (-2)   ← Z-Image default
  Layer 36 (-1)   ← LAST, just before vocab projection
      ↓
  [LM Head → logits → token prediction]
```

By default z-image-turbo is getting Qwen-3B output from the line marked with -2.
However it is technically possible to modify ComfyUI code such that the image is produced based on Qwen3 output from any of the earlier layers.
Some of them result in gibberish but many will result in images, different from the one we get by default.
We probably should expect it to be implemented - some time soon?..

## Older

`CRT-Nodes` added `LoRA Loader (Z-Image)(CRT)`. It can load `zit-ivy.safetensors`

## Notable LoRA-s

- [detail-slider](https://civitai.com/models/2202638/detail-slider-for-z-image) note: strength can be -2 to +2, greater values mean more details
- [detaildeamonz](https://civitai.com/models/2209262/detaildeamonz-sliderlora-for-zimageturbo-and-redz15) note: strength can be -2 to +2, greater values mean less details
