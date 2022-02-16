---
title: Logging in with Flask
slug: log-in-users-flask
tags:
    - Written
    - How to
categories:
    - Video
section_number: 13
excerpt: How to perform authentication (log in) using Flask.
draft: true
---

# Logging in with Flask

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/59e5830d277c44768f368b6807036f33](https://diff-store.com/diff/59e5830d277c44768f368b6807036f33)
:::

Logging in is extremely similar to signing up! The main (and only) difference is that we don't add the user data to our `users` dictionary.

All we do is populate the `session`, since that is what tells us the user is logged in.

This is what we're starting with:

```py
@app.route("/login")
def login():
    return render_template("login.html")
```

Just as we did with the `/signup` endpoint, we need to accept `POST` requests and handle them:

```py {1,3,4}
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    return render_template("login.html")
```

Then, we need to get the `email` and `password`, and see if they match what we have in our `users` dictionary:

```py {4-9}
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
    return render_template("login.html")
```

## Handling incorrect login details

There are two ways to handle incorrect login details:

1. Send the users to an error page that says "Unauthorized" or something along those lines; or
2. Be a bit more helpful and send the users back to the login page and show them a message to tell them what went wrong.

::: danger
If the e-mail or password are wrong, it's important you **don't say which one is wrong**. This is so that a malicious attacker can't keep guessing passwords for an e-mail they know exists.
:::

### Send the user to an error page due to incorrect login details

Super easy, all you do is use `abort` to raise an exception:

```py {10}
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
        abort(401)
    return render_template("login.html")
```

You can then catch with with `@app.errorhandler` as we did in [How to add error handling to a Flask app](/section12/lectures/10_add_error_handling_to_flask_app/).

### Re-render the form and show a message

A slightly better approach would be to use `flash()` to show an informative message.

This is better because the user then doesn't have to go _back to the login page_ from the error page:

```py {10}
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
        flash("Incorrect e-mail or password.")
    return render_template("login.html")
```

You could take this a step further and pass the email the user typed back to the form so it's already populated when the page refreshes:

```py {3,13}
@app.route("/login", methods=["GET", "POST"])
def login():
    email = ""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
        flash("Incorrect e-mail or password.")
    return render_template("login.html", email=email)
```

::: v-pre
This requires that we change the HTML form slightly also, adding `value="{{ email }}"`. This will put the `email` there if it's passed. If nothing is passed, then the field will remain empty.
:::

```html {5}
{% extends "base.html" %} {% block content %}
<form method="POST">
  <label>
    E-mail
    <input type="email" name="email" value="{{ email }}" />
  </label>
  <label>
    Password
    <input type="password" name="password" />
  </label>
  <input type="submit" value="Log in" />
</form>
<p><a href="{{ url_for('signup') }}">Sign up</a> instead</p>
{% endblock %}
```

Note that this doesn't tell the user the e-mail they typed is correct, but if it is then it makes it easier for them.