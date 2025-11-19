from flask import Flask, request, render_template
from services.webp_to_png import webp_to_png
from services.favicon import create_favicon
from services.png_to_webp import png_to_webp
from services.allowed_file import allowed_file
from services.video_to_webm import video_to_webm
from services.file_extension import file_extension
from services.svg_to_webp import svg_to_webp

app = Flask(__name__)
# Track which conversion mode should run (convert vs favicon)
toggle_state = {"mode": "convert"}
@app.route('/')
def index():
    return render_template('index.html',show_popup=False)
##==========================================================
## Get the value of the option to use (Create Image or FavIcon)
##==========================================================
@app.route("/toggle", methods=["POST"])
def toggle():
    global toggle_state
    payload = request.form or (request.get_json(silent=True) or {})
    toggle_state["mode"] = payload.get("mode", "convert")
    print(f"Toggle Updated: {toggle_state['mode']}")
    return {"message": "Toggle value received", "mode": toggle_state["mode"]}
##==========================================================
## Upload the file and act according to the toggle value
##==========================================================
@app.route('/upload', methods=['POST'])
def upload_file():
    ##Get the toggle value.
    global toggle_state
    print(f"Toggle Value at Upload: {toggle_state['mode']}")

    response = 1
    print("at upload")
    
    # Check if the file is present
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    print(f"file to name", file.filename)
    if file.filename == '':
        return 'No selected file', 400
    
    #Option to create image or FavIcon
    if toggle_state["mode"] == "favicon":
        ##Create a favicon.
        print("going to favicon")
        response = create_favicon(file)
    else:
        #Convert image.
        #Check the extension of the  file to define the transformation it.      
        if file and allowed_file(file.filename) :
            print(f"file to change", file_extension(file.filename))
            if file_extension(file.filename) == 'png':
                print("file to change to png")
                response = png_to_webp (file)
            elif file_extension(file.filename) == 'mp4':
                print("file to change to mp4")
                response = video_to_webm (file)
            elif file_extension(file.filename) == 'svg':
                print("file to change to svg")
                response = svg_to_webp (file)
                print(response)
            elif file_extension(file.filename) == 'webp':
                print("file to change to svg")
                response = webp_to_png (file)
                print(response)
    
    if (response == 200):    
        return render_template('index.html', show_popup=True, output_folder='Downloads')
    else:
        return render_template('index.html', show_popup=True, output_folder='Error 400')

if __name__ == '__main__':
    app.run(debug=True)