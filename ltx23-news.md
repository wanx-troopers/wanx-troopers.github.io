# Chronological News on LTS 2.3

## 2026.05

A bug confirmed in ComfyUI: ever since LTX 2.3 release when guides' strengths is set to any value other than 1 VRAM usage grows.

Bug fixed including improvements to how Sageattention is used - bringing results closer to what happens with default SPDA.

## 2026.05.08

Native VAELoader can now load LTX 2.3 audio VAE

Hint: `bf16` can be a good format for VAE-s

## 2026.04.29

VRAM usage decreased many times for Tiny VAE, yes LTX 2.3 has a functional tiny VAE: [PR #13617](https://github.com/Comfy-Org/ComfyUI/pull/13617)
