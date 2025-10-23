# Phantom And MAGREF

This section is a incomplete. 
Phantom and MAGREF are relatively old finetunes based on Wan 2.1, so called "reference" models.

|Model|Type|Notes|
|:---|:---|:---|
|Phantom|T2V|Could theoretically work with VACE, also exists as T2V LoRA|
|MAGREF|I2V|-|

# Phantom

It has been shown that Phantom generation is a somewhat influenced by [Lynx](lynx.md).

# MAGREF

> with MAGREF you can sort of adjust the strength by padding your image with white;
> so for example put your full image without any padding as main image, then a version of that with padding to this and it sticks to it less

> Q: how do u use magref?  
> A: Exactly like normal I2V, except you either remove background or pad the input with white  
> Q: any recommended sampler to test against it? to see realism, because when I use more steps in dpm++_sde
> can end up with a burned image, over coocked one?  phantom-magref.md  
> A: With distil Loras, try lcm instead for less burn

Can be used with [WanVideo Context Options](what-plugs-where/context-options.md).
