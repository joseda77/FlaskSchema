MODULE_NAME = 'Modules'
IMPORT_NAME = __name__

from flask import Flask
from flask_cors import CORS

def create_app(configFile = None):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(configFile)

    with app.app_context():
        #Aqui se realizan la importación de modulos y los servicios a exponer
        #app.register_blueprint()

        @app.shell_context_processor
        def ctx():
            return {'app': app}
        return app

