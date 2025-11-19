from services.output_path_folder import output_path_folder
import ffmpeg
import os
def video_to_webm(file):
    print("file at webm",file)
    try:
        # Save the file temporarily to a directory
        original_filename = os.path.splitext(file.filename)[0]
        output_path = output_path_folder()
        input_file_path = os.path.join(output_path, original_filename)

        # Save the uploaded file to the disk
        file.save(input_file_path)

        # Create the output file path for the WebM video
        output_file_path = os.path.join(output_path, f"{os.path.splitext(original_filename)[0]}.webm")

        # Convert the video to WebM format
        ffmpeg.input(input_file_path).output(output_file_path, vcodec='libvpx', acodec='libvorbis').run()
        return 200
    except ffmpeg.Error as e:
        return 500