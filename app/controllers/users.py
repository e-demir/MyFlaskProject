from flask import session

def UserLogin(username, password):
    if username == "admin" and password == "admin":
        session["username"] = username
        return True
    else:
        return False

def UserLogout():
    if "username" in session:
        del session["username"]
        return True
    else:
        return False


def GetCurrentUser():
    username = ""
    login_auth = False
    if "username" in session:
        username = session["username"]
        login_auth = True

    return username, login_auth
