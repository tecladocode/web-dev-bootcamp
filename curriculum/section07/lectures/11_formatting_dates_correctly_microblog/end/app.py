import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

entries = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"),
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entries_with_date)
