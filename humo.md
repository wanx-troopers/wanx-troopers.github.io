# HuMO

## Drozbay

2025.11.15 [drozbay](https://github.com/drozbay) has shared `droz_wanexperiments_svishot_with_humo_v1.1` worflow
![droz_wanexperiments_svishot_with_humo_v1.1](workflows/droz_wanexperiments_svishot_with_humo_v1.1.png)
Earlier version: [droz_wanexperiments_svishot_with_humo_v1.png](workflows/droz_wanexperiments_svishot_with_humo_v1.png)

This is a HuMo continuation workflow, it allows generating videos beyond the usual HuMo limit of about 4 seconds.
Continuation is made possible by the fact that
- among other types of [conditioning](conditioning.md) accepts Wan 2.1 I2V style 1st frame image -
  provided that ComfyUI implementation of HuMo model is "patched" not to erase it
- resulting slight flickering artifacts appear to become better by using [SVI](svi.md) shot LoRa

SVI-shot allows to supply an additional reference image as part of conditioning.
The manner in which it is supplied is unique to SVI-shot.

Both of these actions - patching HuMo model code and correct formatting of conditioning are
implemented in this workflow through the use of `WanEx I2VCustomEmbeds` node which 
[drozbay](https://github.com/drozbay) has shared via the following new code repository:
[GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments)

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