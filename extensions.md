# Extensions

Wan 2.1 and 2.2 models are typically limited to around 5 seconds of generation.
Some models have inherent capability to go beyond that but they need an external driving signal: [WanAnimate](wan-animate-mocha.md), [InfiniteTalk](infinite-talk.md).
An approach that remains mysterious to the maintainer of this website: [ContextOptions](what-plugs-where/context-options.md).

However there is a separate host of solutions.
We can take an existing video and generate an extension to it.
The simplest form of doing this is to run I2V generation supplying last frame from previous generation as `start_frame`.
This works but does not preserve continuity of motion - characters start moving at a different speed, in a different direction, etc.

## VACE Masks

A method which has been practiced for a while is to supply several last frame from previous generation, say 16 as initial frames
in VACE embeds. VACE masks need to be setup accordingly - so that these frames are preserved and subsequent frames are generated.
Rest of frames need to be supplied as (127, 127, 127) grey frames.

VACE naturally works with T2V models.

## I2V Masks

As a more recent discovery it appears that a number of frames from previous generation can be supplied as starting frames
into the next generation for I2V models as well.

Apparently Wan 2.2 I2V models can accept those frames without any additional LoRa-s or controlnet-like additions.
Wan 2.1 I2V models did not have this ability however.

A common problem which accompanies this kind of generation are "flashes".
On those initial frames the 2nd generation would abruptly change overall image brightness, colors or exhibit some sort of a noise pattern.
These typically last for a few frames only.
Avoiding this kind of issues is an area of ongoing experimentation.

## Drozbay Study

[drozbay](https://github.com/drozbay) has shared the following workflow

![drozbay_testembeds_wani2vmasks.png](screenshots/drozbay_testembeds_wani2vmasks.png)
[drozbay_testembeds_wani2vmasks](screenshots/drozbay_testembeds_wani2vmasks.png)

This workflow is using nodes from his [GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments).
Please view this work in conjunction with his work on HuMo last-image [extensions](humo.md#drozbay).

The above workflow demonstrates ways to prepare [conditioning](conditioning.md) data for [Bindweave](bindweave.md) and vanilla Wan 2.2 I2V.
Further this workflow demonstrates how to debug resulting embeds.

Note: "polarity" of masks - e.g. if 1 means "keep these pixels" and 0 means "generate these pixes" versus the opposite differs between
[kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) and ComfyUI native nodes.
The image above shows both ways to prepre the masks and how they look on the previews.
The difference is due to the fact that one of the implementations inverts the masks in code while the other doesn't.

TODO: a detailed write-up on what the previews on the above image actually mean and why the previews have the number of frames they have.
The number of frames actually make sense.

A key observation is that `start_image` can be not just one but several images.

Separately it is worth noting that masks don't have to be binary black or white and can contain shades of grey in between.

## Degradation

Degradation remains an ongoing problem with generating extensions.
Degradation takes two forms:

- if the character turned away in the "handover" frame(s) the likeness may be lost without some sort of reference - and not many models accept references
- video contrast tends to go up and colors tend to shift with each extra generation - this type of degradation is commonly referred to as "burnout" - again references would have solved this but it remains problematic how to supply them

[SVI-shot](svi.md#svi-shot) is one way to supply a reference, however a method has not yet been found to use svi-shot and preserve continuity of motion.
[SVI-film](svi.md#svi-film) may be a vible way to reduce "burnout" degradation; it would seem that we would need exactly 5 handover frames in this case - probably less than what we would have wanted
to preserve continuity of motion - and this doesn't help with character likeness problems. So right now it seems that we need to choose between countering character
likenes problems and countering burnout.

## Clip Vision

There is an easy way to determine if a model is using clip vision embeds.
Look at the model on Hugging face and see if it contains a `img_emb.proj` layer.
For models which do accept clip embeds they may be a viable way to counter both kinds of degradation.
Wan 2.2 models don't seem to be clip vision embeds at all, expect Wan Animate which is 2.2 only in name.
