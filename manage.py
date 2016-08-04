import os

from flask_script import Manager, Server

from neuralpoet import create_app

app = create_app()

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
