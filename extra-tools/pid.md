# PiD

Versions of image models started emerging that support direct generation to pixel space without a VAE.
[hidream](hidream.md) seems to have been the 1st. PiD version of [ZIT](z-image.md) is known as L2P, 
AsymFLUX.2 is the flux flavor.

Nvidia released its own [PixelDiT-1300M-1024px](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)
text to image model and also [PiD](https://huggingface.co/nvidia/PiD), pixel decoder, which has versions replacing
flux2 and sd3 vae-s. Support for NVidia models has been [added](https://github.com/Comfy-Org/ComfyUI/pull/14103) to ComfyUI native.

BNP4535353 on PiD:
> it directly enlarges the original small image into a very large one and forcibly applies a lot of sharpening, which is uncontrollable

David Snow:
> yeah. now that I test it more, there are some serious issues. my current method of using SDXL controlnet union tile is much better.

huddadudd:
> my go to is still magnific

INT8 versions: [HF:tsolful/PixelDiT_INT8:diffusion_models](https://huggingface.co/tsolful/PixelDiT_INT8/tree/main/diffusion_models)
require [GH:BobJohnson24/ComfyUI-INT8-Fast](https://github.com/BobJohnson24/ComfyUI-INT8-Fast) node to load.

wf: [buggz-ZturbotoPiDv2](../workflows/z-image/buggz-ZturbotoPiDv2.json)