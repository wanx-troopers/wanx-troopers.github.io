# What Plugs Where

A big table analysing workflows available online to take note of which embeds node can be used with which model (.safetensors).

## Native KSampler

* `2.2 Fun VACE` (high/low) loaded by Kijai's `Diffusion Model Selector` nodes
* `Wan 2.2 T2V` (high/low) loaded by Kiaji's `Diffusion Model Loader KJ` nodes
* speed loras loaded by `Lora Loader Model Only`
* `2.2 Fun Vace` plugged as `extra_state_dict` into `Diffusion Model Loader KJ` nodes

| Embeds Node | Inputs | Model | Bonuses |
| :-- | :-- | :-- | :-- |
| WanVaceToVideo | control_video, masks, ref_image, pos/neg | VACE + Wan | trim_latent from WanVaceToVideo to TrimLatentNode |

Bonus nodes: Create Video, Save Video, Points Editor, (Down)Load SAM2Model, Sam2Segmentation, GrowMask, Preview Animation, Empty Image (color 8421504), ImageComposeMask.

Not entirely clear if inpainted area needs to be gray-ed out in `control video` input to `WanVaceToVideo`

## Kijai's Wrapper

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
| - | - | WanVideo VACE Encode | / input_frames, input_masks, ref_images<br>-> vace_embeds | VACE + Wan T2V family | image_embeds |
| - | - | WanVideo ImageToVideo Encode | / start_image, end_image, control_embeds?, temporal_mask?, extra_latents?, add_cond_latents?<br>-> image_embeds | Wan I2V family | image_embeds |

Note: ? denotes parts which are not clear enough.

## WanVideo VACE Start To End Frame

* inputs: `start_image`, `end_image`, `num_frames` and, confusingly, `control_images` and `inpaint_mask`
* outputs: `images`, `masks`

Can be used to prepare `input_frames` for `WanVideo VACE Encode`.

## Notes on Using VACE (2.1 and 2.2 Fun)

```
WanVideo VACE Start To End Frame --------------------> | Replace Images  |
                                                       | In Batch        | --> Preview Image,
LoadImage  ---> ResizeImage ---> RepeatImageBatch ---> |                 |     WanVideo VACE Encode --> ..
                                                       |                 |
SolidMask  ---> RepeatMask --------------------------> |                 |
```

## Ovi

In [Ovi](ovi.md) section.
