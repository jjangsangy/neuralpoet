from flask_script import Manager, Server

from neuralpoet import create_app

app = create_app()

server = Server(host="127.0.0.1", port=8080)
manager = Manager(app)

manager.add_command('runserver', server)

if __name__ == "__main__":
    manager.run()
