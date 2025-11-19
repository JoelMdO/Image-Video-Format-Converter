from PIL import Image
import os
from services.output_path_folder import output_path_folder
from typing import Optional

##-----------------------------------------------##
## Convert WEBP to PNG
##-----------------------------------------------##
def webp_to_png(file: str, fileName: Optional[str] = None):

    # TODO: check again how to do it
    try:
        with Image.open(file) as img:
            img = img.convert("RGBA") 
            if fileName:
                original_filename = fileName
            elif hasattr(file, 'filename'):
                original_filename = os.path.splitext(file.filename)[0]
            else:
                original_filename = os.path.splitext(os.path.basename(file))[0]
            
            output_path = output_path_folder()
            img.save(os.path.join(output_path, f"{original_filename}.png"), format='PNG', optimize=True)
            return 200
    except Exception as e:
        print(f"Error: {e}")
        return 500