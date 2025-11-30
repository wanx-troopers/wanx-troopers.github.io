# HuMO

## Drozbay

2025.11.15 [drozbay](https://github.com/drozbay) has shared `droz_wanexperiments_svishot_with_humo_v1.1` worflow
![droz_wanexperiments_svishot_with_humo_v1.1](workflows/droz_wanexperiments_svishot_with_humo_v1.1.png)
[droz_wanexperiments_svishot_with_humo_v1.1](workflows/droz_wanexperiments_svishot_with_humo_v1.1.png)

This is a HuMo continuation workflow, it allows generating videos beyond the usual HuMo limit of about 4 seconds.
Continuation is made possible by the fact that
- among other types of [conditioning](conditioning.md) accepts Wan 2.1 I2V style 1st frame image -
  provided that ComfyUI implementation of HuMo model is "patched" not to erase it
- resulting slight flickering artifacts appear to become better by using [SVI](svi.md) shot LoRa

SVI-shot allows to supply an additional reference image as part of conditioning.
The manner in which it is supplied is unique to SVI-shot.

Both of these actions - patching HuMo model code and correct formatting of conditioning are
implemented in this workflow through the use of `WanEx I2VCustomEmbeds` node which 
[drozbay](hidden-knowledge.md#drozbay) has shared via the following new code repository:
[GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments)

See also: [Drozbay's Study](conditioning.md#drozbays-study) on composing and examining embeds.

## VRGameDevGirl

[VRGameDevGirl](https://github.com/vrgamegirl19/comfyui-vrgamedevgirl) is prominent artist in Video AI space known for her HuMo workflows for generating AI musical videos.
2025.11.20 she shared a work-in-progress workflow for `Wan 2.2 Humo I2V First Last Frame`, which is similar to the one above but doesn't offer continuation facility.
Here's a [copy](workflows/Wan2.2HumoI2VorFLF_WIP.webp), please beware of possible bugs.

## Notes

When using `HuMo` safetensors it may be possible to use `WanVideo Long I2V Multi/InfiniteTalk` in addition to or instead of `HuMo Embeds`.
If both are used at the same time the embeds need to do be mixed using `WanVideo Combine Embeds`.
In this case `HuMo Embeds` is plugged first and `WanVideo Long I2V Multi/InfiniteTalk` is plugged second.
`WanVideo Long I2V Multi/InfiniteTalk` in this scenario controls looping like for a regular `InfiniteTalk` generation.
It looks like `WanVideo Long I2V Multi/InfiniteTalk` additionally makes `HuMo` model respect the start frame more strongly.

`HuMo` might work with other I2V workflows as well.

It appears difficult to stop characters opening their mouth with `HuMO` (though one can try with silent audio).

Without `WanVideo Long I2V Multi/InifiniteTalk` node `HuMo` is limited to less than 4 seconds of generation.

It appears `HuMo` can use multiple reference images.

> Besides having great audio-dependent generation, even without that HuMo is the best one-shot subject-to-video model we have.
> It also works great in V2V with inpainting simply by using a latent noise mask, especially when combined with differential diffusion.


[GH:vrgamegirl19/comfyui-vrgamedevgirl](https://github.com/vrgamegirl19/comfyui-vrgamedevgirl) is a well-known workflow supporting generation of rather long music videos with HuMo.

Note: latent output from `WanHuMoImageToVideo` is simply empty just giving the sampler the right resolution and number of frames.

> The conditioning lines carry all of the references and embeddings and such.