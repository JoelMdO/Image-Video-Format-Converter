from services.output_path_folder import output_path_folder
from services.png_to_webp import png_to_webp
import io
import cairosvg
def svg_to_webp(file):
    print("file at svg to webm",file)
    try:
        # Convert the SVG to a PNG byte stream
        svg_data = file.read()
        png_data = cairosvg.svg2png(bytestring=svg_data)
        # Convert the PNGto webp
        response = png_to_webp (io.BytesIO(png_data), fileName=file.filename)
        print("response after png",response)
        return 200
    except Exception as e:
        return 500