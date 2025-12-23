# LongCat Avatar

## 2025.12.23

> the old distill LoRA for LongCat-Avatar is suboptimal way to use it, and they are training a specific new one for Avatar,
> so right now the results aren't best it can do if you use the distil, and if you don't it's super slow

> they also said they are working on 24fps version because the 32/16 fps it's now has some lipsync issues
> this model now actually uses 32 fps as input an samples the audio with stride of 2, so the output is 16 fps video

## Summary

Following in the trail after Infinite Talk, Humo and Wan S2V we now have `LongCat Avatar`.
`LongCat Avatar` seems to be based on [LongCat](../longcat.md),
and able to use same LoRA-s, at least to an extent.

The purpose of `LongCat Avatar` appears remarkably similar to [HuMo](../humo.md) and [Infinite Talk](../infinite-talk.md).
Actually it appears that the same team which created MultiTalk/InfiniteTalk is behind this model.

As of 2025.12.23 Kijai has added code supporting `LongCat Avatar` in `ComfyUI` to main branch
in [Wrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper).

One of the relevant nodes:

![WanVideoLongCatAvatarExtendEmbeds](../screenshots/longcat-avatar/WanVideoLongCatAvatarExtendEmbeds.webp)

> `prev_latents` is where it continues from, the overlap amount of frames are taken from it,
> `ref_latent` is used to insert that latent in the sequence at the `ref_frame_index` position (latent space),
> which is how it keeps the reference consistency in longer extensions

Model and LoRA-s: [HF:Kijai/LongCat-Video_comfy](https://huggingface.co/Kijai/LongCat-Video_comfy/tree/main).

Reportedly around 10 steps is necessary

> It feels like you get diminishing returns pretty early when increasing step count.

> reference method always has the initial frame to use, so it still should not burn.

> The audio_cfg makes it twice as slow, you can try without it but usually the lipsync suffers a lot

> **The audio_cfg has major impact on the lipsync, so that's the main thing to adjust**

> 1 minute without degradation, using the old distill lora (at 0.8 str), audio_cfg 3.0, text cfg 1.0, 12 steps with the longcat distil schedule

> you can do v2v already;
> this helps to slice the correct part of the input video for each window

![slicing.webp](../screenshots/longcat-avatar/slicing.webp)

> at the moment there is only the bf16 model for longcat_avatar;
> for the normal longact video there is a fp8 version;
> You can run a bf16 at fp8 though

> are you using the chinese-wav2vec?
> the chinese model is the only one that works ... because it's trained with this one

`wav2vec-chenese-base_fp16.safetensors` `bf16`

> do not use sageattn 1.0.6, need sage 2.2.0 or sdpa

Youtube [tutorial](https://www.youtube.com/watch?v=eZTdaLbzqL4)
