# Starting code

The starting code for this lecture is just a Flask app that renders a template, and the template itself.

```py
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def todo():
    return render_template("fizzbuzz.html")
```

You can also create an empty template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fizzbuzz</title>
</head>
<body>
  
</body>
</html>
```