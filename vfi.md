# Frame Interpolation

Frame Interpolators increase FPS.
Wan 14B models normally produce video that feels natural when played at 16fps.

One idea is to 2x number of frames arriving at a video that should have been played at 32fps but can probably play well at 29 or 30 too.
Another idea is to 3x number of frames arriving at a video that should be played at 48fps but play it at 50fps.
And then possibly 1/2 number of frames arriving at video that plays at 24fps, but could probably be played at 25fps too.

Once you have generated the number of frames you want you are free to package them up into an .mp4 labelled with whatever playback speed you like.

VFI = video frame interpolation.

## RIFE

RIFE VFI still good to double frame rate.

A popular node pack implementing RIFE: [GH:Fannovel16/ComfyUI-Frame-Interpolation](https://github.com/Fannovel16/ComfyUI-Frame-Interpolation).

Occasionally this alternative nodepack requirint `tensorrt` installation is mentioned: [GH:yuvraj108c/ComfyUI-Rife-Tensorrt](https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt).

## FILM

Popular implementation: `FL RIFE Frame Interpolation` from [GH:filliptm/ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes).

> Film - it's an alternative to RIFE?
> yeah exactly, its by google
> its really old actually, like 10 years old =p
> but its really good

> FILM so far never gave me any of the ghosting RIFE did or the artifact GIMM did, and it's fast enough (only in Fill's pack) and otherwise good enough

## GIMM

Kijai's Github contains [ComfyUI-GIMM-VFI](https://github.com/kijai/ComfyUI-GIMM-VFI).
