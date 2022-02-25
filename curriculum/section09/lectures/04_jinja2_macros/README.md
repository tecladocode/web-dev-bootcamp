---
title: Simplifying your Jinja code with macros
slug: simplifying-jinja-code-macros
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: 'Jinja macros allow us to re-use blocks of Jinja code, including using arguments for better extensibility.'
draft: false
---

- [Simplifying your Jinja code with macros](#simplifying-your-jinja-code-with-macros)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Simplifying your Jinja code with macros

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/f906ce3bb3d3403eb179770ffeda0743](https://diff-store.com/diff/f906ce3bb3d3403eb179770ffeda0743)
:::

Another thing in Jinja similar to functions in Python, but here they're used for composition rather than transformation.

The process for using macros starts by extraction: extract some existing Jinja code into a macro so that you can call it from anywhere, and reuse it in multiple places.

```html
{% macro alert(title, message) %}
	<div class="alert alert-warning">
		<p class="alert__title">{{ title }}</p>
		<p class="alert__body">{{ message }}</p>
	</div>
{% endmacro %}
```

## Code at the start of this lecture

```html
{% set num_todos = todos | length %}
  {% if num_todos > 0 %}
      <p>You have {{ num_todos }} things to do today.</p>
      <ul>
        {% for text, completed in todos %}
          <li>{{ "[x]" if completed else "[ ]" }} - {{ text }}</li>
        {% endfor %}
      </ul>
  {% else %}
      <p>Nothing to do today. Relax!</p>
  {% endif %}
```

## Code written in this lecture

### Step 1

```html
{% macro todo_li(text, completed=False) %}
  <li>{{ "[x]" if completed else "[ ]" }} - {{ text }}</li>
{% endmacro %}

{% set num_todos = todos | length %}
  {% if num_todos > 0 %}
      <p>You have {{ num_todos }} things to do today.</p>
      <ul>
        {% for text, completed in todos %}
          {{ todo_li(text, completed) }}
        {% endfor %}
      </ul>
  {% else %}
      <p>Nothing to do today. Relax!</p>
  {% endif %}
```

### Step 2

```html
{% import 'macros.html' as macros %}
<!-- or -->
{% from 'macros.html' import todo_list %}

{% set num_todos = todos | length %}
  {% if num_todos > 0 %}
      <p>You have {{ num_todos }} things to do today.</p>

      {{ macros.todo_list(todos) }}
      <!-- or -->
      {{ todo_list(todos) }}
  {% else %}
      <p>Nothing to do today. Relax!</p>
  {% endif %}
```

## Final code at the end of this lecture

```html
{% import 'macros.html' as macros %}

{% set num_todos = todos | length %}
  {% if num_todos > 0 %}
      <p>You have {{ num_todos }} things to do today.</p>

      {{ macros.todo_list(todos) }}
  {% else %}
      <p>Nothing to do today. Relax!</p>
  {% endif %}
```
