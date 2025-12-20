from typing import Union

def file_extension(filename: str) -> Union[str, bool]:
    return '.' in filename and filename.rsplit('.', 1)[1].lower()