from flask import Flask
from app.routes.scan_routes import scan_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(scan_bp)
    return app