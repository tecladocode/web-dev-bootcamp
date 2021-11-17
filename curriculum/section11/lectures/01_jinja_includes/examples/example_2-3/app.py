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
        "store.j2",
        name="My Store",
        address="23 No Name Street",
        employees=["Rolf", "Bob", "Anne"],
        items=items
    )


@app.route("/items")
def items():
    return render_template("items.j2", items=items)