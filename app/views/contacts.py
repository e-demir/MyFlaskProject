from app.controllers import GetCurrentUser, SaveContactRequest,GetContactList
from flask import Flask, render_template, url_for, redirect, request, Blueprint

bp = Blueprint(name="contacts", import_name=__name__, template_folder="../templates")

@bp.route("/contact", methods=["GET", "POST"])
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
            return redirect(url_for("contacts.Contact"))
    return render_template("contact.html", username=username, login_auth=login_auth)

@bp.route("/list")
def ContactList():
    username, login_auth = GetCurrentUser()
    contactList = GetContactList()
    return render_template("contact_list.html",username=username, login_auth=login_auth, contactList=contactList)