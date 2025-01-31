from flask import Flask
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    # # DB configuration
    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("RENDER_DATABASE_URI") #Connect to render
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    
    # Import models 
    from app.models.planet import Planet

    db.init_app(app)
    migrate.init_app(app,db)
    

    # Register Blueprints
    from .routes import planets_bp

    app.register_blueprint(planets_bp)
    
    return app
