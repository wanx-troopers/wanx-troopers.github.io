# Infinite Talk

This section is incomplete.

## 2026

Stef:
> I have used Infinite a lot and there is no solution against this beside masking, which sucks because it WILL let traces unless your character's head moves only slightly and there is no zooming/panning. Infinite is so good in v2v for lipsync but it changes details of the source vidéo, especially if the camera moves/zooms/pans. Mask when you cannot do otherwise, and play around with Grow Mask With Blur or how the node is called, sorry I just woke up. If you have several characters, don't forget Infinite will go from left to right. And if only one character is speaking, you'll have to feed the other with an empty audio track, though I got often issues if I just used a generated silence in Audacity. I solved the issues with free soundfiles of people breathing quietly which work wonder as 'silence', you can make them even quieter with Audacity. Also, if using several sound files they must not only have the same length but also the same amount of samples, you can check in Mediainfo how many samples an audio file has (check advanced parameters to display those). If the sample count doesn't match, infamous kwarg error in comfy console. And another thing : If you mask, because you have no other option (see masking as last option because it sucks), make sure the audio file isn't 1 ms longer than the video file or again kwarg error (because Infinite will look for masks which don't exist). Last but not least, Wan2.1 loras work with infinite both in i2v and v2v mode, though they sometimes give funny unexpected results, especially in i2v mode when they fight with Infinite for hand movements (if your lora is a movement or pose lora e.g.).

> in i2v Infinite is perfect of course, masking won't let traces because there is no source video. But in v2v masking in Infinite is just meh unless I missed something

> in v2v without masking, Infinite works very well if you accept the details it WILL change in your source video of course, you don't even need to add masks, you just provide audio files from left character to right character audio1, audio2 etc
> but the changes can be dramatic, as said, especially when the camera moves

> To my knowledge, there is no open source perfect v2v lipsync solution yet, Infinite is still the second rank optimum  
> It's a quote of Pareto, means 'best possible under current conditions'

> unfortunately it will change other things than your character's expressions, it is because Wan2.1 reencodes the video - if the camera moves it can hallucinate things which were not in your source video 

## 2025.01.22

InfiniteTalk support has been added to ComfyUI native. Sample wf: [infinitetalk_multi_test_native](workflows/kj_infinitetalk_multi_test_native.json)

## Models

Infinite Talk workflows utilize regular Wan I2V safetensors file with regular speed lora of your choice.

They additionally use a "InfiniteTalk Model" such as `Wan_2_1-InfiniteTalk-Multi_fp16.safetensors`. It is loaded by `WanVideo Long I2V Multi/InfiniteTalk` which similar to VACE plugs into `VanVideo Model Loader`.

`clip_vision_h` and `wav2vec` .safetensors files are loaded as well.

Can do start image + audio to video as well as start video + audio to video. Can use up to 4 audio tracks and masks to show which character is associated with which file.

## Nodes

|Name In Code (sometimes easier to understand)|Name on Screen|
|:---|:---|
|MultiTalkModelLoader|Multi/InfiniteTalk Model Loader|
|MultiTalkWav2VecEmbeds|Multi/InfiniteTalk Wav2vec2 Embeds|
|WanVideoImageToVideoMultiTalk|WanVideo Long I2V Multi/InfiniteTalk|
|Wav2VecModelLoader|Wav2vec2 Model Loader|
|MultiTalkSilentEmbeds|MultiTalk Silent Embeds|

## What Plugs Where

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
|`WanVideo ClipVision Encode`|`image_1`, `image_2` -> `image_embeds`| `WanVideo Long I2V Multi/InfiniteTalk` | `clip_embeds` / `start_image` -> `image_embeds` | Wan I2V family | `image_embeds` |
| - | - | `Multi/InfiniteTalk Wav2vec2 Embeds` | `wav2vec_model`, `audio_1`, .. 4, `ref_target_masks` -> `multitalk_embeds` | Wan I2V family | `multitalk_embeds` |


### Note

| Node | Setting | Meaning |
| :--- | :--- | :--- |
| `WanVideo Long I2V Multi/InfiniteTalk` | `frame_window_size` | how many frames are processed at once, leave at default |
| `Multi/InfiniteTalk Wav2vec2 Embeds` | `num_frames` | total number of frames in the video |


`WanVideo Context Option` is *not* compatible with `Infinite Talk`.

## QnA

> Q: is it possible to do v2v with infinitetalk and only inpaining the head? my videos get changed too much  
> A: yeah, you can use a mask
