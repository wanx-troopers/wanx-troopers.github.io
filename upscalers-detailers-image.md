# Image Upscalers and Detailers

This page is a work in progress

## Simplest: Upscale Image By

Use stock ComfyUI node `Upscale Image By` with `upscale_method`=`lanczoc`

## USDU

Ultimate SD Upascaler, a popular choice.

[GH:ssitu/ComfyUI_UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)

## Detailer (SEGS)

There are two Github repositories to get nodes from

- [GH:ltdrdata/ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) the orginal main repository
- [GH:drozbay/ComfyUI-Impact-Pack](https://github.com/drozbay/ComfyUI-Impact-Pack) a copy by [Drozbay](hidden-knowledge.md#drozbay)
  which is also used in his created by not very widely known
  SEGS/VACE video [detailer](upscalers-detailers-video.md#drozbays-impact-pack-segs-detailer-for-wan-video-and-vace)

## Chatter

> In my tests, z image doesn't work well for second pass. Instead, I'm using wan 2.2; you can also use flux

## For ZIT

- [GH:wildminder/ComfyUI-DyPE](https://github.com/wildminder/ComfyUI-DyPE) "ok I give up on DyPE 4096, but going to keep using dype 2048, it's just barely manageable"
- [GH:spacepxl/ComfyUI-VAE-Utils](https://github.com/spacepxl/ComfyUI-VAE-Utils)
- [blend-masked-noise](workflows/kibito-blend-masked-noise.webp) wf which allows exclusing skip from noise blend to prevent "zombie skin" while adding details
