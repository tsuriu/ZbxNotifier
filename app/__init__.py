from flask import Flask

def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    #app.config.from_object("config.Config")

    with app.app_context():
        # Import parts of our application
        from .home import home
        from .api import api
        
        # Register Blueprints
        app.register_blueprint(home.home_bp, url_prefix='/')
        app.register_blueprint(api.api_bp, url_prefix='/api')

        return app