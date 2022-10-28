#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Index Page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_home():
    """ Display hbnb home"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def get_text(text):
    """ get url params"""
    if text:
        value = str(text).replace("_", " ")
        return "C {}".format(value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
