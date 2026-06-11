# Bernini

ByteDance released open weights for Bernini edit model based on Wan 2.2.
Has high and low noise weights exactly like Wan 2.2.

Original sources [bernini-ai.github.io](https://bernini-ai.github.io/),
[HF:ByteDance/Bernini](https://huggingface.co/ByteDance/Bernini/tree/main)

- [HF:Kijai/WanVideo_comfy_fp8_scaled/tree/main/Bernini](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/Bernini);
- early wf: [bernini_testing_01](workflows/wan/kj-bernini_testing_01.json)
- wf: [lucifer-Bernini_testing_video_edit_with reference](workflows/bernini/lucifer-Bernini_testing_video_edit_with reference.json)

Change merged to main in ComfyUI.
Use `Bernini Conditioning` node.

> when you edit a video, the WHOLE video is added to the sequence the model processes
> that doubles the compute needed
> so it's 2x slower than normal Wan22

> Q: 4K?  
> A: it would be impossible anyway as this is trained at 720p

> if it wasn't so slowwwwwwwwwwww
> need to make mxfp8 and use my 5090

> 144 frames at 24fps

mxfp8 Bernini:
[HF:Kijai/WanVideo_comfy_fp8_scaled:Bernini/Wan22_Bernini_HIGH_mxfp8](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Bernini/Wan22_Bernini_HIGH_mxfp8.safetensors)
[HF:Kijai/WanVideo_comfy_fp8_scaled/blob/main/Bernini/Wan22_Bernini_LOW_mxfp8](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/Bernini/Wan22_Bernini_LOW_mxfp8.safetensors)

Recommended:
![kj-wan-mem-effective-sage](screenshots/nodes/kj-wan-mem-effective-sage.webp)


JohnDopamine: [GH:CCpt5/ComfyUI-BerniniStudio](https://github.com/CCpt5/ComfyUI-BerniniStudio)
> AIO Bernini + Ollama + Prompt preset node  
> "replace the X with the Y from image0, image1, and image2"

slmonker:
> multi-angle ref image is working  
> high noise+lightx2v(strength=1) +low noise +lightx2v(wan2.1 t2v version ),3steps+3steps,high noise part cfg=1.5  
> 4+4, `Patch Sage Attention KJ` wf: [slmonker-bernini-studio](workflows/bernini/slmonker-bernini-studio.json)

Apparently Bernini has pure I2V capabilities as well, up to 161 frames

> You are a helpful assistant specialized in image-to-video generation. Anime girl is dancing with a red panda, the camera zooms out displaying the dance floor. The panda jumps to the floor.

![bernini-prompts](screenshots/bernini/bernini-prompts.webp)

| task_type | system prompt (prepended to T5 text) |
|---|---|
| `default` | You are a helpful assistant. |
| `t2i` | You are a helpful assistant specialized in text-to-image generation. |
| `t2v` | You are a helpful assistant specialized in text-to-video generation. |
| `i2i` | You are a helpful assistant specialized in image editing. |
| `r2i` | You are a helpful assistant specialized in subject-to-image generation. |
| `i2v` | You are a helpful assistant specialized in image-to-video generation. |
| `v2v` | You are a helpful assistant specialized in video editing. |
| `r2v` | You are a helpful assistant specialized in subject-to-video generation. |
| `vi2v` | You are a helpful assistant specialized in video editing on content propagation. |
| `rv2v` | You are a helpful assistant specialized in video editing with reference. |
| `ads2v` | You are a helpful assistant specialized in ads insertion. |
| `vrc2v` | You are a helpful assistant for editing. You may need to adjust the subject's action or position. |
| `mv2v` | You are a helpful assistant for editing. You might need to adjust the video's style, lighting, colors, textures, and the subject's pose or action. |

![bernini-conditioning](screenshots/bernini/bernini-conditioning.webp)

> the reference can be larger than the gen even since it's added as tokens anyway

> their code only used 5 so wasn't sure how many it can take, I think I capped it at 8 but technically there wouldn't be any cap

LDWorks David:
> seems like with one sheet ref also works [several images on white background as one image]

Stef:
> Wan2.2 loras seem to work with Bernini  
> I use Bernini mostly for v2v + reference images  

> Bernini and first frame/last frame ... I could manage to do a FFLF by prompting.
> Describe the starting image and mention it is "image0", describe the action and
> how the final image looks like and mention it is "image1". Exemple of prompt:
> "A soldier looking at a woman in image0 walks backwards, keeping eyes locked with
> the woman and looking angry, and sits on the tree hunk behind him in image1.
> The woman keeps her face turned towards the soldier." And indeed, the first frame
> of the clip is my image0 and the last frame of the clip is my image1
                                             
Qwen3.6 35b was tested in ollama

slmonker: [GH:AIMixer/ComfyUI-Bernini](https://github.com/AIMixer/ComfyUI-Bernini/tree/main) - all in Chinese? based on kj's wanvideowarpper "but why? core is so much faster"

> is bernini lora possible or nah cause it has a new layer or something ?  
> it has no new layers

## 190Gb Model

Funnily enough it seems fully over 190Gb FP32 Bernini weights have been made public on [HF:ByteDance/Bernini-Diffusers:bernini](https://huggingface.co/ByteDance/Bernini-Diffusers/tree/main/bernini).
"it's 7B qwen VL 2.5 + Wan 2.2 in fp32"

> hmm the planner is looking better;
> it is not prompt enchancer, there's projector that projects it's output to the T5 size
> so potentially it replaces/modifies T5 embeds

> the qwenVL seems finetuned a bit... not sure how important that is, could maybe just make a lora
