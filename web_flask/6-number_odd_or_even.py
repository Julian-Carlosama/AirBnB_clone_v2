#!/usr/bin/python3
""" Script that starts a Flask web application """
import re
from flask import Flask, render_template
from urllib3 import Retry
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
    return ("C {}".format(tx))
    """return f"C {txt}"."""


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    """ Function called with /python/<text> route """
    if text is not "is cool":
        text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function called with /number_template route """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function called with /number_odd_or_even route """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
