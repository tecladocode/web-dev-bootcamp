---
title: Add user logins
slug: add-user-login-movie-watchlist
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to allow users to log in by adding it to the movie watchlist project.
draft: true
---


# Adding user logins to the movie watchlist

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/de666ee57fea4e4ead460380608dfc2f](https://diff-store.com/diff/de666ee57fea4e4ead460380608dfc2f)
:::

## Creating the login form

Let's start by creating a WTForms form for user logins. Similar to the registration form, but we don't need the password confirmation field or as much validation. In `forms.py`:

```py
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")
```

## Rendering the login form

Then let's go to `routes.py` and work on displaying the form and logging users in when we receive the form data:

```py
from movie_library.forms import LoginForm  # among others


@pages.route("/login", methods=["GET", "POST"])
def login():
    if session.get("email"):
        return redirect(url_for(".index"))

    form = LoginForm()

    if form.validate_on_submit():
        user_data = current_app.db.user.find_one({"email": form.email.data})
        if not user_data:
            flash("Login credentials not correct", category="danger")
            return redirect(url_for(".login"))
        user = User(**user_data)

        if user and pbkdf2_sha256.verify(form.password.data, user.password):
            session["user_id"] = user._id
            session["email"] = user.email

            return redirect(url_for(".index"))

        flash("Login credentials not correct", category="danger")

    return render_template("login.html", title="Movies Watchlist - Login", form=form)
```

At this point, we can also change the `register` endpoint to redirect users to the `login` endpoint when registration is successful:

```diff
         current_app.db.user.insert_one(asdict(user))

         flash("User registered successfully", "success")

-        return redirect(url_for(".index"))
+        return redirect(url_for(".login"))

     return render_template(
         "register.html", title="Movies Watchlist - Register", form=form
     )
```

## Creating the login template

The login template is very similar to the register template:

```jinja2
{% from "macros/fields.html" import render_text_field %}

{% extends "layout.html" %}

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/forms.css') }}" />
{% endblock %} 

{% block main_content %}

    <form name="login" method="post" novalidate class="form">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {%- for category, message in messages %}
                <span class="form__flash form__flash--{{category}}"> {{ message }}</span>
            {% endfor %}
        {% endwith %}

        <div class="form__container">
            {{ form.hidden_tag() }}
    
            {{ render_text_field(form.email) }}
            {{ render_text_field(form.password) }}
    
            <span class="form__small">
                Don't have an account? <a href="{{ url_for('pages.register') }}" class="form__link">Register here</a>.
            </span>
    
            <div>
                {{ form.submit(class_="button button--form") }}
            </div>
        </div>
    </form>

{% endblock %}
```

Note that at this point, we've added the same message flashing code to two templates. You could move it to the `layout.html` template if you wish, although that will show these messages in all other templates.

If that makes sense for your app, then do that! For us, we'll keep this logic only in these two templates so I'm okay with this duplication. Any more though, and I'd be looking to making some changes to our template structure. For example, you could create a template that is almost identical to `layout.html`, but has message flashing. Then the login and register templates could extend that template instead of `layout.html`.

## Linking to the login endpoint across the app

There are two places where we want to link to the login endpoint: `macros/nav.html` and `register.html`.

In `macros/nav.html`:

```diff
 {%- if not email %}
     <a
-        href="#"
-        class="nav__link"
+        href="{{ url_for('pages.login') }}"
+        class="nav__link {{ 'nav__link--active' if request.path == url_for('pages.login') }}"
     >
         <span class="nav__item">Log in</span>
     </a>
     <a
         href="{{ url_for('pages.register') }}"
         class="nav__link {{ 'nav__link--active' if request.path == url_for('pages.register') }}"
     >
         <span class="nav__item">Register</span>
     </a>
 {% else %}
```

And in `register.html`:

```diff
 <div class="form__container">
     {{ form.hidden_tag() }}
 
     {{ render_text_field(form.email) }}
     {{ render_text_field(form.password) }}
     {{ render_text_field(form.confirm_password) }}
 
     <span class="form__small">
-        Already have an account? <a href="#" class="form__link">Log in here</a>.
+        Already have an account? <a href="{{ url_for('pages.login') }}" class="form__link">Log in here</a>.
     </span>

     <div>
         {{ form.submit(class_="button button--form") }}
     </div>
 </div>
```

And with that, we're done! We've added user logins to our application!

Congratulations in getting this far. You're really, almost done with a complete web app using Flask. The last few things are to add some personalization, and the ability to log out.