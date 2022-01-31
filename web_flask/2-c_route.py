#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function called with /hbnb route """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """ Function called with /c/<text> route """
    tx = text.replace("_", " ")
    return (f"C {tx}")
    """return f"C {txt}"."""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
