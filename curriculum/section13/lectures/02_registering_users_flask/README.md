---
title: Register users with Flask
slug: register-users-flask
tags:
    - Written
    - How to
categories:
    - Video
section_number: 13
excerpt: Learn how to sign up (register) users with your Flask app.
draft: true
---

# Register users with Flask

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/9601b2eec48942b2a1a6357d079abf42](https://diff-store.com/diff/9601b2eec48942b2a1a6357d079abf42)
:::

## Overview of the starter code

In the starter code for this section we've got a simple Flask app with 4 routes and 4 templates:

- `/login` renders the log in form.
- `/signup` renders the sign up form
- `/protected` checks whether the user is logged in.
  - It returns an error page (401 Unauthorized) if the user isn't logged in.
  - It renders the `protected.html` template if the user is logged in.
- `/` renders the `home.html` template, which shows the information we've stored in the session.

At the moment we have the log in and sign up forms but we aren't handling them in the Flask app.

Let's start by handling the sign up form.

## How to handle user sign-ups in Flask

At its core, user signups are very straightforward:

1. Receive form data (username and password)
2. Add that to your database

That's it!

When users log in (we'll cover that in the next lecture), they will send you username and password again, and you'll check whether the username and password match what you've got in the database.

This can be made better by using [password encryption](../04_encrypt_passwords_passlib/README.md). More on that at the end of this section.

### `signup.html`

Inside `signup.html` we already have a form. I've written this code for you since you already know how forms work:

```html
{% extends "base.html" %}

{% block content %}
    <form method="POST">
    <label>
        E-mail
        <input type="email" name="email" />
    </label>
    <label>
        Password
        <input type="password" name="password" />
    </label>
    <input type="submit" value="Sign up" />
    </form>

    <p><a href="{{ url_for('login') }}">Log in</a> instead</p>
{% endblock %}
```

### Handling the signup form submission

At the moment the `/signup` endpoint only renders the template when a `GET` request is sent:

```py
@app.route("/signup")
def signup():
    return render_template("signup.html")
```

Let's make it so it can handle both `GET` and `POST` requests first:

```py {1}
@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")
```

Next, we'll add an `if` statement to check the `request.method`. If it's `POST`, we'll handle incoming form data. If it's `GET`, we'll just render the template as normal.

```py {1,7,8}
from flask import request

...

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        pass
    return render_template("signup.html")
```

Inside the `if` statement we'll get the form data using `request.form.get()`, and add it to our `users` dictionary:

```py {4-7}
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
    return render_template("signup.html")
```

::: tip
Here I'm using a **dictionary** to store my users instead of a list. That makes it easier to find a particular user if we have their e-mail.

With an email to password dictionary, finding a user is just a matter of doing `users.get(email)`.

By comparison, a list would require a for loop to go through all the items and it would be slower and more difficult to both write and read.
:::

### Should users be logged in immediately after signing up?

Now you can make a decision regarding whether to log in users immediately after signing up.

Normally, once you sign up a website, you are "logged in". After signing up you are redirected to your profile or your dashboard, and you don't have to log in again for a while.

In order to say that the user is "logged in", we need to store some data in the session for the browser that just signed up.

To do that, we use `flask.session`:

```py {1,12}
from flask import session

...

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        session["email"] = email
    return render_template("signup.html")
```

### Redirecting users after signing up

What should happen when a user signs up?

Like I mentioned above, normally you'd redirect the user to their profile or their dashboard.

Here we'll redirect users to the `/protected` endpoint. We will also use `flash` to make sure the user is told that they signed up correctly.

```py {1,14-15}
from flask import flash

...

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        session["email"] = email

        flash("Successfully signed up.")
        return redirect(url_for("login"))
    return render_template("signup.html")
```

## Flashing messages with Flask

When you use `flash()`, the string is stored in a queue until the queue is consumed.

How do you consume the queue?

Look at the queue contents, and the queue will be consumed. So all we have to do is display the messages to the user.

If you `flash` multiple messages, they will all go in the queue until they are all displayed, and then the queue will be emptied.

You can see we are consuming the queue contents in `base.html`:

```html
{% for message in get_flashed_messages() %}
    <div class="alert">
        <p>{{ message }}</p>
    </div>
{% endfor %}
```

This loop gets each message as a for loop, and creates a `div` element for each message. This does mean that if you have multiple messages, you'll create multiple divs and that can look a bit strange.

That's why it's best to use `flash` sparingly, just for single, important notifications to the user.