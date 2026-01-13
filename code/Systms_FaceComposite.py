# Copyright (c) [2026] Ingi Erlingsson https://x.com/ingi_erlingsson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import torch
import numpy as np
import cv2
from tqdm import tqdm
from comfy.utils import ProgressBar

class FaceComposite:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "original_images": ("IMAGE", {"tooltip": "Original video frames before face extraction"}),
                "face_images": ("IMAGE", {"tooltip": "Refined face images to composite back"}),
                "face_bboxes": ("BBOX", {"tooltip": "Face bounding boxes from Pose and Face Detection node"}),
            },
            "optional": {
                "blend_mode": (["replace", "alpha_blend", "feather"], {"default": "feather", "tooltip": "How to blend refined faces back onto original"}),
                "feather_amount": ("INT", {"default": 5, "min": 0, "max": 50, "step": 1, "tooltip": "Pixels to feather at edge (only for feather mode)"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("composited_images",)
    FUNCTION = "composite"
    CATEGORY = "WanAnimatePreprocess"
    DESCRIPTION = "Composites refined face images back onto original video using bounding box coordinates. Handles frames without faces (bbox at 0,0 with original size) by passing through unchanged."

    def composite(self, original_images, face_images, face_bboxes, blend_mode="feather", feather_amount=5):
        """
        Composite refined face images back onto original frames.
        
        Args:
            original_images: Original video frames [B, H, W, C]
            face_images: Refined face crops [B, h, w, C] 
            face_bboxes: List of (x1, y1, x2, y2) tuples
            blend_mode: How to blend faces back
            feather_amount: Pixels to feather at edges
        """
        B, H, W, C = original_images.shape
        
        # Convert to numpy for easier manipulation
        original_np = (original_images.numpy() * 255).astype(np.uint8)
        face_np = (face_images.numpy() * 255).astype(np.uint8)
        
        result_frames = []
        comfy_pbar = ProgressBar(B)
        
        for idx in tqdm(range(B), desc="Compositing faces"):
            # Get the original frame
            frame = original_np[idx].copy()
            
            # Get bbox for this frame
            if idx >= len(face_bboxes):
                # If we run out of bboxes, just use original frame
                result_frames.append(frame)
                continue
                
            x1, y1, x2, y2 = face_bboxes[idx]
            
            # Check if this is a "no face detected" frame
            # These have bbox at (0, 0) with full image dimensions
            is_full_frame = (x1 == 0 and y1 == 0 and x2 == W and y2 == H)
            
            if is_full_frame:
                # No face was detected in this frame, pass through original
                result_frames.append(frame)
            else:
                # We have a valid face bbox, composite it back
                face_img = face_np[idx]
                
                # Calculate bbox dimensions
                bbox_width = x2 - x1
                bbox_height = y2 - y1
                
                # Resize refined face to match bbox size
                if bbox_width > 0 and bbox_height > 0:
                    face_resized = cv2.resize(face_img, (bbox_width, bbox_height), interpolation=cv2.INTER_LANCZOS4)
                    
                    if blend_mode == "replace":
                        # Simple replacement
                        frame[y1:y2, x1:x2] = face_resized
                        
                    elif blend_mode == "alpha_blend":
                        # Simple alpha blend (50/50)
                        alpha = 0.5
                        frame[y1:y2, x1:x2] = cv2.addWeighted(
                            frame[y1:y2, x1:x2], 1 - alpha,
                            face_resized, alpha,
                            0
                        )
                        
                    elif blend_mode == "feather":
                        # Create a feathered mask for smooth blending
                        mask = self._create_feathered_mask(bbox_width, bbox_height, feather_amount)
                        
                        # Apply mask
                        for c in range(3):  # For each color channel
                            frame[y1:y2, x1:x2, c] = (
                                face_resized[:, :, c] * mask + 
                                frame[y1:y2, x1:x2, c] * (1 - mask)
                            ).astype(np.uint8)
                
                result_frames.append(frame)
            
            if (idx + 1) % 10 == 0:
                comfy_pbar.update_absolute(idx + 1)
        
        # Convert back to tensor
        result_np = np.stack(result_frames, 0)
        result_tensor = torch.from_numpy(result_np).float() / 255.0
        
        return (result_tensor,)
    
    def _create_feathered_mask(self, width, height, feather_amount):
        """
        Create a feathered mask for smooth edge blending.
        
        Args:
            width: Mask width
            height: Mask height  
            feather_amount: Pixels to feather from edges
            
        Returns:
            2D numpy array with values 0-1
        """
        if feather_amount == 0:
            return np.ones((height, width), dtype=np.float32)
        
        # Create coordinate grids
        y, x = np.ogrid[:height, :width]
        
        # Calculate distance from edges
        dist_left = x
        dist_right = width - 1 - x
        dist_top = y
        dist_bottom = height - 1 - y
        
        # Get minimum distance to any edge
        dist_to_edge = np.minimum(
            np.minimum(dist_left, dist_right),
            np.minimum(dist_top, dist_bottom)
        )
        
        # Create feathered mask
        mask = np.clip(dist_to_edge / feather_amount, 0, 1).astype(np.float32)
        
        return mask


NODE_CLASS_MAPPINGS = {
    "FaceComposite": FaceComposite,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FaceComposite": "Face Composite",
}

