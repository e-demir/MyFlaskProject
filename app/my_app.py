from flask import Flask
from .views import Index as _Index
from .views import Login as _Login
from .views import Logout as _Logout
from .views import Contact as _Contact
from .views import ContactList as _ContactList


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = b"secretkey1903"
    app.config.from_pyfile("config.py")


    # app.session_interface = MySessionInterface()

    @app.route("/")
    def Index():
        return _Index()

    @app.route("/login", methods=["GET", "POST"])
    def Login():
        return _Login()

    @app.route("/logout")
    def Logout():
        return _Logout()

    @app.route("/contact", methods=["GET", "POST"])
    def Contact():
        return _Contact()

    @app.route("/list")
    def ContactList():
        return _ContactList()

    return app
