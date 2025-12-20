from services.png_to_webp import png_to_webp
from werkzeug.datastructures import FileStorage
import io
import cairosvg  # type: ignore

def svg_to_webp(file: FileStorage) -> int:
    print("file at svg to webm")
    try:
        # Convert the SVG to a PNG byte stream
        svg_data = file.read()
        png_data = cairosvg.svg2png(bytestring=svg_data) # type: ignore
        if png_data is None:
            return 500
        # Convert the PNGto webp
        response = png_to_webp (io.BytesIO(png_data), fileName=file.filename) # type: ignore
        print("response after png",response)
        return 200
    except Exception:
        return 500