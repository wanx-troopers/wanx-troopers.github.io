# Wan 2.2 I2V Conditioning

## Drozbay Study

[drozbay](https://github.com/drozbay) has shared the following workflow

![drozbay_testembeds_wani2vmasks.png](screenshots/drozbay_testembeds_wani2vmasks.png)
[drozbay_testembeds_wani2vmasks](screenshots/drozbay_testembeds_wani2vmasks.png)

This workflow is using nodes from his [GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments).

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


## See Also

- [Conditioning](conditioning.md)
- HuMo last-image to first-image [extensions](humo.md#drozbay)