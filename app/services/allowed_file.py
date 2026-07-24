ALLOWED_EXTENSIONS = {'png', 'jpeg','mp4', 'svg', 'webp'}

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS