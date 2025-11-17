# Wan I2V Tricks

In Nov 2025 community started exploring hidden potential behind Wan 2.2 I2V models.
This page collects insights into non-obvious workflows.

## PainterI2V

`princepainter/PainterI2V` node attracted attention and sparked research. It exists into two versions
- [Native](https://github.com/princepainter/ComfyUI-PainterI2V)
- [Wrapper](https://github.com/princepainter/ComfyUI-PainterI2VforKJ)

The node was created to inject more motion into I2V generations with speed LoRa-s.
It works by preparing noise latents in a special manner.

Here are some quotes about it: "It's pre-scaling the input latents"; "it tries to balance out the brightness increase you normally get when scaling the input like that"; "basically adding some of the input image to what's normally gray in I2V input"; "I think the logic behind using the reference partially in those frames is to keep the color from changing"; "this is what it does to input image: invert and blend to gray" (input latents); "definitely changes something" - "thing is it's randomness, if you added noise controllably then you could also make a slider that changes the output"

## PainterLongVideo

[princepainter/ComfyUI-PainterLongVideo](https://github.com/princepainter/ComfyUI-PainterLongVideo) from that same authrow is being played with - and nice long videos are being posted.

## TimeToMove

Insipired by [time-to-move/TTM](https://github.com/time-to-move/TTM), a promising body of code for converting rough mock-ups into smooth AI videos
which re-juvenates an old approach which existed as early as CogVideoX days Kijai added 
`WanVideo Add TTMLatents` node now in [kijai/ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
and provided an [example wf](https://github.com/kijai/ComfyUI-WanVideoWrapper/blob/main/example_workflows/wanvideo2_2_I2V_A14B_TimeToMove_example.json)
  
Mixed results reported in testing. [Official tool](https://github.com/time-to-move/TTM/tree/main/GUIs) is used to generate driving video.
Mockups use character pictures with a white outline around them.
Low noise step is somehow more problematic.
Removing Lightx2V on low seems to help.