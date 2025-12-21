# LongCat Avatar

Following in the trail after Infinite Talk, Humo and Wan S2V we now have `LongCat Avatar`.
`LongCat Avatar` seems to be based on [LongCat](../longcat.md),
and able to use same LoRA-s, at least to an extent.

The purpose of `LongCat Avatar` appears remarkably similar to 

As of 2025.12.20 the code supporting `LongCat Avatar` in `ComfyUI` is [longcat_avatar](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/longcat_avatar)
branch in Kijai's [Wrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) repository on Github. One of the relevant nodes:

![WanVideoLongCatAvatarExtendEmbeds](../screenshots/longcat-avatar/WanVideoLongCatAvatarExtendEmbeds.webp)

Model and LoRA-s: [HF:Kijai/LongCat-Video_comfy](https://huggingface.co/Kijai/LongCat-Video_comfy/tree/main).

Reportedly around 10 steps is necessary

> The LongCat dev said they are working on 24fps version though, as there are lipsync issues with this 16 fps setup.
> It feels like you get diminishing returns pretty early when increasing step count.
> For short clips at least seems fine to use less, maybe the extension quality will suffer on long runs.
> But this reference method always has the initial frame to use, so it still should not burn.


