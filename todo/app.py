import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from todo import api, commands
from todo.extensions import db


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    return None


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.create_todo)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(api.graphql.blueprint)
    return None


def create_app():
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/."""
    app = Flask(__name__.split(".")[0])
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app
