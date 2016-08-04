import os

from flask_script import Manager

from neuralpoet import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
