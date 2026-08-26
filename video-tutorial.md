# Video Tutorial Setup

This directory contains tutorial and demo videos for the WAN AI ecosystem.

## Adding Videos

To add a tutorial/demo video to this site:

1. **Create or record your video** in MP4 format (recommended: 1280x720 resolution, 30fps)
2. **Place the video file** in this directory or a subdirectory
3. **Create an HTML page** linking to the video (see examples below)

## Video Player Examples

### Basic HTML5 Video Player

```html
<!DOCTYPE html>
<html>
<head>
    <title>WAN AI Tutorial</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1280px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }
        video { width: 100%; height: auto; border-radius: 8px; }
        .info { margin-top: 20px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="container">
        <h1>WAN AI Video Tutorial</h1>
        <video controls>
            <source src="tutorial.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <div class="info">
            <h2>Tutorial Overview</h2>
            <p>This tutorial covers the basics of WAN AI video generation.</p>
            <ul>
                <li>Getting started with WAN models</li>
                <li>Basic prompt engineering</li>
                <li>Advanced techniques</li>
            </ul>
        </div>
    </div>
</body>
</html>
```

### Responsive Video with Chapters

```html
<!DOCTYPE html>
<html>
<head>
    <title>Advanced WAN Techniques</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a1a1a; color: white; margin: 0; padding: 20px; }
        .container { max-width: 1280px; margin: 0 auto; }
        video { width: 100%; background: black; border-radius: 8px; }
        .chapters { margin-top: 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; }
        .chapter-btn { padding: 10px 15px; background: #0066cc; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .chapter-btn:hover { background: #0052a3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Advanced WAN Techniques</h1>
        <video id="tutorial-video" controls>
            <source src="advanced-tutorial.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <div class="chapters">
            <button class="chapter-btn" onclick="seekTo(0)">Intro (0:00)</button>
            <button class="chapter-btn" onclick="seekTo(30)">Techniques (0:30)</button>
            <button class="chapter-btn" onclick="seekTo(120)">Advanced Tips (2:00)</button>
            <button class="chapter-btn" onclick="seekTo(200)">Q&A (3:20)</button>
        </div>
    </div>
    <script>
        function seekTo(seconds) {
            document.getElementById('tutorial-video').currentTime = seconds;
        }
    </script>
</body>
</html>
```

## Recommended Video Specifications

- **Format**: MP4 (H.264 codec)
- **Resolution**: 1280x720 (720p) or 1920x1080 (1080p)
- **Frame Rate**: 30fps
- **Bitrate**: 2-5 Mbps
- **Audio**: AAC, 128 kbps, 48kHz

## Tips for Creating Good Tutorial Videos

1. **Keep it concise** - Aim for 5-10 minute videos
2. **Use clear audio** - Speak clearly and use a good microphone
3. **Annotate when needed** - Add text overlays for technical terms
4. **Show your workflow** - Screen recordings work best for software tutorials
5. **Include captions** - Help non-native speakers and those watching silently

## Tools for Creating Videos

- **Screen Recording**: OBS Studio, Camtasia, ScreenFlow (Mac)
- **Video Editing**: DaVinci Resolve, Adobe Premiere, Final Cut Pro
- **Video Conversion**: FFmpeg, HandBrake, MediaConverter

## Hosting Large Videos

GitHub has file size limits. For very large video files:
1. Upload to a hosting service (YouTube, Vimeo, etc.)
2. Embed using an iframe or link
3. Or compress the video further

Example embedding from YouTube:
```html
<iframe width="1280" height="720" src="https://www.youtube.com/embed/VIDEO_ID" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
```

---

**Ready to create your video?** Follow the examples above and add your tutorial to this site!
