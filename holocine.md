# HoloCine

Warning: non-commercial license (though it is possible initial release was under ASF license, not certain).

[Holo Cine](https://holo-cine.github.io/) models have been uploaded to Huggingface, Kijai's provided fp8 [conversion](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/tree/main/T2V/HoloCine).

There is no special code yet in ComfyUI to use them properly even though ppl tried to drop the .safetensor files into T2V workflows to see what happens.
The hope/promise is to generate longer videos with consistent characters; in practice generated videos are still quite short but longer than 5 seconds.

> just using the weight at 253fr on low reso (480*480);
> disabling nag to use the | between each shot (no context windows);
> keep same formating than in paper /demo

> no idea for native [e.g. experiments are in wrapper workflows]

![holocine-prompts.webp](screenshots/holocine-prompts.webp)

Models are uploaded as "sparse" and "full", the article says:
> The sparse model is a computationally efficient approximation of the full model, maintaining
> almost the same visual and narrative quality while enabling long, coherent cinematic video generation.

Note: 2025-Oct-24 the authors updated slightly tweaked models which are supposed to be better, among them film-opt.