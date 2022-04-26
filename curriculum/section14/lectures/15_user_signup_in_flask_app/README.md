---
title: Add user signups
slug: add-user-signups-movie-watchlist
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to allow user signups to a Flask app by adding them to the movie watchlist project.
draft: true
---



# Adding user signups to the movie watchlist

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/2c2610d4766c41e099e677cde029e696](https://diff-store.com/diff/2c2610d4766c41e099e677cde029e696)
:::

In Section 13, we learned about user authentication in Flask apps, and now we're going to follow exactly what we did in that section to add user signups to our app. In the next lecture, we'll add user logins.

We will do one thing that we didn't cover in Section 13, which is to create a WTForms form for user signups. That's so validation is a bit easier, and we can add a "Confirm password" field in our form without much hassle.

Let's start there!

## Creating a WTForms form for user signups

There's not much new in this form, except for a couple of nice validators. In `forms.py`:

```py
from wtforms import PasswordField  # among others
from wtforms.validators import Email, EqualTo, Length  # among others


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(),
            Length(
                min=4,
                max=20,
                message="Your password must be between 4 and 20 characters long.",
            ),
        ],
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="This password did not match the one in the password field.",
            ),
        ],
    )

    submit = SubmitField("Register")
```

## Creating a User model to work with user data

Just as we did with the `Movie` model, let's create a `User` model so it's a bit easier for us to work with user data in our application.

In `models.py`:

```py
@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: list[str] = field(default_factory=list)
```

I'm adding a `movies` property here that will be a list of movie IDs. Every time a logged-in user adds a movie to our database, it will be linked to their user. Then when they want to see their movies, only movies that are in this list will be loaded.

## Rendering the form

Before we can do anything more, we must install `passlib`. Activate your virtual environment and run:

```
pip install passlib
```

To render our user signup form we'll create a new endpoint in `routes.py`.

Here we will:

1. Check the user isn't logged in already (i.e. the `session` is empty)
2. Create the `RegisterForm` object
3. Render `register.html` with the form object

```py
# new imports
from flask import flash
from movie_library.forms import RegisterForm
from movie_library.models import User
from passlib.hash import pbkdf2_sha256


@pages.route("/register", methods=["GET", "POST"])
def register():
    if session.get("email"):
        return redirect(url_for(".index"))

    form = RegisterForm()

    if form.validate_on_submit():
        pass

    return render_template(
        "register.html", title="Movies Watchlist - Register", form=form
    )
```

### Handling form submissions

When the user submits `register.html`, we will want to hash their password and add them to MongoDB. We already know how to do that, so let's add that in now:

```py
@pages.route("/register", methods=["POST", "GET"])
def register():
    if session.get("email"):
        return redirect(url_for(".index"))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            _id=uuid.uuid4().hex,
            email=form.email.data,
            password=pbkdf2_sha256.hash(form.password.data),
        )

        current_app.db.user.insert_one(asdict(user))

        flash("User registered successfully", "success")

        return redirect(url_for(".index"))

    return render_template(
        "register.html", title="Movies Watchlist - Register", form=form
    )
```

## The `register.html` template

This template just renders the form using our macros:

```jinja2
{% from "macros/fields.html" import render_text_field %}

{% extends "layout.html" %} 

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/forms.css') }}" />
{% endblock %} 

{% block main_content %}

    <form name="register" method="post" novalidate class="form">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {%- for category, message in messages %}
                <span class="form__flash form__flash--{{category}}"> {{ message }}</span>
            {% endfor %}
        {% endwith %}
        
        <div class="form__container">
            {{ form.hidden_tag() }}

            {{ render_text_field(form.email) }}
            {{ render_text_field(form.password) }}
            {{ render_text_field(form.confirm_password) }}
    
            <span class="form__small">
                Already have an account? <a href="#" class="form__link">Log in here</a>.
            </span>
    
            <div>
                {{ form.submit(class_="button button--form") }}
            </div>
        </div>
    </form>

{% endblock %}
```

## Adding a link to the registration endpoint in the navbar

The last thing to do is make sure users can actually navigate to our new endpoint!

Let's change `macros/nav.html`:

```diff
 {%- if not email %}
     <a
         href="#"
         class="nav__link"
     >
         <span class="nav__item">Log in</span>
     </a>
-     <a
-         href="#"
-         class="nav__link"
-    >
+    <a
+        href="{{ url_for('pages.register') }}"
+        class="nav__link {{ 'nav__link--active' if request.path == url_for('pages.register') }}"
+    >
         <span class="nav__item">Register</span>
     </a>
 {% else %}
```

Note I'm making this the active page using `.nav__link--active`, just as we did for the movies list, when the user is in this page.

And that's it! We've added user signups to our app. When they register, they'll get added to MongoDB. Next up, logging in!