from flask import Flask, render_template

app = Flask(__name__)
items = [
    {
        "name": "Chair",
        "stock": 3,
        "price": 156.79,
        "supplier": "Wood Manufacturing Ltd"
    },
    {
        "name": "Table",
        "stock": 1,
        "price": 1799.0,
        "supplier": "Standing Desks Ltd"
    },
    {
        "name": "Pen",
        "stock": 7,
        "price": 3.99,
        "supplier": "Pens & Company"
    },
]

@app.route("/")
def home():
    return render_template(
        "home.j2",
        address="23 No Name Street",
        employees=["Rolf", "Bob", "Anne"],
        all_items=items
    )


@app.route("/items")
def home():
    return render_template("items.j2", all_items=items)