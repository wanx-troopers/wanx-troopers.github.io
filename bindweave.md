# BindWeave

## BindWeave In ComfyUI

- [GH:kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper) contains nodes to run Bindweave in "wrapper" workflows
- [GH:drozbay/WanExperiments](https://github.com/drozbay/WanExperiments) contains nodes to use Bindweave in native workflows - and said to work quite well including CLIP Vision and QwenVL - which actually don't seem to improve the outputs

Fp8 model weights adaptation by Kijai: [link](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Bindweave)

## Comments

2024.11.10 QwenVL part is not working, code still not in wrapper main branch

Trained from Wan 2.1 I2V 720p

Very strong character consistency

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

> When you pad the input noise latent to match the i2v channels input, do those 4 frames also get set to zeros or do you just pad with "gray" frames?
> Zeros

> Q: if you had no references hypothetically, your input latent into the model would be 32 channels of just zeros for the first four latent frames? all zeros all the way down? (not including the 4 mask channels I mean, which would be 1's right?) 
> A: The first 4 in the noise channel are zeros; In the cond channel those are references 
> Q: yeah but they are also zeros if the references aren't there right? just hypothetically?
> A: If you only have single reference, then first would be the ref latent + it's I2V mask, which btw is actual box mask not full frame;
> And the 3 after that, in the cond channel, would be zeroes, mask too;
> What they do is mark the original area white, and the padded are black if it's for example square reference and you generate wide aspect;
> They mostly used face crops so those were always padded and thus always masked

> Q: Do you per chance know if in bindweave we apply mask to conditioning? 
> A: there's always a mask in I2V conditioning, 1 marks the input image and 0 is what's generated, usually that's full frame mask, in Bindweave however they mark the original area 1 and possibly padded area 0 in addition. 
> there's no latent mask per se, it's automatically created with the I2V node already;
> if you were to add Bindweave references to it, they'd need to be masked similarly

> Q: Bindweave is pretty sensitive to the  positioning and scale of reference?

See also: "conditioning" [details](conditioning.md#details).