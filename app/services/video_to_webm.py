from services.output_path_folder import output_path_folder
from werkzeug.datastructures import FileStorage
import ffmpeg  # type: ignore
import os

def video_to_webm(file: FileStorage) -> int:
    print("file at webm")
    try:
        # Save the file temporarily to a directory
        original_filename = os.path.splitext(file.filename or "temp_video.mp4")[0]
        output_path = output_path_folder()
        
        # Save the uploaded file with original extension first
        input_file_path = os.path.join(output_path, f"{original_filename}_input.mp4")
        file.save(input_file_path)

        # Create the output file path for the WebM video
        output_file_path = os.path.join(output_path, f"{original_filename}.webm")

        # Convert the video to WebM format
        # crf=10,  # Lower is better quality, try 4-10  
        #bitrate='2M'  # Set a higher bitrate if needed)
        ffmpeg.input(input_file_path).output(output_file_path, vcodec='libvpx', acodec='libvorbis', crf=10).overwrite_output().run(capture_stdout=True, capture_stderr=True) # type: ignore
        return 200
    except ffmpeg.Error as e:
        print(f"FFmpeg error occurred:")
        # print(f"stdout: {e.stdout.decode() if e.stdout else 'N/A'}")
        # print(f"stderr: {e.stderr.decode() if e.stderr else 'N/A'}")
        return 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 500