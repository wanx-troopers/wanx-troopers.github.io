# Extensions

Wan 2.1 and 2.2 models are typically limited to around 5 seconds of generation.
Some models have inherent capability to go beyond that but they need an external driving signal: [WanAnimate](wan-animates.md#wan-animate), [InfiniteTalk](infinite-talk.md).
An approach that remains mysterious to the maintainer of this website: [ContextOptions](what-plugs-where/context-windows.md).

However there is a separate host of solutions.
We can take an existing video and generate an extension to it.
The simplest form of doing this is to run I2V generation supplying last frame from previous generation as `start_frame`.
This works but does not preserve continuity of motion - characters start moving at a different speed, in a different direction, etc.

## UltraVico

Note: 2024.12.29 `sageattn_ultravico` implementation has been fixed to worth with resolutions other than 832x480

`UltraVico` is not an extension method in itself.
Instead this is a method of "convincing" Wan models to generate videos longer that 81 frames without looping.

Implemented on 2025.12.04 `sageattn_ultravico` is an `attention_mode` which can be chosen on `WanVideoModelLoader` in [Wrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper).

It actually implementes one of the newer methods formerly known as [RifleX](https://github.com/thu-ml/DiT-Extrapolation).

Not so bad results have been demostrated with [Kandinsky-5](k5.md).

Alternative implemenation of `UltraVico` has been tested with Wan 2.2 I2V achieving a good result, but it's not available for use at the moment.
For record the following parameters (not exposed by the current Comfy implementation) have been reported to work well:

> 0.95 alpha, 0.3 beta, 4 gamma

> 0.95 alpha for ultravico doesn't really allow the subject to leave the frame :/

## VACE Extensions

A method which has been practiced for a while is to supply several last frame from previous generation, say 16 as initial frames
in VACE embeds. VACE masks need to be setup accordingly - so that these frames are preserved and subsequent frames are generated.
Rest of frames need to be supplied as (127, 127, 127) grey frames.

VACE naturally works with T2V models.

One possible workflow from Verole: [civitai.com/models/2024299](https://civitai.com/models/2024299).

## I2V Extensions

As a more recent discovery it appears that a number of frames from previous generation can be supplied as starting frames
into the next generation for I2V models as well.

Apparently Wan 2.2 I2V models can accept those frames without any additional LoRa-s or controlnet-like additions.
Wan 2.1 I2V models did not have this ability however.

A common problem which accompanies this kind of generation are "flashes".
On those initial frames the 2nd generation would abruptly change overall image brightness, colors or exhibit some sort of a noise pattern.
These typically last for a few frames only.
Avoiding this kind of issues is an area of ongoing experimentation.

See also: [Drozbay's Study](conditioning.md#drozbays-study) for additional details on how embeds can be preapred and examined.

## HuMo Last Image to First Image Extensions

[Drozbay's WF](humo.md#drozbay-continuations)

## Degradation

Degradation remains an ongoing problem with generating extensions.
Degradation takes two forms:

- if the character turned away in the "handover" frame(s) the likeness may be lost without some sort of reference - and not many models accept references
- video contrast tends to go up and colors tend to shift with each extra generation - this type of degradation is commonly referred to as "burnout" - again references would have solved this but it remains problematic how to supply them

[SVI-shot](svi.md#svi-shot) is one way to supply a reference, however a method has not yet been found to use svi-shot and preserve continuity of motion.
[SVI-film](svi.md#svi-film) may be a vible way to reduce "burnout" degradation; it would seem that we would need exactly 5 handover frames in this case - probably less than what we would have wanted
to preserve continuity of motion - and this doesn't help with character likeness problems. So right now it seems that we need to choose between countering character
likenes problems and countering burnout.

It is believed that degradation might be happing as a result of converting data from pixel to latent space and back via VAE too many times.
An idea that often comes up then is to avoid roundtripping and just take last several latents from generation of the previous segment
and use them to kick-start generation of the next segment. This will not work however.

This is because the 1st frame in sequence is encoded differently to the rest in WAN latent space.
It takes up 4x as much bytes and subsequent frames use it as a point of reference.
If we simply chop off the last 4 latents from the previous generation (and this is 16 frames)
they will not constitute a correctly encoded sequence of frames in WAN latent encoding.

## Clip Vision

There is an easy way to determine if a model is using clip vision embeds.
Look at the model on Hugging face and see if it contains a layer called `img_emb.proj`.
For models which do accept clip embeds this may be a viable way to counter both kinds of degradation.
Wan 2.2 models unfortunately don't seem to be clip vision aware at all, expect Wan Animate which is 2.2 only in name.
