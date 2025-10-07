# Sigmas

## Intro

[What the hell is a sigma schedule?!](https://www.youtube.com/watch?v=egn5dKPdlCk)

## Useful Nodes

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

## Wan 2.2 Switchover

Advice on switching from hight noise to low noise model with WAN 2.2

| Model Type | Switchover Sigma |
| :--- | :--- |
| I2V | 0.9 |
| T2V | 0.875 |

## Alternative Tools

`Get Sigma` from [BlenderNeko/ComfyUI_Noise](https://github.com/BlenderNeko/ComfyUI_Noise)