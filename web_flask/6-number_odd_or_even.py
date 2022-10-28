#!/usr/bin/python3
"""
Flask App
"""
from flask import Flask
from flask import render_template

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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
def get_python(text):
    """ python smart route"""
    value = "is cool"
    if text:
        value = text.replace("_", " ")
    return "Python {}".format(value)


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """check if number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """ number template example"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ check odd or even"""
    val = "odd"
    if n % 2 == 0:
        val = "even"
    return render_template("6-number_odd_or_even.html", n=n, val=val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
