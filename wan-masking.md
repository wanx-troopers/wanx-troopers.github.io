# Wan Masking

Along with [Context Windows](what-plugs-where/context-windows.md) this topic can be confusing.
Material here applies to all of Wan I2V/T2V, both 2.1 and 2.2.

These are related but separate concepts

- `latent masks`
- `differential diffusion`

In wrapper (as of 2025.08.21) `differential diffusion` is enabled by default and is the only way to do latent masking.

> you just add the mask and it's enabled

In native `differential diffusion` is enabled in one of two ways

- either by supplying `latent masks` "normally" and applying `Differential Diffusion` "model patch" node ![kj-enabling-differential-diffusion-native-1](screenshots/kj-enabling-differential-diffusion-native-1.png)
- or by using combined `Differential Diffusion Advanced` node from [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) ![kj-enabling-differential-diffusion-native-2](screenshots/kj-enabling-differential-diffusion-native-2.png)

Setting `latent masks` "normally" is done like this
![kj-latent-masking](screenshots/kj-latent-masking.webp)

[Sample T2V Latent Mask Workflow](screenshots/kj-sample-t2v-latent-mask-wf.webp)

Note: latent masks are separate from VACE masks. Latent masks can and should be blurry. VACE masks possibly need to be binary black/white. Both can be used at the same time in VACE workflows.

In Wrapper if a single frame of latent mask is supplied it is automatically duplicated to match `num_frames` in the video.

One way to create latent masks using [WanEx](https://github.com/drozbay/WanExperiments):
[droz-latent-masks](screenshots/droz-latent-masks.png)
