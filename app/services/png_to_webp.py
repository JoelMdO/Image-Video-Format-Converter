from PIL import Image
import os
from services.output_path_folder import output_path_folder 
from typing import Optional


##-----------------------------------------------##
## Convert PNG to WEBP
##-----------------------------------------------##
def png_to_webp(file: str, fileName: Optional[str] = None):
    try:
        with Image.open(file) as img:
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