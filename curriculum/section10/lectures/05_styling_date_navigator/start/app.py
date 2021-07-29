import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
habits = ["Test habit"]


@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}


@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template(
        "index.html",
        habits=habits,
        selected_date=selected_date,
        title="Habit Tracker - Home",
    )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form:
        habits.append(request.form.get("habit"))

    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        selected_date=datetime.date.today(),
    )
