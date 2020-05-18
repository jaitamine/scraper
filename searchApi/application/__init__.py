from flask import Flask
from .extensions import mongo
from flask_cors import CORS
from .search import search


def create_app(config_file='settings.py'):
    '''
    flask factory method.
    args:
         config_file: used by flask to locate environment variables.
    returns: 
         application instance.
    '''

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    CORS(app)

    app.register_blueprint(search)

    mongo.init_app(app)
    
    return app
