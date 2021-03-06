"""
Creates Flask HTTP server to run the Custom Vision model.
"""
import json
import os
import io

# Imports for the REST API
from flask import Flask, request, jsonify, Response

# Imports for image procesing
from PIL import Image

# Imports for prediction
from onnxruntime_predict import initialize, predict_image

app = Flask(__name__)

# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024 

# Default route just shows simple text
@app.route('/')
def index():
    return 'CustomVision.ai model host harness'

# Like the CustomVision.ai Prediction service /image route handles either
#     - octet-stream image file 
#     - a multipart/form-data with files in the imageData parameter
@app.route('/image', methods=['POST'])
@app.route('/<project>/image', methods=['POST'])
@app.route('/<project>/image/nostore', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/image', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/image/nostore', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/image', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/image/nostore', methods=['POST'])
def predict_image_handler(project=None, publishedName=None):
    try:
        imageData = None
        if ('imageData' in request.files):
            imageData = request.files['imageData']
        elif ('imageData' in request.form):
            imageData = request.form['imageData']
        else:
            imageData = io.BytesIO(request.get_data())

        img = Image.open(imageData)
        response = predict_image(img)
        return jsonify(response)
    except Exception as err:
        err_val = '[ERROR] Exception in score : {}'.format(repr(err))
        print(err_val)
        return Response(response=json.dumps(err_val), status=500)


if __name__ == '__main__':
    # Load and intialize the model
    initialize()

    # Run the server
    app.run(host='0.0.0.0', port=80)

