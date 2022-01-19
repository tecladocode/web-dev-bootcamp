from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.jinja2")


@app.route("/about")
def about():
    return render_template("about.jinja2")


@app.route("/contact")
def contact():
    return render_template("contact.jinja2")
