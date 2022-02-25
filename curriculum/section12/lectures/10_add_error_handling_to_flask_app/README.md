---
title: How to add error handling to a Flask app
slug: error-handling-flask-app
tags:
    - How to
    - Written
categories:
    - Video
section_number: 12
excerpt: "In this lecture we look at adding error handling to a Flask app using the @app.errorhandler syntax."
draft: true
---

# How to add error handling to a Flask app

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/ebafb589868c46dc947fc522930b5423](https://diff-store.com/diff/ebafb589868c46dc947fc522930b5423)
:::

Adding error handling to a Flask app is fairly straightforward when we use the `@app.errorhandler` decorator.

Let's add this to our `__init__.py`:

```py
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
```

This function is like a normal Flask route, but it only triggers when we raise an exception of type `HTTPException` with a response code of `404`.

If we define an `errorhandler(500)`, then that will also trigger when there is an uncaught exception in our code.

Flask provides the `abort()` function, which is a shorthand for raising an `HTTPException` with a given response code. Therefore, `abort(404)` will trigger this error handler.

Now let's create the `404.html` template so that we can show our users a nicer error page:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Bob Smith | Portfolio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}" />
</head>

<body>
    <main class="main main--error">
        <h1>404 - Page Not Found</h1>
        <p>
            Sorry, we couldn't find the page you're looking for.
            It may have been mis-spelled, or it doesn't exist anymore.
        </p>
        <a href="{{ url_for('home') }}">Go to home</a>
    </main>
</body>

</html>
```

Notice I'm not extending `base.html` here because I don't want the navbar showing up in the error page, but feel free to change this!