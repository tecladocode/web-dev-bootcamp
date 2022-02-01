---
title: Adding Flask blueprints
slug: adding-flask-blueprints
tags:
  - Recorded
  - How to
categories:
  - Video
section_number: 10
excerpt: Learn how to add blueprints to an existing Flask application, and why you may want to do so.
draft: true
---
# Adding Flask blueprints

[[toc]]

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/ce6051701cc947e5b5f2626eaf95fa59](https://diff-store.com/diff/ce6051701cc947e5b5f2626eaf95fa59)
:::

A blueprint in Flask is basically a collection of routes. We can register zero or more blueprints with an application so that our routes can be split across different files and not all in `app.py`.

In the future, if we expand the app, adding more blueprints would also simplify route organization.

## Code written in this lecture

### Flask Blueprints

Let's start with the main reason why we're going to use blueprints: to separate route definition from app configuration.

In `app.py`, we'll just keep the barebones to create the Flask application. Later on, when we connect to MongoDB, we'll also put things like MongoDB secrets handling here.

The new `app.py` will look like this:

```py
from flask import Flask
from routes import pages


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)

    return app
```

Notice that we've added an import: `from routes import pages`. The `pages` variable is a Flask blueprint. Inside `create_app` we're registering the blueprint.

That makes all the endpoints defined inside the blueprint available to the Flask app.

In `routes.py` we'll begin by importing `Blueprint` from flask (along with our other imports), and creating the `Blueprint` object:

```py
import datetime
from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, url_for

pages = Blueprint(
    "habits", __name__, template_folder="templates", static_folder="static"
)
habits = ["Test habit"]
completions = defaultdict(list)
```

There's the `pages` variable we imported in `app.py`.

The first argument is the name of the blueprint. This is what we will refer to when we need the names of endpoint functions (more on that in a moment!).

The second argument is the import name, usually `__name__`.

Then we have a number of optional keyword arguments, such as the template folder or static asset folder. These can be different for each blueprint if we want, but they must be provided if we want the blueprint to be able to access templates or static assets.

For more information, see the [official documentation](https://flask.palletsprojects.com/en/2.0.x/api/#flask.Blueprint).

Every route in `routes.py` is then registered against the `pages` blueprint:

```py
@pages.route(...)  # or @pages.get(...), @pages.post(...)
```

So here's the finalised code in `routes.py`:

```py
import datetime
from collections import defaultdict
from flask import Blueprint, render_template, request, redirect, url_for

pages = Blueprint(
    "habits", __name__, template_folder="templates", static_folder="static"
)
habits = ["Test habit"]
completions = defaultdict(list)


@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}


@pages.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template(
        "index.html",
        habits=habits,
        selected_date=selected_date,
        completions=completions[selected_date],
        title="Habit Tracker - Home",
    )


@pages.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    date = datetime.date.fromisoformat(date_string)
    habit = request.form.get("habitName")
    completions[date].append(habit)

    return redirect(url_for(".index", date=date_string))


@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form:
        habits.append(request.form.get("habit"))

    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        selected_date=datetime.date.today(),
    )
```


When registering a blueprint we can also set a prefix so that all routes in that blueprint will share the same URL prefix:

```py
@app.register_blueprint(pages, url_prefix="/pages")
```

Then routes in our blueprint would be preceded by `/pages`:

- `/` becomes `/pages/`
- `/add` becomes `/pages/add`
- `/complete` becomes `/pages/complete`

### Using `url_for`

The `url_for` function takes a function name, and returns its route.

Now that we've got our functions inside blueprints, we need to provide both the blueprint name, and the function name to `url_for`, separated by a period (`.`).

For example:

```py
url_for("habits.index")
```

This is great because that means we can have functions with the same name in different blueprints, and we'll still be able to differentiate them.

However, when we are in a blueprint's route and we want to get to another route in the same blueprint, we can skip the blueprint name--but not the period!

We're using `url_for` in the `complete` function:

```py
@pages.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    date = datetime.date.fromisoformat(date_string)
    habit = request.form.get("habitName")
    completions[date].append(habit)

    return redirect(url_for(".index", date=date_string))
```


### Using blueprint endpoints in Jinja2

In our Jinja2 code we're also using `url_for`. We must remember to change those instances to use the required syntax.

In `index.html`:

```diff
--- templates/index.html
+++ templates/index.html
@@ -15,7 +15,7 @@
             </div>
         {% else %}
             <div class="habit">
-                <form method="POST" class="habit__form" action="{{ url_for('complete') }}">
+                <form method="POST" class="habit__form" action="{{ url_for('habits.complete') }}">
                 <input type="hidden" id="habitName" name="habitName" value="{{ habit }}" />
                 <input type="hidden" id="date" name="date" value="{{ selected_date }}" />
                 <button type="submit" class="habit__button">

```

And in `layout.html`:

```diff
--- templates/layout.html
+++ templates/layout.html
@@ -13,9 +13,9 @@
     
     <body>
         <header class="header">
-            <h1 class="header__logo"><a href="{{ url_for('index') }}" class="header__link">Habits</a></h1>
+            <h1 class="header__logo"><a href="{{ url_for('habits.index') }}" class="header__link">Habits</a></h1>
             {% if "add" not in request.endpoint %}
-                <a href="{{ url_for('add_habit') }}" class="header__link">+ Add new</a>
+                <a href="{{url_for('habits.add_habit')}}" class="header__link">+ Add new</a>
             {% endif %}
         </header>
 
@@ -24,7 +24,7 @@
                 {% for date in date_range(selected_date) %}
                     <a 
                         class="dates__link {{ 'dates__link--current' if loop.index0 == 3 else ''}}"
-                        href="{{ url_for('index', date=date) }}"
+                        href="{{ url_for('habits.index', date=date) }}"
                     >
                         <time class="date" datetime="{{ date }}">
                             <span>{{ date.strftime("%a") }}</span>
```

And with that, we're done adding blueprints to our application!