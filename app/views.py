from flask import  Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def Home():
    return "Flask Denemesi"

@app.route("/hello")
def Hello():
    return render_template("hello.html")

@app.route("/hello_user/<string:name>")
def HelloUser(name):
    if name.lower() == "admin":
        return redirect(url_for("HelloAdmin"))
    return render_template("hello_user.html")

@app.route("/hello_admin")
def HelloAdmin():
    return render_template("hello_admin.html")

@app.route("/hello/<name>")
def Hello_User(name):
    return render_template("hello.html",name=name)

@app.route("/add/<int:number1>/<int:number2>")
def Add(number1, number2):
    result = number1 + number2
    return  render_template("add.html",number1=number1,number2=number2,result=result)