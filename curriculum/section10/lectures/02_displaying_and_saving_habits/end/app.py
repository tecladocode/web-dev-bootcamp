from flask import Flask, render_template, request

app = Flask(__name__)
habits = ["Bob"]


@app.route("/")
def index():
    return render_template("index.html", habits=habits, title="Habit Tracker - Home")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form:
        habits.append(request.form.get("habit"))

    return render_template("add_habit.html", title="Habit Tracker - Add Habit")
