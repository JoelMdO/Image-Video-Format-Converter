import os
from typing import Any

from PIL import Image
from PIL.Image import Resampling
from services.output_path_folder import output_path_folder


def create_favicon(file: Any) -> int:
    """Generate favicon and platform icons from an uploaded image."""
    try:
        with Image.open(file) as img:  # type: ignore[arg-type]
            output_path = output_path_folder()
            base_image = img.convert("RGBA")

            # Save multi-resolution ICO for legacy support
            ico_sizes = [(16, 16), (32, 32), (48, 48)]
            ico_variants = [base_image.resize(size, Resampling.LANCZOS) for size in ico_sizes]  # type: ignore[call-overload]
            ico_variants[0].save(os.path.join(output_path, "favicon.ico"), format="ICO", sizes=ico_sizes)
            print(f"Favicon saved as {output_path}/favicon.ico")

            # Generate requested PNG variants
            png_targets = {
                "android-chrome-192x192.png": (192, 192),
                "android-chrome-512x512.png": (512, 512),
                "favicon-16x16.png": (16, 16),
                "favicon-32x32.png": (32, 32),
            }

            for filename, size in png_targets.items():
                resized = base_image.resize(size, Resampling.LANCZOS)  # type: ignore[call-overload]
                resized.save(os.path.join(output_path, filename), format="PNG")
                print(f"Saved {filename} in {output_path}")

            # Maintain Apple touch icon support
            base_image.resize((180, 180), Resampling.LANCZOS).save(  # type: ignore[call-overload]
                os.path.join(output_path, "apple-touch-icon.png"),
                format="PNG",
            )
            print(f"Apple Touch Icon saved as {output_path}/apple-touch-icon.png")

            return 200
    except Exception as e:
        print(f"Error: {e}")
        return 500

