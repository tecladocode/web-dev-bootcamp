from flask import Flask, render_template

app = Flask(__name__)

items = [
    {"name": "Chair", "stock": 3},
    {"name": "Table", "stock": 1},
    {"name": "Pen", "stock": 7},
]


@app.route("/")
def home():
    return render_template(
        "store.html",
        name="My Store",
        address="23 No Name Street",
        employees=["Rolf", "Bob", "Anne"],
        items=items,
    )


@app.route("/items")
def items_list():
    return render_template("items.html", items=items)
