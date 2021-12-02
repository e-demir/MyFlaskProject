from flask import Flask, Blueprint
from .views import home, users, contacts


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile("config.py")
    app.register_blueprint(home.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(contacts.bp)

    return app
