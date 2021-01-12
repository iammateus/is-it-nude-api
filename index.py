from flask import Flask, jsonify, request
import nude

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    data = {'message': 'The server is running! (Todo-api of the snake)'}
    return jsonify(data)

@app.route("/")
def isItNude():
    data = {'isNude': nude.is_nude("./pic.jpg")}
    return jsonify(data)

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
    