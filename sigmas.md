# Sigmas

## Intro

[What the hell is a sigma schedule?!](https://www.youtube.com/watch?v=egn5dKPdlCk)

## Nodes For Working With Sigmas In Kijai's Wrapper

`WanVideo Sigma To Step` if you supply a floating point value like 0.9 you can plug this into `end_step` input of `WanVideo Scheduler` and it will be treated as sigma, not step.

```
WanVideo Sigma To Step
      |
      v
WanVideo Scheduler
      |
      v 
Preview Any
```

## Native Nodes For Working With Sigmas

* Basic Scheduler
* Sigmas Split Value
* Custom Sampler Advanced

Other nodes you will likely see in the same workflow are

* ModelSamplingSD3 - change shift
* KSamplerSelect
* CFGGuider - split out inputs for Custom Sampler Advanced: model, positive, negative, cfg
* RandomNoise - noise input for 1st WAN 2.2 sampler
* DisableNoise - noise input for 2nd WAN 2.2 sampler

## Wan 2.2 Switchover

Advice on switching from hight noise to low noise model with WAN 2.2

| Model Type | Switchover Sigma |
| :--- | :--- |
| I2V | 0.9 |
| T2V | 0.875 |

## Alternative Tools

`Get Sigma` from [BlenderNeko/ComfyUI_Noise](https://github.com/BlenderNeko/ComfyUI_Noise)