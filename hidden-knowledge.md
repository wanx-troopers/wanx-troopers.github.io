# Hidden Knowledge

By default `safetensors` files are loaded via `mmap`.

Kijai's nodes can convert between data types such as `bf16` at `safetensors` loading time.

`load_device` = `main_device` in `WanVideo Model Loader` means "keep model in VRAM".

| Kijai's Repo | Purpose |
| :-- | :-- |
| [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)| Alternative to Native KSampler, "wrapper" nodes |
| [kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)| Supplementary, can be used with Native KSampler |
| [kijai/ComfyUI-WanAnimatePreprocess](https://github.com/kijai/ComfyUI-WanAnimatePreprocess) | Nodes for Kijai's WanAnimate workflow |