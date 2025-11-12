# BindWeave

2024.11.10 QwenVL part is not working, code still not in wrapper main branch

Trained from Wan 2.1 I2V 720p

Very strong character consistency

bindweave [branch](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/bindweave) on Kijai's wrapper github repository

> such a hard model to use; 3 different image inputs and all should be handled differently

> clip vision is the 224x224, so you have to crop;
> QwenVL still unsure about... not 224, and not the full res either;
> their examples are mostly faces

> Q: How high is the res of the characters images u are using. Also, can u use a video as environemntal background? 
> A: 1280x720; it's reference images, can't use video
> Q: Can't use open pose video to drive animation or character movement either?
> A: maybe unianimate

> Q: Does BindWeave have native control?
> A: No, it's just reference(s) to video. Unianimate could work, but the extra latents at start need to be compensated for.
> Not implemented yet either in Wrapper or Native. Unianimate is only available in the wrapper actually.
> It can be added to any I2V model, but as Bindweave adds 4 latents to the start, you have to compensate for that somehow.
> I did try normal I2V + references with it and it seemed to work.
