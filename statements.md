# Statements

## Kijai Quotes

> WAN 2.2 VAE is only for 5B model; Ovi is based on 5B

### AniSora

> Q: does the anisora model work with the usual lightX2v loras ?  
> A: the 3.2 is already distilled, so no need for that, the older versions do work with the loras  
> and it's better than lightx2v or lightning too for high noise  
> 8 steps  
> I also extracted it into a lora that works ok https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/AniSora/Wan2_2_I2V_AniSora_3_2_HIGH_rank_64_fp16.safetensors

### Flash Attention

> Q: In wrapper we can't use flashattn?  
> A: at least flash2, I never tried 3  
> [WanVideo Uni3C Controlnet Loader] uses it's own attention so never added [flashattn] there

### Lora Merging

> silly to merge to fp8 scaled model  
> Q: so merging the bf16 model with any loras then converting them down would be the best way  , yes ?  
> A: yeah always merge at highest precision you can and only then quant it  
> if you end up only using the quantized version it may not matter -that- much, but still as rule of thumb

## Random Claims

These claims have not been verified. Neither has the rest of this website :)

Loras trained on Wan2.1-VACE-14B-diffusers work though not perfectly with WanAnimate.

Negative prompt is ignored with CFG=1 in wrapper samplers but can be re-enabled by using `WanVideoNAG` node.

Not bad for realism: 250928 from [LoRAs/Wan22-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main) 0.7 strength, 1.4 CFG, 3 steps on WAN 2.2 low noise.

Tiled vae doesn't work with vace extend - makes generated part blurry and the position is slightly shifted ???
Kijai: looked at the code and since that doesn't set the tile size, it's set by dividing the width and height by half, so that probably creates badly sized tiles for some resolutions or something
I believe these are the original defaults: tile_size=(34, 34), tile_stride=(18, 16)
so 720 would be 90 in latent space, than in half you get 45 tile size
dunno why it wouldn't work really
unless it's VACE issue in general and it just doesn't like tiled encode

Apparently SDE samplers are not a good fit when distilled loras/models are in use
> DE samplers add noise they can do harm at low steps  
> If you want a general good safe sampler then UniPC is good

Kijail on SEC segmentation mode
>  the sec model still is SAM2.1, it's just extra guidance for it, the segmentation is still just SAM

Re choice of attention for RTX3090: flash is deprecated, sage 3 fast but quality is bad, sdpa is the best for quality, radial is for longer gens;
radial also takes a noticable quality hit, which might not be that bad for a lot of gens;
another user: "but I noticed in, infinitetalk as an example, it really muted the expressiveness of lip syncs";
original commenter: "sage 1 is still quite good".

Take a subject and their motion and put it in a new setting/style (via img/txt);
take a subject's motion but replace the subject (via img/txt) in the same setting/style:
Wan Animate for humans, VACE for objects.

One way to "uplift" a video: normal t2v workflow, except pass input video to vae encoder, then pass to ksampler with like 0.5-0.7 denoise.

5+5 cfg  3 is nice for closeups.

Florence is too good; Used it for like 2 years at this point lol.

Wan 2.2 High with MPS Reward + Magref Low (RCM distill Lora for both strength 1) - sort of works; LayerForge node to put a character or two, the node can remove their background with Matting button, white background.

The movement tends to be better for t2v; sometimes its great to get a good base video from a good t2V and then u can paint over it.