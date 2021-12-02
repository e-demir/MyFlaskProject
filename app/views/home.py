from flask import render_template
from app.controllers import GetCurrentUser

def Index():
    username, login_auth = GetCurrentUser()
    return render_template("index.html",username=username, login_auth=login_auth)
