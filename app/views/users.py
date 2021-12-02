from flask import request,redirect,url_for,abort,render_template, Blueprint
from app.controllers import UserLogin, UserLogout,GetCurrentUser

bp = Blueprint(name="users", import_name=__name__, template_folder="../templates")

@bp.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username,password):
                    return redirect(url_for("home.Index"))
                else:
                    return redirect(url_for("users.Login"))
        abort(400)
    username, login_auth = GetCurrentUser()
    return render_template("login.html", username=username, login_auth=login_auth)

@bp.route("/logout")
def Logout():
    UserLogout()
    return redirect(url_for("home.Index"))