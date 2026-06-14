# Cross Image Models

[GH:BigStationW/ComfyUi-Untwisting-RoPE](https://github.com/BigStationW/ComfyUi-Untwisting-RoPE)
style transfer

[GH:shootthesound/ComfyUI-Angelo](https://github.com/shootthesound/ComfyUI-Angelo)
> A click-to-refine sampler for ComfyUI. Generate an image, then click or paint on regions you want improved. Each click refines
just that area while the rest stays bit-exact. One node replaces the standard KSampler + post-processing chain. Works with FLUX 2
Klein 9B and Qwen-Image-Edit as first-class edit models - plus any other sampler-compatible model (FLUX 1, SDXL, SD 1.5).

> So, Qwen can process that json style prompt?  

ramonguthrie:

> Yes Qwen, so can Ernie, Flux 2.0, but not to the level of ideogram of course  ...Z-Image does need a lot of tweaking to work  
> Z-Image isn't that great with json, even Flux.1 Kontext is better than Z-Image


huddadudd:

> One of the biggest discoveries from the community is that Z-Image-Turbo performs significantly better on structured or JSON-style
> prompts than on natural language. Because Qwen3 is highly attuned to structured layouts (like Markdown and JSON),
> formatting your prompt this way drastically improves composition, layout control, and prompt adherence.
> Recommended JSON Template:  
> {  
>   render_type: A high-fidelity fashion editorial photograph.,  
>   subject: An East Asian female model.,  
>   face: Neutral expression, focused gaze, soft makeup.,  
>   hair: Sleek black hair parted down the middle.,  
>   outfit: An off-white knitted crop top and high-waisted linen trousers.,  
>   environment: Standing on a wet pavement in Tokyo at night, neon signs reflecting in rain puddles.,  
>   lighting: Stark, dramatic neon rim lighting casting soft shadows.,  
>   mood_and_style: Moody, cinematic, high-fashion aesthetic.  
> }  
> i thought ZIT handled .json well  
> havent tried it though so could just be bs

patientx:
> these definetly work with anima at least to some degree, even though it is using just a 06b qwen

ramonguthrie:
> Yes just having a structure prompt like this works with every model, even SDXL  
> "" or ' ' in a prompt might target on some seeds, to create text, when you don't want it to!

Therefore advice seems to be to use a "broken" json without quotes
