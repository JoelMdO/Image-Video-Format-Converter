from PIL import Image
import os
from services.output_path_folder import output_path_folder 
from typing import Optional, Union
from werkzeug.datastructures import FileStorage
import io

# Increase PIL's pixel limit to handle large images (e.g., 4x resolution)
# Set to None to disable limit entirely, or set a specific value (in pixels)
Image.MAX_IMAGE_PIXELS = None  # or use a specific value like 500000000


##-----------------------------------------------##
## Convert PNG to WEBP
##-----------------------------------------------##
def png_to_webp(file: Union[str, FileStorage, io.BytesIO], fileName: Optional[str] = None) -> int:
    try:
        with Image.open(file) as img:  # type: ignore
            if img.format == 'JPEG':
                print("Warning: The provided file is not a PNG image. Proceeding with conversion from JPEG to WebP.")
                # Convert to PNG from JPEG
                if img.mode in ("RGBA", "LA") or "transparency" in img.info:
                    background = Image.new("RGB", img.size, "white")
                    if img.mode != "RGBA":
                        img = img.convert("RGBA")
                    background.paste(img, mask=img.getchannel("A"))
                    img = background
                else:
                    img = img.convert("RGB")

            # WebP has a max dimension limit of 16383 pixels
            MAX_WEBP_DIMENSION = 16383
            width, height = img.size
            
            # Check if resizing is needed
            if width > MAX_WEBP_DIMENSION or height > MAX_WEBP_DIMENSION:
                # Calculate scaling factor to fit within limits
                scale = min(MAX_WEBP_DIMENSION / width, MAX_WEBP_DIMENSION / height)
                new_width = int(width * scale)
                new_height = int(height * scale)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS) # type: ignore
                print(f"Image resized from {width}x{height} to {new_width}x{new_height} to fit WebP limits")
            
            if fileName:
                print(f"fileName provided: {fileName}")
                original_filename = os.path.splitext(fileName)[0]
            elif isinstance(file, FileStorage) and file.filename:
                original_filename = os.path.splitext(file.filename)[0]
            else:
                original_filename = "converted_file"
            
            output_path = output_path_folder()
            img.save(os.path.join(output_path, f"{original_filename}.webp"), format='WEBP')
            return 200
    except Exception as e:
        print(f"Error: {e}")
        return 500