---
title: Completing habits
slug: completing-habits
tags:
    - Recorded
    - How to
categories:
    - Video
section_number: 10
excerpt: "Implement the habit completion functionality and work on the styling for it!"
draft: true
---

# Lecture Title

[[toc]]
## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/568e68ad5fd84f5faa9abdc938f9074c](https://diff-store.com/diff/568e68ad5fd84f5faa9abdc938f9074c)
:::

Let's add habit completion so that our users can complete habits on the day they've got currently selected.

As part of this, we'll also write some CSS to improve the look of habits in the `index` page.

## Code written in this lecture

There's a few things going on in this video!

Let's start by changing the `index.html` template. We're going to make it so that the template rendering gets a list of habits that were completed on the currently selected day, as well as the list of habits themselves.

With that, we can check each habit to see if it's in the `completions` list, which would tell us we've already completed it.

With that, we can do one of two things:

- If the habit has been completed, show the habit as normal, with a checkbox icon beside it.
- If the habit hasn't been completed, we'll change it slightly so it becomes a button that when clicked, marks the habit as complete for the day.

The tricky part is going to be to style the normal habit and the form so similarly that it's impossible to tell them apart.

You'll see what I mean by the time we're done!

The form contains a hidden field with the habit name, and another with the current date. That way when we submit the form we can still access the necessary data in the backend.

```diff
--- templates/index.html
+++ templates/index.html
@@ -3,11 +3,27 @@
 {% block main_content %}
     <section class="habit-list">
     {% for habit in habits %}
-        <div class="habit">
-            <p class="habit__name">
-                {{ habit }}
-            </p>
-        </div>
+        {% set completed = habit in completions %}
+        {% if completed %}
+            <div class="habit completed">
+                <p class="habit__name">
+                    {{ habit }}
+                </p>
+                <svg class="habit__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
+                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
+                </svg>
+            </div>
+        {% else %}
+            <div class="habit">
+                <form method="POST" class="habit__form" action="{{ url_for('complete') }}">
+                <input type="hidden" id="habitName" name="habitName" value="{{ habit }}" />
+                <input type="hidden" id="date" name="date" value="{{ selected_date }}" />
+                <button type="submit" class="habit__button">
+                        {{ habit }}
+                </button>
+                </form>
+            </div>
+        {% endif %}
     {% endfor %}
     </section>
 {% endblock %}
```

Now that we've got that, we can go ahead and code the Flask side of things.

We'll add a `completions` variable which is a `defaultdict` that maps dates to lists. Each list contains the habits completed on that date.

We'll then pass the completed habits to `render_template` in the `index` endpoint.

We'll also add the `complete` endpoint which handles the submission of the form (an incomplete habit). That adds it to the `completions` dictionary.

```diff
--- app.py
+++ app.py
@@ -1,8 +1,10 @@
 import datetime
-from flask import Flask, render_template, request
+from collections import defaultdict
+from flask import Flask, render_template, request, redirect, url_for
 
 app = Flask(__name__)
 habits = ["Test habit"]
+completions = defaultdict(list)
 
 
 @app.context_processor
@@ -26,8 +28,19 @@
         "index.html",
         habits=habits,
         selected_date=selected_date,
+        completions=completions[selected_date],
         title="Habit Tracker - Home",
     )
+
+
+@app.route("/complete", methods=["POST"])
+def complete():
+    date_string = request.form.get("date")
+    date = datetime.date.fromisoformat(date_string)
+    habit = request.form.get("habitName")
+    completions[date].append(habit)
+
+    return redirect(url_for("index", date=date_string))
 
 
 @app.route("/add", methods=["GET", "POST"])
```

```diff
--- static/css/main.css
+++ static/css/main.css
@@ -130,3 +130,53 @@
   flex-direction: column;
   align-items: center;
 }
+
+.habit {
+  display: flex;
+  flex-direction: row;
+  align-items: center;
+  justify-content: space-between;
+  font-size: 26px;
+  padding: 20px;
+  margin-bottom: 20px;
+  background-color: #fff2d8;
+  border: 3px solid black;
+  border-radius: 6px;
+}
+
+.habit:not(.completed) {
+  padding: 0;
+}
+
+.habit:not(.completed):hover {
+  background-color: #e9cd87;
+}
+
+.habit__icon {
+  width: 1em;
+  height: 1em;
+}
+
+.habit__name {
+  margin: 0;
+}
+
+.habit__form {
+  width: 100%;
+}
+
+.habit__button {
+  display: block;
+  width: 100%;
+  margin: 0;
+  padding: 20px;
+  font-family: inherit;
+  font-size: inherit;
+  text-align: left;
+  border: none;
+  background-color: unset;
+  cursor: pointer;
+}
```

## Resources

Code for the SVG "Completed" icon. Feel free to copy it into your code!

```html
<svg class="habit__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
</svg>
```