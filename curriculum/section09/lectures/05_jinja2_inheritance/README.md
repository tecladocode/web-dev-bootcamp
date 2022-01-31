---
title: Reducing code duplication using inheritance
slug: reducing-code-duplication-inheritance
tags:
  - How to
  - Published
categories:
  - Video
section_number: 0
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

- [Reducing code duplication using inheritance](#reducing-code-duplication-using-inheritance)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Reducing code duplication using inheritance

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/f5d286715a154b448343cbdce1318fd7](https://diff-store.com/diff/f5d286715a154b448343cbdce1318fd7)
:::

Instead of coding whole HTML documents in every Jinja template, we can code specific parts of a document and place them within a predefined HTML structure.

That way we don't have to rewrite parts of the HTML that may never change, such as the `html`, `head`, and `body` tags--and also HTML within those.

We use the `extends` keyword in Jinja2 as well as `block` to define the inheritance and the parts that will be replaced dynamically.

## Code at the start of this lecture

Every template in our starting code has the full HTML document, such as this one:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title or "Todos" }}</title>
</head>
<body>
  <h1>Not found</h1>
  <p>We're sorry, that todo item was not found:</p>
  <p>{{ text }}</p>
</body>
</html>
```

Something else interesting in the starting code is this part of `app.py`:

```py
@app.route("/<string:todo>")
def todo_item(todo: str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[]"
            title = f"{completed_text} - Todos"
            return render_template("todo.html", text=text, completed=completed, title=title)
    else:
        return render_template("not-found.html", text=todo, title="Not found")
```

Here we're taking a `todo` argument--the name of an item in our to-do list--and seeing if:

- It exists or not, rendering `not-found.html` if it isn't.
- It's completed or not, with content inside the `todo.html` template changing dynamically as needed.

## Code written in this lecture

Throughout the lecture we'll first create a `base.html` file that contains the HTML code that doesn't change per file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title or "Todos" }}</title>
</head>
<body>
  {% block content %}

  {% endblock %}
</body>
</html>
```

Note the `block` is used to dynamically place other Jinja code in there.

In every file where we just want to include a `block`, and nothing else, we can extend this `base.html` and define a new content block:

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Not found</h1>
  <p>We're sorry, that todo item was not found:</p>
  <p>{{ text }}</p>
{% endblock %}
```

It's important to note that we can have more than `block content`. We can have as many `block` as we want, and each one needs to have a unique name.

It's common to have a `block head` as well, that allows each page to add to the `head` part of the HTML whatever it needs.

## Final code at the end of this lecture

This is in the `end` folder. Every HTML file has `{% extends 'base.html' %}` and uses the `{% block content %}`.
