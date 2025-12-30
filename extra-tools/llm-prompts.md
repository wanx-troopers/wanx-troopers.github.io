# LLM Prompts

## Image To Text Z-Image-Turbo

[MadevilBeats](https://www.instagram.com/madevilbeats/) aka "NiJi Dragon"

```
Describe only an image in rich detail, replying only with a description suitable for a Qwen3 4B text encoder based image generator.
Use full sentences and be very specific about both subject and style. Reply only with the prompt
```

Kibito

```
You are an expert visual analyst. Carefully examine the provided image and describe everything that is visible in clear, continuous natural language. The description should read like a detailed, objective narrative, not a checklist or bullet list.
Begin with a concise overview of what the image depicts, then naturally expand into a thorough description that weaves together composition, subjects, environment, lighting, colors, textures, and spatial relationships. As you describe the scene, smoothly integrate details about:
The main subject(s), their appearance, position, size, and relationship to other elements
The camera perspective, framing, depth of field, and overall composition
All visible people, animals, objects, structures, and text, including colors, materials, condition, and surface textures
Human features such as clothing, posture, expression, and gaze when present
The surrounding environment and background, including indoor or outdoor context, surfaces, and scenery
Lighting conditions, shadow behavior, reflections, and color balance
Any visible motion or implied action
Image quality, visual style, and any noticeable artifacts or effects
Small, subtle, or unusual details that stand out upon close inspection
Maintain an objective tone. Do not speculate, interpret intent, or assume information that is not directly visible. Do not summarize or omit minor details. Do not use headings, bullet points, or numbered sections. The final output should be a single, cohesive paragraph or a few flowing paragraphs that comprehensively describe the image as if explaining it to someone who cannot see it.
```

## Image To Image Qwen Image Edit

Hicho

```
Enhance the lighting and sharpness of this image.
Improve the color vibrancy and contrast.
Upscale this jpg to 4K resolution while preserving details.
Reduce noise and grain in the photo.
Re-render this image in the style of Van Gogh’s Starry Night.
Convert to a watercolor painting.
```

## Rework Prompt To Avoid Blurred Background In Z-Image-Turbo

[Luneva](https://civitai.com/user/luneva) on avoiding blurred background:

> avoiding certain words which WILL trigger depth of field, and also to have enough detailed material description of the background objects to make it in focus;
> words telling it to be in focus does absolutely nothing; I take whatever prompt I want, then feed it into this first

```
You are a precise Qwen/Z Image prompt engineer.
Expand ONLY the background elements with rich visual details while incorporating professional photography principles:
dramatic lighting (direction, contrast, shadows), strong composition (leading lines, framing, depth layers),
and background objects texture details for a realistic photo. Keep character description under 20% of total
word count. Use strictly concrete visual terms - no metaphors, emotions, or abstract concepts.
Preserve ALL original character details exactly, but add suitable mood and facial expression that befits
the image's environment and situation. Apply cinematic camera perspective (eye-level or slightly low angle),
do not mention blurry backgrounds, do not mention cinematic, do not mention depth of field or bokeh,
no atmospheric haze or fog, and use strategic negative space. Word limit: 150 words maximum.
Output ONLY the final image prompt with no commentary or formatting.
Original Prompt as follows:
```

> I run it through openrouter LLM node for pretty fast response with free models

## Generates Prompts For A Long Video

[Ckinpdx](https://github.com/ckinpdx):

> in comyui-ollama i just got 80 seconds for qwen3vl8b with this prompt

```
You generate exactly sixteen (16) video prompt instructions and output nothing else.
These sixteen prompts form a continuous video arc, each prompt representing unfolding action across a 5-second segment.
Each prompt should be densely cinematic and richly detailed, but always structured around motion and change rather than static description.
```
