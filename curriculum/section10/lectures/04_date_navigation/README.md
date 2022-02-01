---
title: Adding date navigation
slug: adding-date-navigation
tags:
  - Recorded
  - How to
categories:
  - Video
section_number: 10
excerpt: "Add a set of links at the top of the app to let the user go to the habits of a different date."
draft: true
---

# Adding date navigation

[[toc]]

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/ba9f5dd5fe6f41d589f1b39c867d3389](https://diff-store.com/diff/ba9f5dd5fe6f41d589f1b39c867d3389)
:::

Let's add the date navigator: a few links under the header that allow the user to go to a date a few days in the past or in the future, to check past habits or what they'll be doing the next day.

## Implementation

We're going to go about this lecture in a bit of a roundabout way, to make it easier to understand where we're going to end up. The final code for this lecture is at the very bottom of this article.

Let's begin by thinking about how we're going to make this date navigator.

We need the current date, as well as 3 days before today and 3 days after today. Each one of the dates should be clickable, and upon clicking it should take us to that date's page.

Let's start by making a function in the Flask side of things that, given any date, returns a list of 7 dates: 3 days before the given date, the given date, and 3 days after the given date:

```py
import datetime

...

def date_range(start: datetime.date):
    dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
    return dates
```

We'll pass this to our homepage's `render_template` call so it can use it to generate the date navigator. Later on we'll also pass it to every other page in our application, since the date navigator will be present everywhere.

```py
@app.route("/")
def index():
    return render_template(
      "index.html",
      habits=habits,
      title="Habit Tracker - Home",
      date_range=date_range
    )
```

So with that, let's go into the `index.html` template and create the date navigator. At the top of the `content` block, I'll add:

```html
<section class="dates">
    {% for date in date_range(selected_date) %}
        <a 
            class="dates__link {{ 'dates__link--current' if loop.index0 == 3 else ''}}"
            href="{{ url_for('index', date=date) }}"
        >
            <time class="date" datetime="{{ date }}">
                <span>{{ date.strftime("%a") }}</span>
                <span>{{ date.strftime("%d") }}</span>
            </time>
        </a>
    {% endfor %}
</section>
```

Although this looks complicated, there isn't much going on:

1. A loop that gives us each date in the list returned by `date_range`. We'll look at what the `selected_date` variable is in a moment.
2. An `a` element with `dates__link` class, and a `dates__link--current` class if it's the middle element of the loop.
3. A `time` element inside that which displays the date. This has a `datetime` attribute which contains the current date.

Note that the `a` element links to the `index` page, and passes a date. Let's go and implement that in the endpoint:

```py
@app.route("/")
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
        title="Habit Tracker - Home",
        date_range=date_range
    )
```

This now receives date strings. When Python turns a `date` object into a string (as we're doing in `url_for`), it uses ISO format. To turn it back into a date, we use `datetime.date.fromisoformat(date_str)`.

With this, our date navigator is done!

Every time we click a date, that calls the `index` endpoint with a date, which is then used to generate the date range around it when the template is re-rendered.

But, what if we wanted the date navigator to show up on the `add_habit` page too? And on every other page we make in the future?

It can be a bit cumbersome to pass the `date_range` argument to _every_ call of `render_template`.

That's where we can use a context processor to add the `date_range` function to all Jinja2 render calls. To do so, we write a function that returns a dictionary containing the `date_range` function. The parent function must be decorated so Jinja2 knows what it's for:

```py
@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}
```

This dictionary returned by `add_calc_date_range` is then merged with the rest of the Jinja2 context variables and made available across the board, every time we render a template.

This means we no longer have to pass the `date_range` function to `render_template`, and all our templates can use `date_range`.

Now that we've done this, I would move the date navigator over to `layout.html` instead of `index.html`.

```diff
--- templates/layout.html
+++ templates/layout.html
@@ -20,6 +20,20 @@
         </header>
 
         <main class="main">
+            <section class="dates">
+                {% for date in date_range(selected_date) %}
+                    <a 
+                        class="dates__link {{ 'dates__link--current' if loop.index0 == 3 else ''}}"
+                        href="{{ url_for('index', date=date) }}"
+                    >
+                        <time class="date" datetime="{{ date }}">
+                            <span>{{ date.strftime("%a") }}</span>
+                            <span>{{ date.strftime("%d") }}</span>
+                        </time>
+                    </a>
+                {% endfor %}
+            </section>
+
             {% block main_content %}
             {% endblock %}
         </main>
```

The `add_habit` endpoint needs to pass `selected_date` to `render_template` though, so that the date navigator knows where to start calculating:

```diff
 @app.route("/add", methods=["GET", "POST"])
 def add_habit():
     if request.form:
         habits.append(request.form.get("habit"))
 
-    return render_template("add_habit.html", title="Habit Tracker - Add Habit")
+    return render_template(
+        "add_habit.html",
+        title="Habit Tracker - Add Habit",
+        selected_date=datetime.date.today(),
+    )
```

And with that, we're done! Next up is styling the date navigator, because at the moment it doesn't look too good.

Below you can find the final code written in this lecture.

## Final code written in this lecture

```diff
--- templates/layout.html
+++ templates/layout.html
@@ -20,6 +20,20 @@
         </header>
 
         <main class="main">
+            <section class="dates">
+                {% for date in date_range(selected_date) %}
+                    <a 
+                        class="dates__link {{ 'dates__link--current' if loop.index0 == 3 else ''}}"
+                        href="{{ url_for('index', date=date) }}"
+                    >
+                        <time class="date" datetime="{{ date }}">
+                            <span>{{ date.strftime("%a") }}</span>
+                            <span>{{ date.strftime("%d") }}</span>
+                        </time>
+                    </a>
+                {% endfor %}
+            </section>
+
             {% block main_content %}
             {% endblock %}
         </main>
```

```diff
--- app.py
+++ app.py
@@ -1,12 +1,33 @@
+import datetime
 from flask import Flask, render_template, request
 
 app = Flask(__name__)
 habits = ["Test habit"]
 
 
+@app.context_processor
+def add_calc_date_range():
+    def date_range(start: datetime.date):
+        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
+        return dates
+
+    return {"date_range": date_range}
+
+
 @app.route("/")
 def index():
-    return render_template("index.html", habits=habits, title="Habit Tracker - Home")
+    date_str = request.args.get("date")
+    if date_str:
+        selected_date = datetime.date.fromisoformat(date_str)
+    else:
+        selected_date = datetime.date.today()
+
+    return render_template(
+        "index.html",
+        habits=habits,
+        selected_date=selected_date,
+        title="Habit Tracker - Home",
+    )
 
 
 @app.route("/add", methods=["GET", "POST"])
@@ -14,4 +35,8 @@
     if request.form:
         habits.append(request.form.get("habit"))
 
-    return render_template("add_habit.html", title="Habit Tracker - Add Habit")
+    return render_template(
+        "add_habit.html",
+        title="Habit Tracker - Add Habit",
+        selected_date=datetime.date.today(),
+    )
```

## Resources

- [For loop variables in Jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates/#for)