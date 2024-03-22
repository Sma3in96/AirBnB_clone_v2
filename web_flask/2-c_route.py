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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
