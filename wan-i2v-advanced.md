# Wan I2V Advanced

## Morphing

- [Ingi](https://x.com/ingi_erlingsson) suggested to auto-generate prompts like the following to facilitate morphing
  ```
  {
    "prompt": "A cinematic, seamless VFX video featuring a woman standing amidst dense, dark green foliage and vibrant pink bougainvillea flowers. She has shoulder-length brown hair with bangs and wears a beige turtleneck sweater with diagonal brown stripes and blue jeans, her hand gently touching a flower. A magical transition effect initiates a fluid metamorphosis. The woman's posture smoothly lowers from standing to sitting without breaking continuity, her raised hand gliding down to rest on her lap. Simultaneously, the texture of her beige wool sweater ripples and darkens, morphing into a smooth, navy blue short-sleeved top with white buttons. Her jeans liquefy and reshape into a flowy, patterned blue and white skirt. Her hair shimmers, lightening from brunette to blonde and pulling back as sunglasses materialize atop her head. The surrounding environment participates in the transition; the chaotic wall of dark leaves recedes and smooths out into a bright, manicured green lawn, while the pink bougainvillea blooms shift hue to become delicate purple flowers in the foreground. A rustic stone and wood bench rapidly grows out of the ground beneath her to catch her settling form, completing the transformation from a lush garden thicket to a sunny park setting in one continuous, dreamlike motion."
  }
  ```

- [CA:2052865/flippinrad-motion-morph](https://civitai.com/models/2052865/flippinrad-motion-morph?modelVersionId=2323211) LoRA
  created by [FlippingSigmas](https://x.com/FlippingSigmas), aka `Flipping Sigmas' AnimateDiff`  
  [Drozbay](hidden-knowledge.md#drozbay) suggested starting with strength 0.3
  > low strength ... does help with the morphing, so experiment with the strengths.
  > If you set it too high you get a lot of abstract objects and cute faces floating in the center of the video

Morphing has been successfully achieved on I2V and can probably work with VACE / T2V.

## HuMo I2V and SVI-shot

Since HuMo is an I2V member of Wan family of models, the [work](humo.md#drozbay-continuations) done by Drozbay to enable [SVI-shot](svi.md#svi-shot)-powered HuMo extensions clearly is a new Wan I2V trick.

The node and workflow discussed in the referenced page faciliate using [SVI-shot](svi.md#svi-shot) LoRa to provide an additional reference to I2V generations.
This counters visual degradation that commonly happens in extension workflows.
Sadly this approach does not facilitate continuity of motion.

Happily this can be applied in normal I2V workflows unrelated to HuMo.

## I2V Video Inpainting

Apparently it has long been possible to use masks when doing V2V processing via I2V models. As of now this website doesn't contain a complete workflow, however here is a hint into how to setup such workflow:
[i2v-masks](screenshots/i2v-masks.webp)

## I2V Keyfarming

It has been proven possible to supply middle frames to I2V in addition to start/end frames. Workflow building hints:

- [wrapper-wf-fragment](screenshots/wan22-i2v-middle-frames-wrapper.webp) the wrapper I2V node already does that, you can use the VACE start/end frame node to create the batches and masks, and that goes into the start image and temporal mask
- [wan22-i2v-middle-frames](screenshots/wan22-i2v-middle-frames.webp)
- [full wf - fixed](workflows/wan22_4frames_interp.json) (earlier this page had a link to [this](workflows/Wan2.2-sub-v0.4.json) which was likely an error)
- work-in-progress [wf](workflows/Wan2.2&Humo_FMML_VRGDG_WIP.json) from [VRGameDevGirl](https://github.com/vrgamegirl19/comfyui-vrgamedevgirl); "Q: HIGH model 2.2 to generate general motion, and HUMO as LOW model to refine and do lipsync? A: you can use any model as the 1st pass: t2v + VACE, Wan2.1FLF, magref, Wananimate"

## FFGO

New high/low Wan 2.2 I2V LoRa-s which allow supplying subjects/objects and background all in the 1st frame on white background
- read [GH:zli12321/FFGO-Video-Customization](https://github.com/zli12321/FFGO-Video-Customization)
- download [HF:Kijai/WanVideo_comfy:LoRAs/Wan22_FFGO](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/LoRAs/Wan22_FFGO)

Workflow building [hint](screenshots/ffgo.webp) Prompt: `ad23r2 the camera view suddenly changes ...`

Works well for anime characters.

Apparently works with [holocine](storymem-holocine.md#holocine)

An artist:
> tested FFGO ... more trouble to set up correctly ... than i would like to spend time

## TimeToMove

Insipired by [time-to-move/TTM](https://github.com/time-to-move/TTM), a promising body of code for converting rough mock-ups into smooth AI videos
which re-juvenates an old approach which existed as early as CogVideoX days Kijai added 
`WanVideo Add TTMLatents` node now in [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
and provided an [example wf](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo2_2_I2V_A14B_TimeToMove_example.json)

Additionally Kijai has added `Latent Inpaint TTM` node to [GH:kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) bringing TTM support to native workflows. `Latent Inpaint TTM` [example](screenshots/native-ttm.webp),
[workflow screenshot](workflows/native-ttm-wf.webp).
  
The workflows are not very easy to use and require a fair bit of trial and error. [Official tool](https://github.com/time-to-move/TTM/tree/main/GUIs) is used to generate driving video.
Mockups use character pictures with a white outline around them.

Ignores Uni3C.

### TimeToMove Workflow Setup Details

Low noise step is somehow more problematic.
Removing Lightx2V on low seems to help a bit.

General advice is to only use [1030](loras/part-01.md) lightx2v LoRa on high - or no LoRa at all.
People have been trying setups both with and without a speed LoRa on low.
Apparently if using a speed LoRa on low then accurate prompt becomes very important.

One no-LoRa setup shared:
> 50 steps, 25/25 split, 3.5 cfg, 8 shift and 3 start and 7 end step

`unipc` may be a good scheduler to use. In order to use `dpm++` it is advisable to
> stop the reference one step before the last step of high noise

[VRGameDevGirl](https://github.com/vrgamegirl19/comfyui-vrgamedevgirl)'s wip native [wf](workflows/VR-native-ttm.json).

### TimeToMove Masks

The process requires that a mask is supplied.

- One approach is to take the "control" (e.g. rouch mockup video which is already being fed into the process) and pass it via `Convert Image To Mask` and then connect to `mask` input. It's possible to take on one of RGB channels
- Alternatively success has been reported with supplying a solid black mask

### TimeToMove Ideas

- [GH:kijai/ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) also contains `Cut And Drag On Path` node.
- [GH:wallen0322/ComfyUI-AE-Animation](https://github.com/wallen0322/ComfyUI-AE-Animation) contains `AE Animation` node which is another good way to prepare control videos for TTM.
- [GH:Verolelb/ComfyUI-AE-Animation-English-Mod](https://github.com/Verolelb/ComfyUI-AE-Animation-English-Mod) a fork of the above fully translated into English. Additional flip and scale features.
- `Cut And Drag On Path` node from [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)

Half-cooked 3d can be supplied. One way to produce:
> blender, put the image on a subdivided plane and use the depth map to displace the geometry, then animating the camera

DepthAnything 3 can be useful generating .glb. Possibly MoGe. Possilby https://huggingface.co/spaces/facebook/vggt

> Try reducing the end step on the LTT node, you might get more motion, so wan is a bit more free earlier during sampling to generate motion since it won't stick as close the reference

It has been hypothesised that having the moving character both as part of the initial image and as part of the control video increases the chances of creating an unwanted 2nd copy of the character.

> If we want TTM to follow the movements of the original video without adding characters or anything else not requested in the prompt, setting fewer steps on the TTM node helps. .. 2 steps out of 6 steps ... and maybe the denoise should be between 0.7 and 0.8

## TTM Without TTM

It has been discovered that specially constructed V2V workflow around Wan 2.2 I2V achieves results similar to TTM and/or FFGO without either of them.

- put two people side-by-side facing front into one reference image
- supply it 4 times
- put background as 5th reference image
- create driving video similar to TTM, encode it to latents
- plug it into the 1st Wan 2.2 I2V sampler as latents
- set denoise to 0.7-0.8, enable add_noise on 1st sampler

No WF currently available.

## FFGO without FFGO aka VACE at Home aka Phantom at Home

Discovered in Wan 2.1 times I2V model is capable of using FFGO style references on its own.
The trick was to place the reference into starting frame and issue a prompt like

> Immediate cut to a new scene, a laboratory. The item at the start of the video is on a man's wrist

## Masks

Here is a slightly non-traditional way to build masks. Please note that actual value 0 vs 1 may be opposite between wrapper and native workflows.

![build-masks-manually](../screenshots/build-masks-manually.webp)

## See Also

- [Wan Masking](wan-masking.md)
- [Video Blending From Fragments](tools-list.md#video-blending-from-fragments)
- [Context Windows](what-plugs-where/context-windows.md)
