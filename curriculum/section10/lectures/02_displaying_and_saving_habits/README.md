---
title: Displaying and saving habits
slug: displaying-and-saving-habits
tags:
  - Recorded
  - How to
categories:
  - Video
section_number: 10
excerpt: "In this lecture we allow users to add new habits and display the habits they've already added to the database."
draft: true
---

# Displaying and saving habits

[[toc]]

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/18ad1f56e51d4239bc2ac024b877ae68](https://diff-store.com/diff/18ad1f56e51d4239bc2ac024b877ae68)
:::

Let's start off our project by allowing users to add new habits and display the habits they've already added to the database.

This will be relatively simple, and will be done in two pages.

One will display all the items in a Python list. The other will contain a form that, when submitted, will add a new item to that list.

We'll also add a simple navigation bar so that users can switch between the two pages easily.

## Code written in this lecture

### The layout header

Let's start off by working on that nav bar! That'll make developing the other two pages easier:

```diff
--- templates/layout.html
+++ templates/layout.html
@@ -13,6 +13,10 @@
     
     <body>
         <header class="header">
+            <h1 class="header__logo"><a href="{{ url_for('index') }}" class="header__link">Habits</a></h1>
+            {% if "add" not in request.endpoint %}
+                <a href="{{ url_for('add_habit') }}" class="header__link">+ Add new</a>
+            {% endif %}
         </header>
 
         <main class="main">
```

Here I've gone into the `header` element and added an `h1` with a link to the homepage, and another link to the `add_habit` page.

That second link only displays if we don't have `"add"` in the current URL text. This is a _very_ crude way of filtering pages, but it will do for now. Another option would be to have two separate headers, and use either one or the other depending on the page you're on.

If you did that, you'd probably want to make the two headers into macros, and place them in the template for each page as needed.

### Displaying habits

Now that we've got that, we can go ahead and display the habits we've already got in our Python list.

To do this, we'll assume that the `index` endpoint is giving our template a list of strings: the habits to display.

Then inside the template, we can go ahead and simply loop over those strings and display them:

```diff
--- templates/index.html
+++ templates/index.html
@@ -1,6 +1,13 @@
 {% extends "layout.html" %}
 
 {% block main_content %}
-    <section>
+    <section class="habit-list">
+    {% for habit in habits %}
+        <div class="habit">
+            <p class="habit__name">
+                {{ habit }}
+            </p>
+        </div>
+    {% endfor %}
     </section>
 {% endblock %}
```

To do this I've made a `div` for each habit, and written the habit text (each string) into a `p` element.

### Adding habits

Next let's focus on adding new habits. We'll have a form in our `add_habit` page which sends our Flask app a string. 

Our Flask app will then receive it and add that string to the habits list.


```diff
--- templates/add_habit.html
+++ templates/add_habit.html
@@ -3,6 +3,8 @@
 {% block main_content %}
 
     <form class="form" method="POST">
+        <textarea class="form__input" id="habit" name="habit" rows="3" placeholder="Add a new daily habit"></textarea>
+        <button class="form__button" type="submit">Add</button>
     </form>
 
 {% endblock %}
```

### Tying everything together

The last piece of the puzzle is to code the Flask app that will receive user data and give it back to our `index` page.

I'll create a `habits` list which contains a list of all habits that have been added. I'll also put a test habit in there to begin with so that we can run our app without adding any habits ourselves.


```diff
--- app.py
+++ app.py
@@ -1,13 +1,17 @@
-from flask import Flask, render_template
+from flask import Flask, render_template, request
 
 app = Flask(__name__)
+habits = ["Test habit"]
 
 
 @app.route("/")
 def index():
-    return render_template("index.html", title="Habit Tracker - Home")
+    return render_template("index.html", habits=habits, title="Habit Tracker - Home")
 
 
 @app.route("/add", methods=["GET", "POST"])
 def add_habit():
+    if request.form:
+        habits.append(request.form.get("habit"))
+
     return render_template("add_habit.html", title="Habit Tracker - Add Habit")
```

In the `add_habit` page, it's important to only get the form data if there is any present. If there isn't any, then we'll just render the template.

With the flow we've got there, after submitting the form the user would once again see the template being rendered (but the form data submitted would be added to the habit list).

At this point you can run the app and see if it works!

::: tip
Every time you restart the app, added habits will disappear. That's just how Python works: the list is cleared when you terminate the app.

Later on we'll add a database so that the habits stick around between runs.
:::