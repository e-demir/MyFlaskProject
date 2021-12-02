from flask import request,redirect,url_for,abort,render_template
from app.controllers import UserLogin, UserLogout,GetCurrentUser

def Login():
    if request.method == "POST":
        if request.form:
            if "username" in request.form and "password" in request.form:
                username = request.form["username"]
                password = request.form["password"]
                if UserLogin(username,password):
                    return redirect(url_for("Index"))
                else:
                    return redirect(url_for("Login"))
        abort(400)
    username, login_auth = GetCurrentUser()
    return render_template("login.html", username=username, login_auth=login_auth)

def Logout():
    UserLogout()
    return redirect(url_for("Index"))