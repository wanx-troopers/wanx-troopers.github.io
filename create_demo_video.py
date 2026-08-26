#!/usr/bin/env python3
"""
Create a sample tutorial/demo video for testing video embedding on GitHub Pages.
This script generates a simple MP4 video with text and shapes.
"""

import cv2
import numpy as np
import os

def create_demo_video(output_path="demo_tutorial.mp4", duration_seconds=5, fps=30):
    """
    Create a simple demo/tutorial video.
    
    Args:
        output_path: Path to save the video file
        duration_seconds: Duration of the video in seconds
        fps: Frames per second for the video
    """
    # Video dimensions
    width, height = 1280, 720
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    total_frames = duration_seconds * fps
    
    print(f"Creating demo video: {output_path}")
    print(f"Duration: {duration_seconds}s | FPS: {fps} | Total frames: {total_frames}")
    
    for frame_num in range(total_frames):
        # Create a new frame
        frame = np.ones((height, width, 3), dtype=np.uint8) * 255
        
        # Calculate progress (0 to 1)
        progress = frame_num / total_frames
        
        # Add background gradient
        for i in range(height):
            ratio = i / height
            frame[i, :] = [
                int(255 * (1 - ratio * 0.5)),
                int(200 + 55 * ratio),
                int(150 + 105 * ratio)
            ]
        
        # Draw a circle that grows and changes color
        circle_radius = int(50 + 150 * progress)
        circle_color = (
            int(100 + 155 * progress),
            int(150 + 105 * (1 - progress)),
            int(255 - 155 * progress)
        )
        cv2.circle(frame, (width // 2, height // 2), circle_radius, circle_color, -1)
        
        # Draw a rectangle with animation
        rect_width = int(200 + 400 * progress)
        rect_x1 = (width - rect_width) // 2
        rect_x2 = rect_x1 + rect_width
        cv2.rectangle(frame, (rect_x1, 100), (rect_x2, 150), (50, 150, 255), 3)
        
        # Add text
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "WAN AI Video Tutorial"
        text_size = cv2.getTextSize(text, font, 1.5, 2)[0]
        text_x = (width - text_size[0]) // 2
        cv2.putText(frame, text, (text_x, 60), font, 1.5, (50, 50, 50), 2)
        
        # Add progress text
        progress_text = f"Progress: {int(progress * 100)}%"
        progress_size = cv2.getTextSize(progress_text, font, 1, 2)[0]
        progress_x = (width - progress_size[0]) // 2
        cv2.putText(frame, progress_text, (progress_x, height - 50), font, 1, (50, 50, 50), 2)
        
        # Write frame to video
        out.write(frame)
        
        # Print progress
        if (frame_num + 1) % (fps * 2) == 0:
            print(f"  Frame {frame_num + 1}/{total_frames} completed...")
    
    # Release the video writer
    out.release()
    
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✓ Video created successfully!")
    print(f"  File: {output_path}")
    print(f"  Size: {file_size_mb:.2f} MB")

if __name__ == "__main__":
    create_demo_video("demo_tutorial.mp4", duration_seconds=5, fps=30)
