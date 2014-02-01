from .main import main

def register_blueprints(app):
    """All blueprints should be registered in this location.
    """
    # Front page, static pages, etc.
    app.register_blueprint(main)

