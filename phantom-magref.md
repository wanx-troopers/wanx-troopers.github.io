# Phantom And MAGREF

This section is a incomplete. 
Phantom and MAGREF are relatively old finetunes based on Wan 2.1, so called "reference" models.

|Model|Type|Notes|
|:---|:---|:---|
|Phantom|T2V|Could theoretically work with VACE, also exists as T2V LoRA|
|MAGREF|I2V|-|

# Phantom

> Phantom can take 4 inputs;
> Phantom [likely] tries to use 1 reference per subject

> If you're using the HN/LN split, keep in mind that Phantom will only work with the LN part,
> so you have to either skip the HN stage totally (which is perfectly fine to do),
> or you have to make the HN stage output look close enough to your target references
> that Phantom can pick up where it left off and finish the details properly

It has been shown that Phantom generation is a somewhat influenced by [Lynx](lynx.md).

# MAGREF

> with MAGREF you can sort of adjust the strength by padding your image with white;
> so for example put your full image without any padding as main image, then a version of that with padding to this and it sticks to it less

> Q: how do u use magref?  
> A: Exactly like normal I2V, except you either remove background or pad the input with white  
> Q: any recommended sampler to test against it? to see realism, because when I use more steps in dpm++_sde
> can end up with a burned image, over coocked one?  phantom-magref.md  
> A: With distil Loras, try lcm instead for less burn

Can be used with [Context Windows](what-plugs-where/context-windows.md).
