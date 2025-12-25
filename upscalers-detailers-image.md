# Image Upscalers and Detailers

This page is a work in progress

## Simplest: Upscale Image By

Use stock ComfyUI node `Upscale Image By` with `upscale_method`=`lanczoc`

## Detailer (SEGS)

There are two Github repositories to get nodes from

- [GH:ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) the orginal main repository
- [GH:drozbay/ComfyUI-Impact-Pack](https://github.com/drozbay/ComfyUI-Impact-Pack) a copy by [Drozbay](hidden-knowledge.md#drozbay)
  which is also used in his created by not very widely known
  SEGS/VACE video [detailer](upscalers-detailers-video.md#drozbays-impact-pack-segs-detailer-for-wan-video-and-vace)

## USDU

Ultimate SD Upascaler, a popular choice.
Interestingly includes a node `Ultimate SD Upscale (No Upscale)` which is used to fix artifacts.

[GH:ssitu/ComfyUI_UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)

## SeedVR2

[GH:numz/ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) useful for both images and videos

## Chatter

> In my tests, z image doesn't work well for second pass. Instead, I'm using wan 2.2; you can also use flux

## For ZIT

- [GH:wildminder/ComfyUI-DyPE](https://github.com/wildminder/ComfyUI-DyPE) "ok I give up on DyPE 4096, but going to keep using dype 2048, it's just barely manageable" - overall negative sentiment like "I still can't fix the stupid dype long body problem"
- [GH:spacepxl/ComfyUI-VAE-Utils](https://github.com/spacepxl/ComfyUI-VAE-Utils)
- [blend-masked-noise](workflows/kibito-blend-masked-noise.webp) wf which allows exclusing skip from noise blend to prevent "zombie skin" while adding details
- [combined ZIT upscaling](../workflows/z-image/l23-combined-upscale.json) "When the image is blurry, I use qwen edit to recover details: input > qwen edit >  seedvr > zit";
  "Upscale the image to a higher resolution, reduce compression artifacts, noise, and blur while preserving original details and colors. Do not change content, pose, face, body, age, gender, clothing, background, or camera angle";
  "do you do any sort of tiling? zIT can't really do more than 2.5MP without tiling? yes USDU";
  "seedvr2 first then usdu? I do the reverse lol, cause seedvr2 adds microdetails";
  "I do it this way because seedvr sometimes generate too much noise. and a second pass to reduce this noise"

## Hmm

What is Supir x3? TTP?