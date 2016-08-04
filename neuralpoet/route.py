from datetime import datetime

from flask import Blueprint, jsonify, render_template

poet = Blueprint('poet', __name__)


@poet.route('/')
def index():
    return render_template('index.html')


@poet.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
