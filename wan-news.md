# Wan News

## 2026.06

John Dopamine offered his [WanLooperDesigner](directors.md#wanlooperdesigner) director-style node for SVI2.2 Pro extensions for Wan capable of limited use of Bernini.

## 2026.05

[HF:lightx2v/Wan2.2-NVFP4-Sparse](https://huggingface.co/lightx2v/Wan2.2-NVFP4-Sparse)
has been released. This promises very fast Wan T2V.
Apparently possible to run in Comfy but not fully supported as a custom kernel is missing.

> The stochastic rounding kernel should be major speed upgrade for anyone using fp8 matmuls with loras and offloading, that old problem discussed here before

![kj-wan-mem-effective-sage](screenshots/nodes/kj-wan-mem-effective-sage.webp) added to `KJNodes`
> combined with ffn chunking drops peak VRAM
