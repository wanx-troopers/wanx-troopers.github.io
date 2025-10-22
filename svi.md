# SVI

Experimentation with SVI is in its early stages. Loras are on [HF:vita-video-gen/svi-model](https://huggingface.co/vita-video-gen/svi-model/tree/main/version-1.0),
[article](https://github.com/vita-epfl/Stable-Video-Infinity).

The intent is to generate videos longer than 81 frames with smooth transitions.
Degradation artifacts such as exposure and contrast increasing with each 81 frames step as well as loss of character consistency are rampant.

These are loras for Wan 2.1 480p I2V model. Distill LoRa is applied by the authors in the article. Workflow/nodes to use are very similar to Fun InP model.

> shot lora with 1 frame yes, film with 5

> Normally the I2V conditioning is added in extra channel.
> * 16 channels for noise
> * 16 for image conditioning
> * 4 for image conditioning mask
>
> The image cond channel normally is the start image + black pixels for rest.  
> The mask marks the image as 1 and the black pixels as 0.

> Q: need to tick `fun_or_fl2v_model` in `WanVideo ImageToVideo Encode` ?  
> A: only if you use end img

Rought sketch of a workflow: [link](workflows/wanvideo_480p_I2V_SVI-shot_test.json).

One way to replicate padding from the article:
![svi-fragment.webp](screenshots/svi-fragment.webp)
