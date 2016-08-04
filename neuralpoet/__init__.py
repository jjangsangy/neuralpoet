"""
Neural Poet
===========
"""
import os

from flask import Flask
from flask_cors import CORS

__title__ = 'neuralpoet'
__license__ = 'Apache Software License Version 2.0'


def create_app():
    """
    Application factory function

    :param cfg: dict
        Configuration parameters

    :return: app
    """

    app = Flask(__name__)

    from .route import poet

    app.register_blueprint(poet)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # Enable CORS Configuration
    cors = CORS(app)
    return app
