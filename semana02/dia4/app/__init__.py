from time import perf_counter
from flask import Flask
from app.FirebaseAdmin import FirebaseAdmin

fb = FirebaseAdmin()

##blueprints
from .portafolio import portafolio


##archivo de configuración
from .config import Config

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    app.register_blueprint(portafolio)

    return app