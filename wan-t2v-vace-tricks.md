# Wan I2V T2V / VACE Tricks

Note: [What Plugs Where](what-plugs-where/what-plugs-where.md) page contains some information on how native and wrapper workflows for VACE are constructed.
This page contains additional/advanced examples.

[drozbay](hidden-knowledge.md#drozbay) has shared the following advanced VACE workflows relying on his
[ComfyUI-WanVaceAdvanced](https://github.com/drozbay/ComfyUI-WanVaceAdvanced) node pack, with ClownShark and VACE:

- [Dancer](screenshots/drozbay_vacedancer_v1.png) - `DWPose Estimator` and `Depth Anything V2` as 2 separate VACE control videos
- [Falling Into The Water](workflows/droz_vace_reference_and_canny_v1.png) - `Canny Edge` limited by depth masking: "keep the outlines, ... don't ... details inside the objects"

Note: `WanVacePhantomDualV2` from `WanVaceAdvanced` is compatible with Phantom but not linked to it otherwise.
`vace_reference` and `phantom_images` on this node are fundamentally different: "they go to different model layers and they are treated differently".

> vace is still pretty iffy when trying to use the reference input for style
> it's not a style-transfer model, even if it occasionally does work
> the reference is really for either background, setting, or subject(s)

> it will not be great for character unless your character reference is pretty much exactly where the character will be in the first frame. In that case I recommend you use Phantom

> and don't use the skeleton+depth mix; send in the depth and the skeleton into separate Vace control inputs;
> either chain WanVaceToVideo nodes, or use WanVacePhantomDualV2 node

> Q: load FUN VACE module for High Model first, and then VACE 2.1 for the LOW model?
> A: sometimes

> can try WAN 2.1 + [Wan 2.1 to Wan 2.2 LOW LoRA](loras/part-01.md#Special Use) + VACE 2.1 on LOW  
> original Vace was pretty weak with pose control

## See Also

- [Native Context Windows PR](what-plugs-where/context-options.md#native-context-windows-pr)
- [Video Blending From Fragments](extra-tools.md#video-blending-from-fragments)
