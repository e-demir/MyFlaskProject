from flask import render_template, Blueprint
from app.controllers import GetCurrentUser

bp = Blueprint(name="home", import_name=__name__, template_folder="../templates" )

@bp.route("/")
def Index():
    username, login_auth = GetCurrentUser()
    return render_template("index.html",username=username, login_auth=login_auth)
