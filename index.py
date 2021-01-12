from flask import Flask, jsonify, request
import nude
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/var/www/html/resources'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/healthcheck")
def healthcheck():
    data = {'message': 'The server is running! (Is it Nude API)'}
    return jsonify(data)

@app.route("/", methods = ['POST'])
def isItNude():
    imageFile = request.files['image']
    filename = secure_filename(imageFile.filename)
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    imageFile.save(filePath)
    data = {'isItNude': nude.is_nude(filePath)}
    return jsonify(data)

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
    