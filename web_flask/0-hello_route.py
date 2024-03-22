#!/usr/bin/python3
""" start a web app """
from flask import Flask

app = Flask(__name__)


@app.route("/", staticmethod=False)
def Hello():
    """ print hello at route root """
    return "Hello HBNB!"
