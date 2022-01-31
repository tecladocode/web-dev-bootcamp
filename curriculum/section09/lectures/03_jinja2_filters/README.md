---
title: Working with filters in Jinja2
slug: working-with-filters-jinja2
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: Filters in Jinja are similar to Python functions. Learn how they work in this lecture.
draft: false
---

- [Working with filters in Jinja2](#working-with-filters-in-jinja2)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Working with filters in Jinja2

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/1b9f968ca55a408ea6b352730f3a336d](https://diff-store.com/diff/1b9f968ca55a408ea6b352730f3a336d)
:::

In a nutshell, filters are to Jinja what functions are to Python. They take inputs, and return outputs. We use them where we use values, to transform them.

```python
{% set num_todos = todos | length %}
```

There are a lot of built-in filters!

- `capitalize()`
- `default()`
- `escape()`
- `first()`
- `format()`
- `groupby()`
- `join()`
- `last()`
- `length()`
- `reverse()`
- Lots more!
- Plus we can create our own (more on that later)

## Code at the start of this lecture

```html
{% set num_todos = len(todos) %}
{% if num_todos > 0 %}
    <p>You have {{ num_todos }} things to do today.</p>
{% else %}
    <p>Nothing to do today. Relax!</p>
{% endif %}
```

## Code written in this lecture

```html
{% set num_todos = todos | length %}
{% if num_todos > 0 %}
    <p>You have {{ num_todos }} things to do today.</p>
{% else %}
    <p>Nothing to do today. Relax!</p>
{% endif %}
```

We've already seen code that uses filters before:

```html
<article class="entry">
  <div>
    <h2 class="entry__title">{{ entry[0] | truncate(30, true) }}</h2>
    <time class="entry__date" datetime="{{ entry[1] }}">• {{ entry[2] }}</time>
  </div>
  <p class="entry__content">
    {{ entry[0] }}
  </p>
</article>
```

## Final code at the end of this lecture

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Todos</title>
</head>
<body>
  {% set num_todos = todos | length %}
  {% if num_todos > 0 %}
      <p>You have {{ num_todos }} things to do today.</p>
  {% else %}
      <p>Nothing to do today. Relax!</p>
  {% endif %}
</body>
</html>
```
