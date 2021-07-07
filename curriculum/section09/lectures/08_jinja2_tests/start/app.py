from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def todo():
    return render_template("fizzbuzz.html")
