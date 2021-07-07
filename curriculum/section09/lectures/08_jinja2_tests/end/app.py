from flask import Flask, render_template


app = Flask(__name__)


def divisibleby(value, other):
    return value % other == 0


app.jinja_env.tests["divisibleby"] = divisibleby


@app.route("/")
def todo():
    return render_template("fizzbuzz.html")
