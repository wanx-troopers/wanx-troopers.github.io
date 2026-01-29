# Infinite Talk

This section is incomplete.

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
