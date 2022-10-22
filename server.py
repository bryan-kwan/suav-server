from flask import Flask, render_template, request, send_from_directory
import glob
import json
import yolo

#------------------
# Main Server File
#------------------

#Flask is the web API libary used
app = Flask(__name__)

#Set the root path to return an HTML file
@app.get('/')
def index():
    return send_from_directory('vue/dist/', 'index.html')

@app.get('/version/')
def version():
    return '1.0.1'

#Lists all .jpg files available in /images/
@app.get('/images/')
def list_images():
    return json.dumps(glob.glob('images/*.jpg'))

#Returns a requested image
@app.get('/images/<file_name>/')
def get_image(file_name):
    return send_from_directory('images', file_name)

#POST request to accept an image upload - no arguments are taken, image is presumed to contain all data
@app.post('/submit/')
def submit_image():
    file = request.files["file"] #file must be attached in body with name "file"
    file.save('images/'+file.filename) #saves the image
    print('Saved file', file.filename)
    #Perform YOLO detections - all detections should be moved to a queue and handled by seperate thread at some point
    #yolo.image_detections(file.filename)
    return 'ok'

#Returns images or other assets (currently the SUAV logo image is the only asset)
@app.get('/<file_name>/')
def get_file(file_name):
    return send_from_directory('vue/dist/', file_name)

@app.get('/js/<file_name>/')
def get_js_file(file_name):
    return send_from_directory('vue/dist/js/', file_name)

@app.get('/img/<file_name>/')
def get_img_file(file_name):
    return send_from_directory('vue/dist/img/', file_name)

@app.get('/css/<file_name>/')
def get_css_file(file_name):
    return send_from_directory('vue/dist/css/', file_name)

#Runs only if this program is the main script (can't be executed by another script)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
