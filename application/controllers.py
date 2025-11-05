from flask import Flask, render_template, request, redirect, url_for
from flask import current_app as app
from application.models import *
from application.controllers import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        id = request.form["id"]
        username = request.form["username"]
        password = request.form["password"]
        user = Patient.query.filter_by(username = username).first()
        if id and user and user.password == password:
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid credentials")
        
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        
        email = request.form.get("email")
        password = request.form.get("password")

        new_user = Patient(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))