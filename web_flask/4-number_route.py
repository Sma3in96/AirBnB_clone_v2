#!/usr/bin/python3
""" start a web app """
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def Hello():
    """ print hello at route root """
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """ print hbnb """
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def textfunc(text):
    """ print a passed text"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ print python something"""
    if text:
        text1 = text.replace('_', ' ')
    else:
        text1 = "is cool"
    return f"Python {text1}"


@app.route("/python/", strict_slashes=False)
def pth():
    """ default """
    return "Python is cool"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """ print n if its an integer"""
    if type(int(n)) is int:
        return f'{n} is a number'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
