# Statements

## Kijai Q&A

> Q: does the anisora model work with the usual lightX2v loras ?  
> A: the 3.2 is already distilled, so no need for that, the older versions do work with the loras  
> and it's better than lightx2v or lightning too for high noise  
> 8 steps  
> I also extracted it into a lora that works ok https://huggingface.co/Kijai/WanVideo_comfy/blob/main/LoRAs/AniSora/Wan2_2_I2V_AniSora_3_2_HIGH_rank_64_fp16.safetensors

> Q: In wrapper we can't use flashattn?  
> A: at least flash2, I never tried 3  
> [WanVideo Uni3C Controlnet Loader] uses it's own attention so never added [flashattn] there

## Random Claims

These claims have not been verified. Neither has the rest of this website :)

Loras trained on Wan2.1-VACE-14B-diffusers work though not perfectly with WanAnimate.

Negative prompt is ignored with CFG=1 in wrapper samplers but can be re-enabled by using `WanVideoNAG` node.

Not bad for realism: 250928 from [LoRAs/Wan22-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning/tree/main) 0.7 strength, 1.4 CFG, 3 steps on WAN 2.2 low noise.
