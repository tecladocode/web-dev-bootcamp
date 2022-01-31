---
title: Creating new variables in Jinja2
slug: creating-variables-jinja2
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: Learn how to create variables within a Jinja2 template so you don't have to re-calculate values in multiple places.
draft: false
---

- [Creating new Jinja2 variables](#creating-new-jinja2-variables)
  - [TL;DR (on this video...)](#tldr-on-this-video)
  - [Lecture contents](#lecture-contents)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Creating new Jinja2 variables

## TL;DR (on this video...)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/925a06fbecaf46fd998785a731e18af3](https://diff-store.com/diff/925a06fbecaf46fd998785a731e18af3)
:::

Learn how to create variables inside a template, so that you can calculate values and re-use them in multiple places within a template.

```python
{% set my_variable = len(todos) %}
<p>You have {{ my_variable }} to-dos left.</p>
```

## Lecture contents

So far, we've learned that we can use variables in Jinja2 templates, as long as those variables are passed in by our Python code. Like this:

```python
@app.route("/todo")
def todo():
    return render_template("home.html", todos=["Get milk", "Learn programming"])
```

Then we can use the `todos` variable in the template:

```html
<ul>
{% for todo in todos %}
  <li>{{ todo }}</li>
{% endfor %}
</ul>
```

But did you know you can also create variables in a Jinja2 template?

```html
{% set friends = 50 %}
<p>You have {{ friends }} friends.</p>
```

It's not something we do very often, because usually in templates it's just easier to use the value rather than create a variable for it.

But there are some uses, such as when you're going to have to calculate a value multiple times.

Imagine we want to tell a user *how many* to-dos they have left to do:

```html
{% set num_todos = len(todos) %}
{% if num_todos > 0 %}
    <p>You have {{ num_todos }} things to do today.</p>
{% else %}
    <p>Nothing to do today. Relax!</p>
{% endif %}
```

The code won't run because we can't do `len(todos)` in Jinja2, but you get the idea.

Here we're creating a variable to hold the amount of to-dos so that we don't have to calculate it in two places: the if statement and the paragraph tag.

So... why can we not do `len(todos)`?

It's because Jinja2 isn't Python code, and the `len()` function doesn't exist in Jinja2.

Instead, we have to use Jinja2 filters. Let's talk about them in the next lecture.

## Code at the start of this lecture

We'll have `app.py` and `templates/home.html`.

Inside `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/todo")
def todo():
    return render_template("home.html", todos=["Get milk", "Learn programming"])
```

And inside `templates/home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Todos</title>
</head>
<body>
  <ul>
    {% for todo in todos %}
      <li>{{ todo }}</li>
    {% endfor %}
  </ul>
</body>
</html>
```

## Code written in this lecture

### Step 1

Here we talk about defining variables in Jinja2.

```html
{% set friends = 50 %}
<p>You have {{ friends }} friends.</p>
```

### Step 2

Here we talk about creating variables and what its purpose is.

```html
{% set num_todos = len(todos) %}
{% if num_todos > 0 %}
    <p>You have {{ num_todos }} things to do today.</p>
{% else %}
    <p>Nothing to do today. Relax!</p>
{% endif %}
```

## Final code at the end of this lecture

The code at the end of this lecture doesn't run, because we can't do `len(todos)` in Jinja2. We need to use a Jinja2 filter, which we'll talk about in the next lecture.

We'll have `app.py` and `templates/home.html`.

Inside `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/todo")
def todo():
    return render_template("home.html", todos=["Get milk", "Learn programming"])
```

And inside `templates/home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Todos</title>
</head>
<body>
  {% set num_todos = len(todos) %}
  {% if num_todos > 0 %}
    <p>You have {{ num_todos }} things to do today.</p>
  {% else %}
    <p>Nothing to do today. Relax!</p>
  {% endif %}
</body>
</html>
```
