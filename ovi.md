# OVI

Ovi is an open-source model capable of sound + video generation. Video quality at 5B level. 24fps. Requires 24Gb VRAM to run in 8fp and 32Gb VRAM to run in 16fp.

Githubs:
* [ComfyUI_RH_Ovi](https://github.com/HM-RunningHub/ComfyUI_RH_Ovi)
* [ComfyUI-Ovi](https://github.com/snicolast/ComfyUI-Ovi)

## Kijai's Support For Ovi

As of 08 Oct 2025 please use Ovi branch in the repository. Wiring:

| Pre Embeds Node| Pre Embeds Inputs -> Output | Embeds Node | Input from Pre / Embeds Inputs -> Output | Model | WanVideo Sampler Input |
| :-- | :-- | :-- | :-- | :-- | :-- |
| - | - | - | Kijai: "5B is different as it puts the image in the noise latent"; Ovi based on WAN 5B, so.. | - | - |
| WanVideo Encode | image, mask<br>-> samples | WanVideo Empty Embeds | **extra_latents** / width, height, number_of_frames<br>-> image_embeds | Ovi | image_embeds |
| ... | ... | WanVideo Add Extra Latent | embeds, latent_index = 0<br>"can be end image too technically" | Ovi | - |
| - | - | WanVideo Empty MMAudio Latents | length -> samples | Ovi | samples |

Extra nodes: `Ovi MMAudio Loader`, `WanVideo Decode Ovi Audio`, `WanVideo Ovi CFG` - adds negative prompt for audio.
`WanVideo EasyCache`.

Put MMAudio VAE model weights into either `vae` or `mmaudio` folder.