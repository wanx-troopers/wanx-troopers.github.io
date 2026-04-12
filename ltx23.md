# LTX 2.3

LTX 2.3 uses Gemma 3 12B as multi-modal text encoder. Gemma is by Google.

## From The Makers

[HF:Lightricks](https://huggingface.co/Lightricks) provide

- ltx-2.3-22b-dev, separate distilled model, alternatively a distillation LoRa
- ltx-2.3-spatial-upscaler-x2-1.1, ltx-2.3-spatial-upscaler-x1.5-1.0, ltx-2.3-temporal-upscaler-x2-1.0
- LTX-2.3-22b-IC-LoRA-Union-Control

They also provide under LTX-2 umbrella

- Lightricks/LTX-2-19b-IC-LoRA-Detailer "still usable with 2.3 , thought it was only available for 2"

## Samplers

Hmm.. `LTXVLoopingSampler`... what is it?..

## IC LoRa-s

IC LoRa generally stands for "in-context LoRa" a _type_ of LoRa. In colloquial speak "IC LoRa" generally refers to one of the IC LoRa-s released alongside LTX 2.3:
[Union Control](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control), Motion Track or Depth/Canny/Pose.
Additional Python code to use them: [GH:Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/).

## Keyframing

Different ways to do FLF: LTXVAddGuide, LTXVImgToVideoInplaceKJ.

[YT:What Dreams Cost/Guide to Prompting and Keyframing I2V](https://www.youtube.com/watch?v=ZY4hsvTzbas)

### ImgToVideoInplace

Alternative to using guides. Kijai's version also allows to specify which frame to apply to: ![LTXVImgToVideoInplaceKJ](screenshots/ltx/LTXVImgToVideoInplaceKJ.webp)

[Drozbay](hidden-knowledge.md#drozbay):
> The inplace nodes are very simple: they don't add any guide latents or anything they just replace the target latent frame with the encoded image and mask it so it doesn't change

### Guides

> guides are latent+mask but they exist at the end of the sequence, and are applied to the position through RoPE;
> so basically they are stored at the end, keyframe info is stored (through the conditioning in comfy) so it knows what frame it should affect;
> that's why using full guide video is so heavy, and that's why the newer guide method halves the guide resolution

`LTXVCropGuides` removes the guides from latents after generation: ![cropGuides.webp](screenshots/ltx/cropGuides.webp)

Specifying the index as -1 allows the reference to show an object before it enters the frame and then to heavily prompt for it.
-1 means before the 1st latent. 0 had been reported to work too. This is about `LTXV Add Latent Guide`
in `LTX Video` node pack, not about `LTXVAddGuide`.

[YT:4TE-QbtkiGQ](https://www.youtube.com/watch?v=4TE-QbtkiGQ) for some advice on using guides to inject frames.

[YT:nekodificador](https://youtube.com/nekodificador) reported plugging the same guide image twice via both of the following nodes increases motion
[twoGuidesMoreMotion](screenshots/ltx/twoGuidesMoreMotion.webp)

## Inpainting

- inpaiting can be done with reference using Alisson's LoRa (see bellow).
- alternatively [YT:nekodificador](https://youtube.com/nekodificador) reported success has placing a large rectange over person's mouth in video and using "just straight inpainting with native nodes and distiled lora"
  additional details: [pcvideomask:PC Video Mask Smooth](screenshots/nodes/pcvideomask-pc-video-mask-smooth.webp) from [GH:pavelchezcin/pcvideomask](https://github.com/pavelchezcin/pcvideomask)
  + sampler=linear/euler + scheduler=exponential were reported to help with detailing part of the video - mouth in this case;
  audio then guided lip motion

## Three Pass Workflows

Zombiematrix:
> use the either of the default templates and change the starting pass to go to .25 of the starting resolution (instead of .5)  
> then add a second upscale pass. thats all it is. you can use either of the upscalers (1.5 or 2.0)

Jonathan (WhatDreamsCost):
> I've been testing a 3 stage workflow for the past month, mainly because I see better motion when the 1st stage is at a lower resolution.
> Also I like it for testing prompts. Since the 2nd stage is faster, you can get a clearer preview quicker when using the tiny vae
> compared to using just 1 or 2 stages. And when you use CacheDiT on top of that, you can test prompts even faster.

[Mark DK Berry](https://markdkberry.com):
> For LTX, I go 480 x 201 first pass so I can make structure quickly util I get what I want ...
> then upscale twice for 2nd pass from v2v in LTX and I am at 1080p in 10 mins,
> and final is polisher low denoise to fix eyes and whatnot, often with a WAN model denoise 0.2 using USDU;
> any higher [denoise] the tiling or weird speckldeing creeps in but you could do a full detailer method
> but the USDU is faster and works on low VRAM. I am using 1.3b for this atm. still testing it, but its half the time of the 14B for me.
> ... just tested Wan 2.1 self forcing DMD 1.3b and its good enough for most fixups at 0.2 denoise

> Q: 40 steps on base dev at 0.25 res, 3 with distill at x2 upscale, and 3 again with x2 upscale? Is this all linear quadratic schedule?  
> A by Garbus: That's it, and er_sde across all three. Distill LoRA on 2 and 3 set to about 0.6 usually is best.
> (I only use the preview node on the first sampler since it can cause an OOM on the upscale, and there's nothing new to see there anyway.)

> Q: When you run ... Wan step how well does it deal with identity preservation?  
> A by Mark: use phantom 1.3b or WAN 2.2 VACE self forcing 1.3b (which is i2v effectively).
> and keep denoise low but with phantom you cant go over 0.5 it gets weird but
> consistency is kept so far in tests both with phantom and VACE 1.3b. HuMO would be better
> but my rig cant wait for it. I wish MAGREF did a 1.3b I would have used that but.
> I tested 5b wan but it wasnt very good which was weird.  
> Q: Do you end up doing context windows for a long base LTX gen to not run out of RAM?
> A by Mark: no, I use USDU then you dont need all that. it handles it. its in the wf
> [links](https://markdkberry.com/workflows/research-2026/#video-pipeline-workflows)
> for my video pipeline. have a look.

- [LTX-23-T2V-3PASS](workflows/ltx/garbus-LTX-23-T2V-3PASS.json) WF from Garbus: "This is the
  default LTX T2V wf with some things added and subgraphs unpacked. It's not pretty, but it works, or should give you an idea what modifications to make to a wf you prefer"
- [ai_hakase's wf](https://x.com/ai_hakase_/status/2040417832769585194?s=20)

N0NSens on flickering in three pass workflows:
> I think it's because of LTXVImgToVideoInplace at upscaler passes. At first frames it's combining lowres latent from prev
> pass and your input image. So far, the only way I found to reduce this effect is to cut off first 3 frames and lower Inplace str to 0.7

> just matching to ref helps in this case

"native SUPIR implementation PR" from Kijai includes a new color matching node

N0NSense
> In my experience, the higher the initial resolution, the better the result. Therefore, 2 passes produce a better result than 3 (especially noticeable on small patterned textures). 

David Show
> but the higher the first pass resolution

[audio] "generate ... once ... all subsequent upscale passes ... reuse the originally generated audio rather than reprocessing it"

## Hints

> As long as the video is relatively static, it's amazing. As soon as there's fast motion ... [things get mushy]

> The newer ic Loras like the union one are trained with half res. 
> Latent downscale factor?
> Yes.

Vertical format videos may still be more problematic than horizontal ones, even though it was claimed they were fixed in LTX 2.3.

Lower image compression (16) helped with a crazy-looking person (no eyes) where higher compression (22) failed.

N0NSense is generating cool videos using
- cinema4d playblast render
- AIO Aux Preprocessor
- depth map
- IC LoRa

Above is also possible with LTXVImgToVideoInplaceKJ node to also use FLF.
N0NSense: emptying a glass is a practically impossible task for the model in i2v mode. The only option is FLF.
Also tested with: `Draft animation + hard cuts. depth, IC str 0.4, clwn sampler, t2v`.
"Need more detailed prompt for camera movement but seems to work".
Can be used to lock camera static: [N0NSens-static-cam-ltx23](screenshots/ltx/N0NSens-static-cam-ltx23.webp).
"ic union lora. depth" "it's based on LTX-2.3_ICLoRA_Union_Control workflow from ltx"
It is sufficient to place cubes where characters need to be and they can be rotated to make characters look the right way etc. This also covers scene cuts.
"depth at str 0.2"; "i2v, using starting image"

> ... a ... (left) does this ... a ... (right) does that. the camera abruptly changes angle: the ... is on the left in the background ... the is on the left in foreground ...


Change FPS from 24 to 25 to fix de-sync of audio

[Mark's Workflows](https://markdkberry.com/workflows/research-2026/#video-pipeline-workflows) "LTX 2.3, 10 seconds, 24 fps, 241 frames. I dont go over that, no real need. and I end on 24fps coz I like it"

[Mark DK Berry](https://markdkberry.com): I've been experimenting with Phantom 1.3B running through USDU to add the WAN back in to LTX results.
I am low VRAM so cant do 14B in under 30 mins, but 1.3B is surprisingly good and very fast even on low VRAM and manages 1080p 24fps,
241 frames in minutes fixing up some of that LTX detail issue like eyes quite well ... anyone with a decent card should be WAN 14B detailing
low denoise for polish and you'll have perfect results from LTX. Juan Gea: Yes, Wan 2.2 14B is the perfect "last pass" for LTX, or the HUMO version.

Reported as working (empty lines are extra empty lines in prompt):
> [fen] character description  
>  
> [scene] scene description  
>  
> [sound] ambience description  
>  
> [0-1s] [fen] does ... says ".."

> are these 2 still needed? Yeah they still help
![ltx-kj-additions-1.webp](screenshots/nodes/ltx-kj-additions-1.webp)

Kijai's tensor loop node "is just a utility" "it works but somewhat awkward with the audio length calculations"

[GH:fblissjr/ComfyUI-AudioLoopHelper](https://github.com/fblissjr/ComfyUI-AudioLoopHelper)
"super rough around the edges but if anyone wants. its meant to handle all those timing calcs that i didnt wanna bother with"

> Q: when using a sampler for videos, what sampler would you suggest to use for clear and fluid animation?  
> A [GH:vrgamegirl19](https://github.com/vrgamegirl19): i found that these two seem to give good results. i would try them both euler_ancestral, euler_ancestral_cfg_pp

Hicho:
> i didnt know that flf nodes accept video frames; is this how we do extension?

Two NAGs exist which can be used with LTX 2.3, "very different", "whole different method of applying"
![twoNags.webp](screenshots/ltx/twoNags.webp)

## Training

On character LoRa training: "just 30 images with 10 repeats and 10 epochs, so quick and dirty - AkaneTendo25 fork of musubi-tuner-ltx-2 - success"

10 videos from 2-8 seconds each ... if overfitted reduce strength of LoRa

Training IC LoRa requires twice the VRAM and twice the time compared to traditional LoRa-s. 5090 should generally be capable of.

[Oumoumad](https://gear-productions.com):
> I never needed to go beyond 5000 steps, in fact most of the time even in 1500 steps you already see your desired effect

## LoRa-s And WFs

- [GH:vrgamegirl19/comfyui-vrgamedevgirl:Workflows](https://github.com/vrgamegirl19/comfyui-vrgamedevgirl/tree/main/Workflows) workflows from one of the masters :) Somewhare out there there are "Claymation", "Puppet",
  [Golden Age Comic](https://civitai.com/models/2532516/ltx-23-golden-age-comic), [Enhancer](https://civitai.com/models/2535622?modelVersionId=2849716) LoRa-s by her as well
- Sir_Axe's [HF:siraxe/TTM_IC-lora_ltx2.3](https://huggingface.co/siraxe/TTM_IC-lora_ltx2.3) cartoony time to move for LTX 2.3
- Alisson Pereira's first experimental version of MR2V (Masked Reference-to-Video): [HF:Alissonerdx/LTX-LoRAs](https://huggingface.co/Alissonerdx/LTX-LoRAs)
  "It’s a reference-based inpainting LoRA ... I trained several variants, and this rank 32 one was the one I liked the most"; use `ltx23_inpaint_masked_r2v_rank32_v1_3000steps.safetensors`;
  "If you want speed, take the first frame from the generated control video, drop it into ChatGPT, and say: 'Describe this video with the object in the green area placed where the magenta mask is.' Then you add more details to it."
  "This IC  LoRa was trained for objects in general, not people." Benji's [video](https://www.youtube.com/watch?v=E_XRBRykDwE) on it;
  "The saddest part is that he seems to have changed the size of the green part on the side of the video and didn't follow the prompt recommendations I left for masked r2v";
  [ap-ltx23_masked_ref_inpaint_v1.json](workflows/ltx/ap-ltx23_masked_ref_inpaint_v1.json);
- [Cseti](https://www.youtube.com/@ChetiArt)'s LoRa to replicate camera motion from one video to another [HF:Cseti/LTX2.3-22B_IC-LoRA-Cameraman_v1](https://huggingface.co/Cseti/LTX2.3-22B_IC-LoRA-Cameraman_v1);
  README and workflow: [HFdatasets:Cseti/ComfyUI-Workflows:ltx/2.3/ic-lora-cameraman](https://huggingface.co/datasets/Cseti/ComfyUI-Workflows/blob/main/ltx/2.3/ic-lora-cameraman/README.md);
  "This one took around 20-24 hours to train with 77 video pairs. And I also made two more runs one with 128 and another with around 40 pairs. But this one looks the best so far" "I used videos from pexels"
- Dave Snow1's animemix for LTX 2.3: [HF:davesnow1/Loras:Loras/tree](https://huggingface.co/davesnow1/Loras/tree/main) "I often crank it to 1.5"
- Sir_Axe's [HF:siraxe/MergeGreen_IC-lora_ltx2.3](https://huggingface.co/siraxe/MergeGreen_IC-lora_ltx2.3) merge one video with another; apparently some green frame is involved - as a separator?..;
  "takes couple of seed tries and description of what changes, but it's also not perfect but better than just inserting start/end frames imo"
- [HF:RuneXX/LTX-2.3-Workflows:Video-2-Video/LTX-2.3_-_V2V_ReTake_recreate_any_section_of_any_video](https://huggingface.co/RuneXX/LTX-2.3-Workflows/blob/main/Video-2-Video/LTX-2.3_-_V2V_ReTake_recreate_any_section_of_any_video.json)
- Crinklypaper's [LTX-23-change-voice](workflows/ltx/crinklypaper-LTX-23-change-voice.json)
- [HF:LiconStudio/Ltx2.3-VBVR-lora-I2V](https://huggingface.co/LiconStudio/Ltx2.3-VBVR-lora-I2V) better VBVR LoRa for LTX 2.3; 100Mb smaller than the one on Civitai;
  the version on Civitai received rather cold reception; [YT:nekodificador](https://youtube.com/nekodificador): "I'm liking it for now tbh. All his cartoonish experiments im doing are way more coherent with the lora";
  seems to also make lip articulation stronger;
  "VBVR refers to a technique that enables video models such as Wan to operate in a more logical and structured way.
  Originally, it existed only for the Wan version".
- [GH:pineambassador/ComfyUI-ID-Lora-Pine](https://github.com/pineambassador/ComfyUI-ID-Lora-Pine)
  "injecting reference images at specified frames in the timeline to increase likeness retention (frontal portrait, profile portrait, re-inject the first frame, etc), without clobbering the scene"
- "LoRa motion transfer" - but might be not that necessary
- BFS LoRa "which does head swapping" [HF:Alissonerdx/BFS-Best-Face-Swap-Video](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap-Video)
- ID Lora: [GH:pineambassador/ComfyUI-ID-Lora-Pine](https://github.com/pineambassador/ComfyUI-ID-Lora-Pine) trained around 1 subject and very alpha
- ID Lora: [GH:ID-LoRA/ID-LoRA](https://github.com/ID-LoRA/ID-LoRA/tree/main) [HF:AviadDahan/LTX-2.3-ID-LoRA-CelebVHQ-3K](https://huggingface.co/AviadDahan/LTX-2.3-ID-LoRA-CelebVHQ-3K)
- [Oumoumad](https://gear-productions.com)'s outpaint LoRa: [HF:oumoumad/LTX-2.3-22b-IC-LoRA-Outpaint](https://huggingface.co/oumoumad/LTX-2.3-22b-IC-LoRA-Outpaint) - fills black bars/pillars with content
- LTX smoothmix: [CA:2524245](https://civitai.com/models/2524245/smoothmix-animations-ltx?modelVersionId=2837052) "ltx trained on smoothmix images from smoothmix sd1.5 model"
- example of what can be achived with grounded images - desaturation and lowered contrast [CA:2530917](https://civitai.com/models/2530917?modelVersionId=2844417) "AmateurHour"
- RuneXX has collected a number of workflows on HuggingFace, here's one: [HF:RuneXX/LTX-2.3-Workflows:Long-Video-Experimental](https://huggingface.co/RuneXX/LTX-2.3-Workflows/tree/main/Long-Video-Experimental)
