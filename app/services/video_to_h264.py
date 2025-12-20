from services.output_path_folder import output_path_folder
from werkzeug.datastructures import FileStorage
import ffmpeg  # type: ignore
import os

def video_to_h264(file: FileStorage) -> int:
    print("file at h264",file)
    """
    Optimize MP4 with H.264 encoding
    
    Args:
        input_path: Path to input MP4 file
        output_path: Path to output MP4 file
        crf: Constant Rate Factor (18-23 recommended, lower = better quality)
        preset: Encoding speed (ultrafast, fast, medium, slow, veryslow)
        audio_bitrate: Audio bitrate (e.g., '128k', '192k')
    """
    try:
        # Save the file temporarily to a directory
        original_filename = os.path.splitext(file.filename or "temp_video.mp4")[0]
        output_path = output_path_folder()
        
        # Save the uploaded file with original extension first
        input_file_path = os.path.join(output_path, f"{original_filename}_input.mp4")
        file.save(input_file_path)

        # Create the output file path for the H.264 MP4 video
        output_file_path = os.path.join(output_path, f"{original_filename}.mp4")

        # Convert the video to H.264 MP4 format
        # crf=20: Constant Rate Factor (18-23 recommended, lower = better quality)
        # preset='medium': Encoding speed vs compression (ultrafast, fast, medium, slow, veryslow)
        ffmpeg.input(input_file_path).output(output_file_path, # type: ignore
                vcodec='libx264',
                crf=20,
                preset='medium',
                pix_fmt='yuv420p',
                acodec='aac',
                audio_bitrate='128k',
                movflags='+faststart',
                **{'profile:v': 'high', 'level:v': '4.2'}
            ).overwrite_output().run(capture_stdout=True, capture_stderr=True) # type: ignore
        return 200
    except ffmpeg.Error as e:
        print(f"FFmpeg error occurred:")
        # print(f"stdout: {e.stdout.decode() if e.stdout else 'N/A'}")
        # print(f"stderr: {e.stderr.decode() if e.stderr else 'N/A'}")
        return 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 500