from flask import Flask
from routes import pages


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)

    return app
