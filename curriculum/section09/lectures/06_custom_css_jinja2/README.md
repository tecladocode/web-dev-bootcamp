---
title: Custom CSS for each Jinja template using inheritance
slug: custom-css-jinja-template-inheritance
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: 'Learn how to apply different CSS to each of your Jinja templates in a very straightforward way, by using inheritance.'
draft: false
---

- [Custom CSS for each Jinja template using inheritance](#custom-css-for-each-jinja-template-using-inheritance)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Custom CSS for each Jinja template using inheritance

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/3feb8bc5492849c182629df53776a768](https://diff-store.com/diff/3feb8bc5492849c182629df53776a768)
:::

Let's create another `block` in our base template so that we can change things there per template. In this video I'll show you how you can use that together with `style` tags to customize the CSS easily.

I'll also show you how you can leverage Jinja conditionals to make the CSS dynamic!

## Code at the start of this lecture

Available at the `start` folder.

## Code written in this lecture

First, let's modify the `base.html` template so it has one extra `block` inside the `head` tag:

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title or "Todos" }}</title>
  {% block head %}
  {% endblock %}
</head>
```

Now in each template we can create that block and place whatever we want.

Put simply, we could create separate CSS files for each template and include them there, or we could write the styles inline.

Writing the styles inline is generally discouraged because things can get pretty messy, but for small, simple applications it can actually make development quicker and easier.

Let's see how that could be done.

### `not-found.html` <!-- omit in toc -->

I'll start with the `not-found.html` template since the styles here are simpler. At the moment we've just got the `content` block, like this:

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Not found</h1>
  <p>We're sorry, that todo item was not found:</p>
  <p class="notfound">{{ text }}</p>
{% endblock %}
```

But now we can also define a `head` block. Inside it we'll put a `style` tag, with our CSS styles.

I'll also add a class to the last `p` tag so that we can target it with CSS:

```html
{% extends 'base.html' %}

{% block head %}
  <style>
    .notfound {
      background-color: gray;
      font-size: 125%;
    }
  </style>
{% endblock %}

{% block content %}
  <h1>Not found</h1>
  <p>We're sorry, that todo item was not found:</p>
  <p class="notfound">{{ text }}</p>
{% endblock %}
```

### `todo.html` <!-- omit in toc -->

The styles here can be more complicated, because we can leverage Jinja conditionals to get different styles depending on whether the todo is completed or not.

This is something you can do when inlining the CSS styles, but you can't do it very easily if you had separate CSS files for each template:

```html
{% block head %}
  {% if completed %}
    <style>
      p {
        margin: 8px 16px;
        background-color: aquamarine;
        padding: 12px 24px;
        border: 1px solid black;
        border-radius: 4px;
      }
    </style>
  {% else %}
    <style>
      p {
        margin: 8px 16px;
        background-color: darkred;
        color: white;
        padding: 12px 24px;
        border: 1px solid black;
        border-radius: 4px;
      }
    </style>
  {% endif %}
{% endblock %}
```

## Final code at the end of this lecture

Available at the `end` folder.
