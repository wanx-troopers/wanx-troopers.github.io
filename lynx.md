# Lynx

Lynx is a new facility to introduce character likeness from a single reference image
into Wan 2.1 (and to extent low noise 2.2) family of models for AI video generation.

Lynx appears inferior to Phantom/Stand-in.
However Kijai has provided an implementation to experiment with.
The implementation is shaped as two LoRA-s and new nodes.

Kijai:
> lite ip adapter + full ref actually works and seemingly better  
> it's not 2.2 model  
> it works somewhat on the A14B low noise  
> the ID is okayish but can't really get any motion, though probably spoiled by 2.2 by now in that regard :)

Other opinion:
> Bah the more testing I’ve done it seems lynx has no effect with wananimate.
> Running with different people for each and its just the wananimate embeds taking over even with ip str at 2.

[https://huggingface.co/Kijai/WanVideo_comfy/Lynx](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/Lynx)   
Wan2_1-T2V-14B-Lynx_lite_ip_layers_fp16.safetensors  
Wan2_1-T2V-14B-Lynx_full_ref_layers_fp16.safetensors  
lynx_lite_resampler_fp32.safetensors

```                                                              
Load Lynx Resampler (lynx_lite_resampler_fp32.safetensors) --->  | Lynx Encode Face Ip   |
                                                                 |                       |
Load Image -+----> Lynx InsightFace Crop --------------------->  | ip_image              |
            |                                                    |                       |
            |                                                    |      lynx_face_embeds |  ---> ...
            |
            |
            |      WanVideo Empty Embeds   --------------->| WanVideo Add Lynx Embeds    |
            |                                              |                             |
            |                                vae --------->|           image_embeds      |  ---> ...
            |                                              |                             |
            +--------------------------------------------->| ref_image                   |
                                                           |                             |
                    ...  --------------------------------->| lynx_ip_embeds              |
```

[Example workflow](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_T2V_14B_lynx_example_01.json)

Lynx has been tested with T2V WAN models. Kijai:
> got it to run with I2V, but dunno if it's doing anything  
> high enough ref strength and it does inject the ref into the gen... one way or the other  
> 1.5

Faster motion with Lynx? Close to 24fps.

There is an unconfirmed report of Lynx working with [Wan Animate](wan-animate-mocha-steady-dancer.md#wan-animate).

## 2024.11.11

> The reference adapter somewhat works with more than just face, the ipadapter is only face;
> lynx reference "too strong"; ip adapter "not very strong"

> Q: Are we limited to 256 on lynx ref image? 
> A: technically ref can be any size, in practice it doesn't do good with very large ones; ipadapter is hardcoded and limited
