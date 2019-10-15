from Modules import create_app
from flask_script import Manager
import config

app = create_app(config.Development)
manager = Manager(app)

@manager.command
def run():
    app = create_app(config.Development)
    app.run(debug = True)

if __name__ == '__main__':
    manager.run()

