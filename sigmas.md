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