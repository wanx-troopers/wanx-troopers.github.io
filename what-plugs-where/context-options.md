# WanVideo Context Options

This section is a incomplete.
`WanVideo Context Options` is a node from [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper). It is plugged into `WanVideo Sampler` and essentially provides extra parameters for it.

Enables batched video generation. Remain somewhat experimental. Known to work with the following models: 
* [Wan Animate](../wan-animate.md)
* [MAGREF](../phantom-magref.md#magref)
* ...

RAM requirements increase according to total video length across all batches.

`reference_latents` input on `WanVideo Context Options` is designed to work specifically for MAGREF. Kijai:
> it's the images used beyond the first window when using context options with I2V models

`WanVideo Encode Latent Batch` is the correct node to feed images into `reference_latents` input on `WanVideo Context Options`.

## Trying To Understand Overlap and Stride

Context Options generally have two goals:

* prevent running out of VRAM when generating longer videos
* prevent videos from looping as Wan 2.1/2.2 start generating loops if asked to work on more than 81 frames at once

Generally when working with Wan 2.2 the expectation is that `WanVideo Context Options` are plugged into both high and low noise samplers.
The rule is not absolute and it might be possible in some cases to connect to high only, especially with lots of VRAM.
It is also potentially possible to have use different `WanVideo Context Options` on high and low.

Because understanding `overalp` and `stride` is so impossibly difficult, here is a selection of quotes from Kijai to at least hint at the right direction.

Kijai:
> context options are in pixel space, so 4 is 1 latent, and overlap or stride at 4 (which is 1 latent) means it's disabled, there's no stride or ovelap, it can't be 0

> usually it's fine with something like 16 overlap, while on high noise you may need up to 48 or something;
> higher overlap = more model passes needed = slower generation, but better blending between windows

> yeah I used 10 stride 48 overlap succesfully at least [on high noise]

> stride doesn't really work with Wan, should probably remove it, context frames is the window size,
> how many frames are processed at once, and overlap is how much they overlap;
> higher overlap = smoother transitions = slower processing

Kijai when asked about stride gave a [link]() to documentation on Animate Diff and then proceeded to say
> stride is that spread out overlap thing it does as you can see in the animation;
> it's not very good with Wan model because context windows work with the latents, and every latent has 4 images;
> so stride will make it very stuttery, only time it's been useful is with 2.2 when used on the high noise only,
> and disabled for the low noise.. so it smooths it out, that works very well even

Disabled means set to 4.

## Alteranative Workflow

An interesting workflow idea has been tried: 3 `WanVideo Sampler`-s, initial one running Wan 2.2 high noise has got `WanVideo Context Options` connected, running 2 steps,
followed by another `WanVideo Sampler` without `WanVideo Context Options` also running high noise followed by another sampler without running low noise. The last two
samplers in the chain thus run with a number of frames much higher than would have been normally possible but because 1st one is batched the motion does not loop.
Incidentally dmp++_sde was used.