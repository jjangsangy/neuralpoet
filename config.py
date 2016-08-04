import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'E8OuPFR6aHogiH3gJunU6nNIFNJFCZRKmI4k'


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
