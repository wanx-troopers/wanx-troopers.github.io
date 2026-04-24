# Known Bugs And Recommended Software Versions

The page needs a brush-up. Bugs referenced have been fixed or worked around. Still might be useful info.

## 2026.04.24

[fredbliss](https://github.com/fblissjr):
> been working on sage optimizations.. 
> not sure how specific this is to my setup (sm89 / rtx 4090, ltx video w/ a frozen audio mask input), but sharing ...
> was using the woct0rdho fork of sage (even tho on linux).. it has some updates over the thu-ml original.

> found two things:

> packaging omission, woct0rdho fork only:
> sm80 build gate is 8.0, 8.6, 8.7 — no 8.9.
> so on rtx 40xx / ada, building from source silently skips
> `_qattn_sm80` and `sageattn_qk_int8_pv_fp16_cuda` (the fp16 fallback) is just missing.
> one liner fix in `setup.py` and only matters if you build from source on an ada-only [RTX 40xx]
> box and explicitly pick the fp16 kernel.
> auto-dispatch picks fp8++ on sm89 anyway

> cuda mask path silently drops masks - the original sage repo thu-ml lineage, every fork, inherent to all sageattention (2.x AND 3.x).
> the cuda kernels only understand `{none, causal}` masks..
> so if you pass an `attn_mask` tensor to `sageattn_qk_int8_pv_fp16_cuda` / `sageattn_qk_int8_pv_fp8_cuda` / `sageattn3_blackwell directly`,
> it gets blackholed into kwargs and never applied.
> math still runs, just against unmasked scores.
> output is wrong in proportion to how much of kv you masked.
> I measured rtol [Relative Tolerance] `0.26` to `0.94` on ltx cross-attn shapes, `NaN` outright at very short kv.
> the triton kernel `sageattn_qk_int8_pv_fp16_triton` has proper mask plumbing and stays at rtol `~0.04`.

> so what actually matters in practice, at least in what i've been working on / researching
> normal video self-attn, no explicit mask - fine. sage still `~2.7x` faster than `torch flash` on ltx shapes (tested);
> any workflow with an explicit `attn_mask` - text prompt padding, audio token masks, controlnets, long-text encoders..
> from what i can tell, the cuda path silently returns bad outputs if a node talks to it directly.
> i havent tested all of these but it would make sense the are impacted.

> KJNodes addresses this issue at the node level. KJNodes ships two sage nodes and both solve what they're designed to do:
> - `PathchSageAttentionKJ` (the general dropdown one): on `auto` it calls sage's top-level dispatcher, which internally routes
>    masked calls to `triton`, so you get the safe path by default. you only expose the underlying sage bug if you
>    manually override to `sageattn_qk_int8_pv_fp16_cuda` / `sageattn_qk_int8_pv_fp8_cuda` / `sageattn_qk_int8_pv_fp8_cuda++` / `sageattn3` / `sageattn3_per_block_mean`... 
>    those bypass the dispatcher and talk to the broken cuda wrappers directly
> - `LTX2MemoryEfficientSageAttentionPatch` (the ltx-specific one) only patches `self-attn` (`attn1`), which doesn't carry a mask in ltx.
>    tuned for the fp8++ path on sm89 (the fast one). scope alone means the mask bug can't hit it

> [GH:fblissjr/SageAttention-ada](https://github.com/fblissjr/SageAttention-ada) fork: one-liner fix [for setup.py on RTX 40xx] +
> an ltx-shape regression test + a standalone repro [reproducer] for the mask bug

## 2026.01.10

As of now Torch 2.11.0 remains too new. Workarounds in Comfy/Wrapper code are not aware of it yet. oom on decode has been reported with 3x memory consumption.

## 2025.12.29

> Which is a good Numpy version? I updated your wrapper and it installed 2.2.6 which broke multiple other nodes;
> Not sure about that, some older stuff just won't work on any numpy 2 version;
> seedvr2 seems to be impacted by this, guess i'll have to manually downgrade

## 2025.12.27

> Sage 3 really doesn't seem all that great.
> for now, Sage 2.1/2.2 are still the mainstream options.

> Sage3 quality loss on 2.1 was way too high to be useful;
> fp8 fast works far better with 2.2 and is even usable,
> while it never was for 2.1

## 2025.12.10

> B200 and onward is so good is because they have a giant L2 cache so cache issues are lowered

## 2025.12.06

> would you recommend migrating to 2.9.1 ? yes

> Comfy comes with pytorch 2.9.1 ... now

Unfortunately it looks like the [fix](https://github.com/woct0rdho/triton-windows/commit/440e3c42a640a4188dd356225e1b13a56b45a377)
bringing fp8e4 support to RTX30xx on Windows has not been implemented on Triton
[mainline](https://github.com/triton-lang/triton/blob/main/third_party/nvidia/backend/compiler.py#L188);
[issue](https://github.com/triton-lang/triton/issues/8929).

## 2025.11.16

[Sam Hodge](https://www.imdb.com/name/nm1668128/) suggested a script to install Sage Attention on Ubuntu 24.04 with an RTX 5090 in the following manner

```
ENV  TORCH_CUDA_ARCH_LIST='8.0,8.0+PTX,8.6,8.6+PTX,8.9,8.9+PTX'
RUN git clone https://github.com/thu-ml/SageAttention.git && \
  cd SageAttention && \
  git reset --hard eb615cf6cf4d221338033340ee2de1c37fbdba4a && \
#  sed -i "/compute_capabilities = set()/a compute_capabilities = {\"$TORCH_CUDA_ARCH_LIST\"}" setup.py && \
  EXT_PARALLEL=4 NVCC_APPEND_FLAGS="--threads 8" \
  MAX_JOBS=32 uv pip install -e . --no-build-isolation --break-system-packages
```

## 2025.11.10

Python 3.12 is probably a good idea

Possible startup arguments: comfy --here launch -- --reserve-vram 5 --max-upload-size 500 --use-sage-attention --disable-pinned-memory

Note: --async-offload can cause OOM-s

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

https://github.com/woct0rdho/triton-windows - read instructions on the page, not simply `pip install sageattention -U`
https://github.com/woct0rdho/SageAttention

Youtube tutorial on installing SageAttention 2.2 on Windows - unconfirmed, advice from community: [9APXcBMpbgU](https://www.youtube.com/watch?v=9APXcBMpbgU).

## Different Attentions

> How does Sage Attention compare against Flash Attention and Sdpa Attention?
> sage >>>>>>>>>>>>>>> flash > sdpa, slight exaggeration

> they all degrade quality?
> only Sage

> "degrade quality" in this context means everything you do to differ from the reference code, like reducing steps etc.
> the quality loss from sage is so small in most cases that you can more than offset it from the speed gain

> Flash Attention is something you have to install if you want to use the actual flash attention, the sdpa flash is different thing
