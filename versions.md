# Known Bugs And Recommended Software Versions

The page needs a brush-up. Bugs referenced have been fixed or worked around. Still might be useful info.

## 2025.11.10

Possible startup arguments: comfy --here launch -- --reserve-vram 5 --max-upload-size 500 --use-sage-attention --disable-pinned-memory

Around 16-17 Oct 2025 issues were reported with latest version of Comfy and other packages. Workflows started consuming more VRAM than previously. Among workarounds suggested were

## VAE Bug

One advice was to use fp32 version of Wan 2.1 VAE safetensors file; possibly a command line option might be needed as well.

[Workaround](https://github.com/comfyanonymous/ComfyUI/commit/19b466160c1cd43f707769adef6f8ed6e9fd50bf) has been commited to ComfyUI.

Kijai 17 Oct 2025 evening:
> torch 2.9.0 has a bug that makes some conv3d operations (when using half precision) use 3x more VRAM, including the Wan VAE;
> it affects 2.10 too currently;
> both native and wrapper has workaround for the bug already anyway; they are different workarounds

## Higher VRAM Usage Realted To Triton

Another source of higher VRAM usage was traced to triton compilation. It seems one particular reason was tritop upon seeing too many errors gave up on compiling. The other was that triton was recompiling too often. Suggestions were

* clean triton caches manually and restart ComfyUI
* set `force_parameter_static_shapes` to `false` in `TorchCompileModelWanVideoV2`
* manually edit `comfy/model_patcher.py` file adding `@torch.compiler.disable()` one line above `class LowVramPatch:`
* commented out all `run_every_op()` from ops.py - this will undo "fast cancellation" change

Kijai 18 Oct 2025:
> The workarounds for the cancellation call and the torch compile disable on the
> problematic bit of the code are merged to comfyUI already btw

> pytorch 2.8.0 was problematic so sticking with 2.7.0 was fine  
> 2.9.0 has one problematic bit that needed workarounds for Wan VAE,  
> so that needs latest ComfyUI version to work  
> I'm on 2.10.0 dev and seems to work too

> Triton 3.5 is what should have the e5 compile fix;

For Windows it's `triton-windows 3.5.0.post21` or later.

> pytorch 2.8.0 works fine in Linux

> and then if you happen to decide to update nvidia drivers on Linux you lose a week of your life   
> Q: ubuntu has nvidia drivers, doesnt it?  
> A: I mean latest drivers; the prebuilt stuff is fine, but usually very outdated  
> from distros with nvidia drivers built in I liked PopOs myself, but then I wanted some newer stuff and went with Debian-testing


## Sage Attention

> SageAttenion 2.2.0 latest
> highly recommended, gets rid of all graph breaks so torch compile works better

[windows install](https://github.com/woct0rdho/SageAttention) - read instructions on the page, not simply `pip install sageattention -U`
