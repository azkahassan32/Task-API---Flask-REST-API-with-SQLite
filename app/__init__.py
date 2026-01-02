#  App Factory
from flask import Flask
from app.routes import api
from app.models import create_table

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    create_table()
    return app
