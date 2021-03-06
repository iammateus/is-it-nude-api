import os
import nude
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

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
    return jsonify({"result": nude.is_nude(filePath)})

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
    