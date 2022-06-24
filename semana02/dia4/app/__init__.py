from time import perf_counter
from flask import Flask

##blueprints
from .portafolio import portafolio

def create_app():
    app = Flask(__name__)

    app.register_blueprint(portafolio)

    return app