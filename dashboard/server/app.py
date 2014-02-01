from flask import Flask, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from .db import db
from .blueprints import register_blueprints

def create_app(config=None, **kwargs):
    app = Flask(__name__)
    app.debug = True

    # TODO - read config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SECRET_KEY'] = 'abc123'

    # SQLAlchemy
    db.init_app(app)

    # Toolbar
    DebugToolbarExtension(app)

    # Bluprints
    register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
    db.create_all()
