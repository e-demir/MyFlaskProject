from flask import  Flask, render_template, url_for, redirect, request, make_response,session,abort
from itsdangerous import Signer,BadSignature
from app.controllers import UserLogin, UserLogout,GetCurrentUser,GetContactList, SaveContactRequest

app = Flask(__name__, template_folder="../templates")
app.secret_key = b"secretkey1903"
# app.session_interface = MySessionInterface()

@app.route("/")
def Index():
    username, login_auth = GetCurrentUser()
    return render_template("index.html",username=username, login_auth=login_auth)

@app.route("/contact", methods=["GET","POST"])
def Contact():
    username, login_auth = GetCurrentUser()
    if request.method == "POST":
        if request.form:
            name = request.form.get("name")
            email = request.form.get("email")
            category = request.form.get("category")
            priority = request.form.get("priority")
            message = request.form.get("message")
            SaveContactRequest(name, email, category, priority, message)
            return redirect(url_for("Contact"))
    username,login_auth = GetCurrentUser()
    return render_template("contact.html",username=username, login_auth=login_auth)

@app.route("/contactlist")
def ContactList():
    username, login_auth = GetCurrentUser()
    contactList = GetContactList()
    return render_template("contact_list.html",username=username, login_auth=login_auth, contactList=contactList)

@app.route("/login", methods=["GET","POST"])
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

@app.route("/logout")
def Logout():
    UserLogout()
    return redirect(url_for("Index"))


# @app.route("/")
# def Home():
#     signer = Signer("MySecretKey")
#     signed_name = request.cookies.get("name")   # How to read the cookie
#     try:
#         name = signer.unsign(signed_name).decode()  # bytes to string
#         print("name",name)
#     except BadSignature:
#         print("bad signature")

#     signed_name = signer.sign("Ayca")
#     response = make_response("Flask Denemesidir")
#     response.set_cookie("name",signed_name)  # How to set the cookie
#     return response

# @app.route("/session")
# def Session():
#     if "name" in session:
#         print(session["name"])

#     # Setting the session
#     session["name"] = "Emrullah"
#     session["username"] = "Emrullah123"


#     return "<h1>Merhaba Session</html>"

# @app.route("/hello")
# def Hello():
#     return render_template("hello.html")

# @app.route("/hello_user/<string:name>")
# def HelloUser(name):
#     if name.lower() == "admin":
#         return redirect(url_for("HelloAdmin"))
#     return render_template("hello_user.html",name=name)

# @app.route("/hello_admin")
# def HelloAdmin():
#     return render_template("hello_admin.html")

# @app.route("/hello/<name>")
# def Hello_User(name):
#     return render_template("hello.html",name=name)

# @app.route("/add")
# def Add():
#     number1 = int(request.args["number1"]) 
#     number2 = int(request.args["number2"]) 
#     result = number1 + number2
#     return  render_template("add.html",number1=number1,number2=number2,result=result)

# @app.route("/login",methods=["POST","GET"])
# def Login():
#     if request.method == "POST":
#         username = request.form["name"]
#         return redirect(url_for("HelloUser",name=username))

#     return render_template("login.html")

# @app.route("/student", methods=["POST","GET"])
# def Student():
#     return render_template("student.html")

# @app.route("/result",methods=["POST"])
# def Result():
    # name = request.form["name"]
    # fizik = request.form["fizik"]
    # matematik = request.form["matematik"]
    # kimya = request.form["kimya"]
    # return render_template("result.html",name=name, fizik = fizik, matematik = matematik, kimya = kimya)
    ContextData = {
        "name":request.form["name"],
        "fizik":request.form["fizik"],
        "kimya":request.form["kimya"],
        "matematik":request.form["matematik"]
    }
    return render_template("result.html",**ContextData)