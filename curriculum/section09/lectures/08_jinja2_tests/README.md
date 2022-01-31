---
title: What are Jinja2 tests?
slug: working-with-jinja2-tests
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: Learn about the 'is' keyword in Jinja2 and how to use it to write simple conditionals.
draft: false
---

- [What are Jinja2 tests?](#what-are-jinja2-tests)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
    - [Writing our own tests](#writing-our-own-tests)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# What are Jinja2 tests?

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/6a481a2959a8483b83b5415cdef3c981](https://diff-store.com/diff/6a481a2959a8483b83b5415cdef3c981)
:::

Jinja2 tests allow us to evaluate conditionals using the `is` keyword.

For example:

```html
{% set number = 10 %}

{% if number is even %}
  <p>It's even!</p>
{% endif %}
```

Tests can sometimes take arguments, in which case they can be called using brackets:

```html
{% set number = 10 %}

{% if number is divisibleby(2) %}
  <p>It's even!</p>
{% endif %}
```

However, as of Jinja2 v2.9, brackets are not necessary. I still like to use them though, I find it easier to read. That means this is fine:

```html
{% set number = 10 %}

{% if number is divisibleby 2 %}
  <p>It's even!</p>
{% endif %}
```

## Code at the start of this lecture

Available in the `start` folder. We've written a document in there to explain the starting code.

## Code written in this lecture

Let's start with our template. We're going to solve the Fizzbuzz problem using Jinja2.

What we want to do is iterate over the first 100 numbers, and then print one thing or another depending on the value.

If the value is divisible by 3 and 5, we print `FizzBuzz`. If it's only divisible by 3, we print `Fizz`. If it's only divisible by 5, we print `Buzz`.

If it's not divisible by any of them, we print the number out.

Let's start with our loop:

```html
<ul>
  {% for n in range(1, 101) %}
  <li>
    {{ n }}
  </li>
  {% endfor %}
</ul>
```

Here I've written an unordered list (with bullet points, so it's easier to see what numbers our code is creating). Using the `range()` function, which is available to us in Jinja2, we can iterate over the numbers from 1 to 100, both inclusive.

Then I'm creating `li` elements for each number.

Within the `li` we can use the `divisibleby` test in an if statement to check whether `n % 3 == 0` and `n % 5 == 0`.

Note that if we do this, we will be creating a bunch of empty bullet points for those numbers that aren't divisible, since we're no longer displaying the numbers themselves.

```html
<ul>
  {% for n in range(1, 101) %}
  <li>
    {% if n is divisibleby(3) and n is divisibleby(5) %}
      FizzBuzz
    {% endif %}
  </li>
  {% endfor %}
</ul>
```

We can fix that using an `else` statement so that we always display the number if the tests don't pass:

```html
<ul>
  {% for n in range(1, 101) %}
  <li>
    {% if n is divisibleby(3) and n is divisibleby(5) %}
      FizzBuzz
    {% else %}
      {{ n }}
    {% endif %}
  </li>
  {% endfor %}
</ul>
```

Finally, we can then use `elif` branches for the other tests:

```html
<ul>
  {% for n in range(1, 101) %}
  <li>
    {% if n is divisibleby(3) and n is divisibleby(5) %}
      FizzBuzz
    {% elif n is divisibleby(3) %}
      Fizz
    {% elif n is divisibleby(5) %}
      Buzz
    {% else %}
      {{ n }}
    {% endif %}
  </li>
  {% endfor %}
</ul>
```

### Writing our own tests

We can also very easily write our own tests. Let me show you how!

A test is a function that takes at least 1 argument: the value before `is`.

So let's say we want to define our own `square` test, that checks whether a number is a square--i.e. has an integer root.

We can do it like this:

```py
def square(value):
    return (value ** 0.5).is_integer()


app.jinja_env.tests["square"] = square
```

If we do this, all templates will have access to a test called `square` that they can use like this:

```html
{% if 10 is square %}
  <p>It's a square!</p>
{% endif %}
```

Note that we call this without brackets because the `value` argument gets it value from the `10` that comes before `is`.

If we want to be able to pass other values, such as in `divisibleby`, we can do it like this: Here's a re-implementation of the `divisibleby` test:

```py
def divisibleby(value, other):
    return value % other == 0


app.jinja_env.tests["divisibleby"] = divisibleby
```

You can create your own tests for checks you do frequently in your code, and for domain-specific checks to make your Jinja code more readable.

## Final code at the end of this lecture

Available in the `end` folder. 
