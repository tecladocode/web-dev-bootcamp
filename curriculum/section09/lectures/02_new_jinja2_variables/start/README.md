# Starting code for this section

There's no starting code for this section! We'll be creating a small Flask app which you already know how to do:

```python
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def todo():
    return render_template("home.html", todos=["Get milk", "Learn programming"])
```

We'll make small changes to it throughout the section, but most of our work will be in the templates.