# PiD

Versions of image models started emerging that support direct generation to pixel space without a VAE.
[hidream](hidream.md) seems to have been the 1st. PiD version of [ZIT](z-image.md) is known as L2P, 
AsymFLUX.2 is the flux flavor.

Nvidia released its own [PixelDiT-1300M-1024px](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)
text to image model and also [PiD](https://huggingface.co/nvidia/PiD), pixel decoder, which has versions replacing
flux2 and sd3 vae-s. Support for NVidia models has been [added](https://github.com/Comfy-Org/ComfyUI/pull/14103) to ComfyUI native.