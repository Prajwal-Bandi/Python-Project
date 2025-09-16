from flask import Flask
from .routes import init_routes
from .logger import logger

def create_app():
    app = Flask(__name__)
    init_routes(app)
    return app
