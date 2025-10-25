# LongCat

Doordash released 14B parameters video AI model called LongCat,
[teaser](https://huggingface.co/meituan-longcat/LongCat-Video).

MIT license, hurrah!

Example code does 832x480x93.

> model structure is similar to Wan, just everything named differently, and has fused qkv;
> 48 blocks, smaller dim (4096);
> text encoding, VAE etc. are same;
> it's not a Wan model

"First, the model generates a 480p, 15 fps video; second, this video is upscaled to 720p, 30f ps using trilinear interpolation and refined by a refinement expert"

> refinement expert = lora, by the looks of it...  
> Cinescale style

> And what's amazing is that this Meituan is a food delivery platform.

An attempt to run in ComfyUI in wrapper, does not yet follow the prompt:

![longcat-1st-try-wrapper](screenshots/longcat-1st-try-wrapper.webp)

> one model for T2V + I2V and continuations (similar to [SVI](svi.md)) seems really exciting

> everything would have to be trained, so not that easy to replace Wan: there's no VACE, audio models, controlnets etc. etc.

> it generates 6 second pieces in either t2v, i2v, or multi-frame i2v mode;
> I tried to generate a 12 second video in one go and it had the same repeating issue as wan

> the multi frame i2v allows extension with motion continuity;
> those 11 frames are the only context it has for the next segment;
> if your character isnt perfectly in the shot at the boundary, rip