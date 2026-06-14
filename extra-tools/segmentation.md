# Segmentation

## Sam3

Kijai: "I'm just about to finish native SAM 3.1 support"

Community is experimenting with SAM3 model from Facebook. The model provides several capabilities

- segmentation
- depth maps

Sam3D praised as new in segmentation models.

Several ComfyUI implementations:

- "we have that in core too"
- [GH:Ltamann/ComfyUI-TBG-SAM3](https://github.com/Ltamann/ComfyUI-TBG-SAM3)
- [GH:PozzettiAndrea/ComfyUI-SAM3](https://github.com/PozzettiAndrea/ComfyUI-SAM3)
- [GH:PozzettiAndrea/ComfyUI-SAM3DBody](https://github.com/PozzettiAndrea/ComfyUI-SAM3DBody) "They don't release VRAM quite as well as you'd expect. They work, but lack optimization"

Sentiment: "crazy", "Sec4B still doing better"

- David Show's workflow for Sam3 masking: [ds-sam3d-Mask-Generator-multi](../workflows/ds-sam3d-Mask-Generator-multi.json)

> SAM2 can arguably be better with points;
> 3 (and 3.1) is all about the text prompting and video tracking

## LocateAnything

[GH:alisson-anjos/ComfyUI-LocateAnything](https://github.com/alisson-anjos/ComfyUI-LocateAnything)
based on [research.nvidia.com/labs/lpr/locate-anything](https://research.nvidia.com/labs/lpr/locate-anything/)

## Depth Anything

> Anyone know why depthanything V3 looks like unadulterated garbage compared to V2?

## Sam3.1 And Sam3D

Preview of future nodes to come utilizing Sam3.1 for segmentation and Sam3D for mesh reconstruction: [sam3d-wip](screenshots/nodes/sam3d-wip.webp); sam3d-object.

> sam3d-object ... it will be able to do whole scene too and then sam3d-body plugs into the scene

> Q: it does do fingers tho?  
> A: sam3d does, but kimodo doesn't; sam3d can even do ASL [American Sign Language], it's really good;
> ... did even add HAMER to refine the hands, but I'm not sure it's ... necessary anymore

`Sam3 Native Model Loader` node has been spotted in the wild.

`SAM3 Video Track Node`, `SAM3 Tracks to Mask`, `SAM3 Trackes Preview`, `SAM3 Detect`

Sam3 masking wf from djbfilmz: ![sam3-masking](workflows/sam3-masking.webp)

> cant we use sam 3 insted of sam 3.1?  
> why? they perform about the same, 3.1 better with multiple people

`people:2` may be required to segment out two characters
