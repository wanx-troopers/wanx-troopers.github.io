# Discussions Around Out Of Memory

2025.12.10

![dc-unload-models-execution-cache](screenshots/dc-unload-models-execution-cache.webp)  
helps free up RAM

SAM3 nodes under suspicion for consuming RAM

2025.12.06

> fun fact, using native load video is actually worse, because it reruns the get video components node each time, which also leaks memory
> vhs at least doesn't have that problem

About notive `Upscale Image` leaking RAM (not VRAM) with pytorch 2.8:

> updating to pytorch 2.9.1+cu130 fixed [it]

Another artist:

> apparently torch 2.9.1 cu130 was the solution

No memory leak on CUDA 12.8 either
