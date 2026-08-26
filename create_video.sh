#!/bin/bash
# Create a simple tutorial demo video using ffmpeg
# This generates a video with animated text and colors

ffmpeg -f lavfi -i color=c=blue:s=1280x720:d=5 \
  -vf "drawtext=fontfile=/Windows/Fonts/Arial.ttf:fontsize=60:fontcolor=white:text='WAN AI Tutorial':x=(w-text_w)/2:y=(h-text_h)/2-100, \
       drawtext=fontfile=/Windows/Fonts/Arial.ttf:fontsize=40:fontcolor=yellow:text='Demo Video':x=(w-text_w)/2:y=(h-text_h)/2+50" \
  -pix_fmt yuv420p \
  -y demo_tutorial.mp4

echo "Video created: demo_tutorial.mp4"
