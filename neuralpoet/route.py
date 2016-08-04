from datetime import datetime

from flask import Blueprint, jsonify

poet = Blueprint('poet', __name__)


@poet.route('/')
def hello():
    return "Hello World!"


@poet.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
