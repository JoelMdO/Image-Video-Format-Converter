from PIL import Image
import os
from services.output_path_folder import output_path_folder 
from typing import Optional

# Increase PIL's pixel limit to handle large images (e.g., 4x resolution)
# Set to None to disable limit entirely, or set a specific value (in pixels)
Image.MAX_IMAGE_PIXELS = None  # or use a specific value like 500000000


##-----------------------------------------------##
## Convert PNG to WEBP
##-----------------------------------------------##
def png_to_webp(file: str, fileName: Optional[str] = None):
    try:
        with Image.open(file) as img:
            # WebP has a max dimension limit of 16383 pixels
            MAX_WEBP_DIMENSION = 16383
            width, height = img.size
            
            # Check if resizing is needed
            if width > MAX_WEBP_DIMENSION or height > MAX_WEBP_DIMENSION:
                # Calculate scaling factor to fit within limits
                scale = min(MAX_WEBP_DIMENSION / width, MAX_WEBP_DIMENSION / height)
                new_width = int(width * scale)
                new_height = int(height * scale)
                img = img.resize((new_width, new_height), Image.LANCZOS)
                print(f"Image resized from {width}x{height} to {new_width}x{new_height} to fit WebP limits")
            
            if fileName:
                original_filename = fileName
                
            elif file.filename:
                original_filename = os.path.splitext(file.filename)[0]
            
            output_path = output_path_folder()
            img.save(os.path.join(output_path, f"{original_filename}.webp"), format='WEBP')
            return 200
    except Exception as e:
        print(f"Error: {e}")
        return 500