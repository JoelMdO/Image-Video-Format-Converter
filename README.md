# FromPNGtoWEBP

FromPNGtoWEBP is an in-progress Flask application that helps designers and developers convert assets into the formats their projects need. It currently focuses on:

- Converting PNG images to modern WEBP files.
- Translating WEBP images back to PNG when legacy compatibility is required.
- Turning MP4 videos into WEBM for web delivery.
- Processing SVG artwork into WEBP while preserving transparency.
- Generating favicon and platform icon bundles (ICO, PNG, Apple touch) from a single source image.

## Status

The application is **under active development**. Interfaces, APIs, and feature coverage may change as the tooling evolves.

## Quick Start

1. Create and activate a Python 3.12+ virtual environment.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```sh
   flask --app app.main run
   ```
4. Open a browser at `http://localhost:5000` and upload assets through the UI.

## Key Components

- `app/main.py` – Flask entry point, routing, and conversion orchestration.
- `app/services/` – Conversion utilities for images, videos, favicons, and path helpers.
- `app/templates/index.html` – HTMX-enabled upload interface with mode toggles.
- `app/static/` – Styles, JavaScript helpers, and branding assets.

## Techstack

- Python
- HTMX
- CSS
- JS

## Roadmap Highlights

- Broader format coverage and batch processing.
- Improved error handling and progress feedback.
- Automated test coverage for service functions.
- Packaging for deployment to managed hosting.

## Nest Stage.

- Remove background

Contributions, bug reports, and suggestions are welcome while the project grows into a complete asset conversion toolkit.
