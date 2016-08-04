from datetime import datetime

from flask import Blueprint, jsonify, render_template

site = Blueprint('site', __name__)


@site.route('/')
def index():
    return render_template('index.html')
