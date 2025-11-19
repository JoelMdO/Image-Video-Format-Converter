import subprocess

try:
    result = subprocess.run(["ffmpeg", "-version"], check=True, text=True, capture_output=True)
    print("FFmpeg binary is accessible!")
    print(result.stdout)
except FileNotFoundError:
    print("FFmpeg binary not found. Ensure it's installed and in PATH.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")