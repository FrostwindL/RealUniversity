from flask import Flask
from .extensions import api, db
from .resources import ns

def create_app():
    api.add_namespace(ns)
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    api.init_app(app)
    db.init_app(app)

    

    return app