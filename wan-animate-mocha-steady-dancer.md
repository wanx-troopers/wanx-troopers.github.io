# Wan Animate And MoCha

Wan Animate and MoCha serve similar goals.

## Wan Animate

Two example workflows given in [Github:kijai/ComfyUI-WanVideoWrapper:example_workflows](https://github.com/kijai/ComfyUI-WanVideoWrapper/tree/main/example_workflows).
Example workflows differ in pose detection tech they provide.
[Github:kijai/ComfyUI-WanAnimatePreprocess](https://github.com/kijai/ComfyUI-WanAnimatePreprocess) github repo was used to work newer pose detection tech for WanAnimate.
Not clear if that repository is still relevant.
As of now this `example_workflow` [folder](https://github.com/kijai/ComfyUI-WanAnimatePreprocess/tree/main/example_workflows) in that repository only contains a native workflow
- which may still be of interest.

```bash
hf download Kijai/sam2-safetensors sam2.1_hiera_base_plus.safetensors # models/sam2
hf download Kijai/WanVideo_comfy_fp8_scaled Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors # models/diffusion_models
hf download Kijai/WanVideo_comfy WanAnimate_relight_lora_fp16.safetensors # models/diffusion_models
```

Important:

* either have both BG and mask connected (background from driving video)
* or have both BG and mask disconnected (background from reference image)

There are two ways to produce longer videos in a batched manner: with and without [WanVideo Context Options](what-plugs-where/context-options.md):

|Option|`WanVideo Animate Embeds`|`WanVideo Context Options`|
|:---|:---|:---|
|A|set `frame_window_size` to you batch size, say 77<br>set `num_frames` to the length of the video you want to generate|do not connect to `WanVideo Sampler`|
|B|set both `frame_window_size` and `num_frames` to the length of the video you want to generate|set `context_frames` to your batch size, say 77 or 81<br>4 is possibly correct value for `stride` effectively setting it to 'disabled'|

> The looping is done automatically in the wrapper even without context options when using the WanAnimate node;
> context options is alternative long gen method, it's biggest benefit is that it doesn't deteriorate longer it goes,
> and downside is speed and window continuation especially on backgrounds

With Kijai's nodes face video can be simply disconnected. In native nodes one may need to connect a black image/video.
Yes, the mask has to be blocky. Sometimes increasing blocks size can make things better.
Blocky mask bleeding into produced video might get fixed if face is connected.

Kijai on WanAnimate with Uni3C:
> I've had it work before, so it definitely can work

Untested but it is possible `WanAnimate` can take up to 4 reference images.

Apparently can be used with [Lynx](lynx.md).

Advice on how to stop WanAnimate adding a face to a character which doesn't have one:
> When im doing non human character dance or whatever, I always put in negative prompt - human;  
> yeah, i have that, in-fact i've translated that word into Chinese and using that

Experienced user:
> I never use positive prompt, leave it empty, only when gen video with cat then I dont know
> why but wanimate likes if you put cat in positive prompt but for everything else leave it empty

The only model with Wan 2.2 in the name to use Clip Embeds (possibly because it's truly Wan 2.1 not 2.2).

> you can adjust the audio scaling down or lock a pose with unianimate

Kijai's retargeting pose node places the stick figure in the centre of frame.
The position of the character in the reference frame (in screen space) dictates the starting position of the ViT pose (in screen space).

### WanAnimate V2 .safetensors File

Kijai:

> I named the fixed scaled fp8 model v2, which in hindsight was a mistake as people are taking it too literally  
> it's a bugfix for native workflows since there was pretty drastic noise issue in the initial fp8 scaled in native  
> [original version, so called v1 is] very slightly better in the wrapper as the face encoder layers are in bf16  

> [so-called V3 from Eddy1111111] is probably just Lora merge or something

### What Plugs Where Wan Animate

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `WanVideo ClipVision Encode` | `clip_vision`, `image_1`, `image_2`<br>-> `image_embeds`  | `Wan VideoAnimate Embeds` | `clip_embeds` / `ref_images`, `pose_images`, `face_images`, `bg_images`, `mask` | Wan 2.1 I2V family | `image_embeds` |

### Sample WF

[GT.WanAnimateLongCartoonCharacterInReal](workflows/GT.WanAnimateLongCartoonCharacterInReal.json) by Gleb.

## MoCha

Slightly newer and simpler to use than Wan Animate. Serves one function only - replace a human character for a human character in a video. Excels in applying correct lighting to the character.
Only supported in wrapper, not supported in native ComfyUI.

Based on Wan 2.1 T2V 14B. Inputs:

* source video
* one or two reference images of the replacement (one of them recommended to be a face close-up)
* a mask covering the character being replaced *in the 1st frame only* (major difference from Wan Animate which requires mask to be masking the character in all frames)

Links:

* Kijai's [conversion](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/MoCha) to fp8 e4m3
* [Article](https://orange-3dv-team.github.io/MoCha/)
* only [ckpt](https://huggingface.co/Orange-3DV-Team/MoCha/tree/main/preview) file available from the authors which is believed to be bf16
* Kijai's 1st sample workflow: [wanvideo_mocha_replacement_original_01](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_mocha_replacement_original_01.json)
* Kijai's 2nd sample workflow: [wanvideo_MoCha_replace_subject_KJ_02](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo_MoCha_replace_subject_KJ_02.json)

> Identity preserved not as strongly as VACE 2.1 / Wan Animate but the lighting is super impressive

2024.10.21 a node has been added to code has been added to latest version of [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
to support generating videos with MoCha. Code has been added as well to support [WanVideo Context Options](what-plugs-where/context-options.md) with MoCha.

> a big downside of MoCha it's basically double compute; the original frames are concatenated along temporal dimension;
> the frame count is basically doubled; so memory use for 81 frames would be similar to 161 frames

> Mocha does better with prompt; you can get by with generic, but the more detailed the better, particularly with character likeness

## Steady Dancer

Nov-2025 single .safetensors model derived from Wan family of video generation models.
Does not work with other Wan models, not a LoRa.
Performs functions roughly similar to WanAnimate.
Works with context windows.
Support has been integrated into ComfyUI native, likely to the wrapper as well.

- fp8 .safetensors: [HF:Kijai/WanVideo_comfy_fp8_scaled:SteadyDancer](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/SteadyDancer)
- fp16 .safetensors: [HF:Kijai/WanVideo_comfy:SteadyDancer](https://huggingface.co/Kijai/WanVideo_comfy/tree/main/SteadyDancer)
- original article: [GH:MCG-NJU/SteadyDancer](https://github.com/MCG-NJU/SteadyDancer) 

> UniAnimate delivers similar results if not better

> used it with lightx2v and it works
