# Chronological News on LTS 2.3

## 2026.06

Echo is work based on LTX 2.3

- a seemingly random related github repo [GH:smthemex/ComfyUI_JoyAI_Echo](https://github.com/smthemex/ComfyUI_JoyAI_Echo)

## 2026.05

A bug confirmed in ComfyUI: ever since LTX 2.3 release when guides' strengths is set to any value other than 1 VRAM usage grows.

Bug fixed including improvements to how Sageattention is used - bringing results closer to what happens with default SPDA.

Guide strength can now be set above 1: "it's not exactly linear, so 2.0 isn't twice as strong, but it definitely has an affect.. could be useful for first to last frame etc."

[Drozbay](hidden-knowledge.md#drozbay):
> The decoder working without tiled efficiently is mostly a consequence of rattus' dynamic VRAM implementation ...
> It is amazing, it started off shaky, and I  kept going back to regular offloading. but it kept getting better and now it's hard to imagine going back

LTX 2.3 Inference code fix coming: [PR#14097/issuecomment-4552771980](https://github.com/Comfy-Org/ComfyUI/pull/14097#issuecomment-4552771980)
[Drozbay](hidden-knowledge.md#drozbay): "that only really matters when using a reference audio tokens like for ID-Lora or lipdub, and even there the effect isn't gigantic"


## 2026.05.08

Native VAELoader can now load LTX 2.3 audio VAE

Hint: `bf16` can be a good format for VAE-s

## 2026.04.29

VRAM usage decreased many times for Tiny VAE, yes LTX 2.3 has a functional tiny VAE: [PR #13617](https://github.com/Comfy-Org/ComfyUI/pull/13617)
