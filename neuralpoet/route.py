from datetime import datetime

from flask import Blueprint, jsonify

poet = Blueprint('poet', __name__)


@poet.route('/')
def index():
    return 'Hello World'


@poet.route('/default')
def default_jsonencoder():
    now = datetime.now()
    return jsonify({'now': now})
