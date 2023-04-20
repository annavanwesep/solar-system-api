from flask import Flask, Blueprint


def create_app(test_config=None):
    app = Flask(__name__)
    
    from .routes import planets_bp
    
    app.register_blueprint(planets_bp)
    
    return app
