import os
import functools
from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for,
)
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
# Secret key generated with secrets.token_urlsafe()
app.secret_key = "lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA"

users = {}


def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for("login"))

        return route(*args, **kwargs)

    return route_wrapper


@app.get("/")
def home():
    return render_template("home.html", email=session.get("email"))


@app.get("/protected")
@login_required
def protected():
    return render_template("protected.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email in users.keys():
            if pbkdf2_sha256.verify(password, users.get(email)):
                session["email"] = email
                return redirect(url_for("protected"))
        else:
            abort(401)
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = pbkdf2_sha256.hash(password)
        # session["email"] = email
        # - Setting the session here would be okay if you
        # - want users to be logged in immediately after
        # - signing up.
        flash("Successfully signed up.")
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.errorhandler(401)
def auth_error(error):
    return "Not authorized"
