from datetime import datetime

from flask import Blueprint, jsonify

poet = Blueprint('poet', __name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
