import os

def output_path_folder():
    ## Set the output path
    home_directory = os.path.expanduser("~")  # Get the home directory
    output_path_folder = os.path.join(home_directory, "Downloads")
    os.makedirs(output_path_folder, exist_ok=True)

    return output_path_folder