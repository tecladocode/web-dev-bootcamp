---
title: Routing between pages with Jinja
slug: routing-between-pages-with-jinja
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: 'Learn how to use url_for to get the endpoint for a given function name, which will simplify navigating between pages in your Flask apps.'
draft: false
---
- [Routing between pages with Jinja](#routing-between-pages-with-jinja)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# Routing between pages with Jinja

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/d57f52bee7a74e9991a8d26fad928011](https://diff-store.com/diff/d57f52bee7a74e9991a8d26fad928011)

Note that the code diffs are split into two. One implements a plain menu bar into the app (inside `/templates`), without using `url_for`.

The other implements navigation using `url_for`, and that's in `templates_urlfor`.
:::

Flask has a function that, given an endpoint's function name, will give us the URL. We can use that for routing in Jinja2 as well.

Let's say we've got these two endpoints in a Flask app:

```py
from flask import redirect, url_for

app = Flask(__name__)

account = None

@app.get("/homepage")
def home():
  return "Home"


@app.get("/profile")
def profile():
  if account:
    return "Profile"
  else:
    return redirect(url_for("home"))
```

Let's assume for a second that the `account` variable is what lets us check if the user has logged in or not.

In the second endpoint, if there is an `account`, then we return "Profile". But if there isn't, we'll redirect to the homepage.

Notice that we get the URL to redirect to with the `url_for("home")` function. This takes the function name for an endpoint--in this case, the function is called `home` and the endpoint is `/homepage`. It then returns the address to that function's endpoint, in this case, `/homepage`.

We could just type the string `"/homepage"` instead, but this has a few benefits:

- It becomes more useful as our apps become more complex.
- It works well with blueprints
- It means we can change endpoints later on, and as long as we keep the function names the same, our code will still work
- It's easy to pass arguments to the endpoint functions without having to think too much about query strings and things like that

So really in Flask, every time you have a link or a local address, you should be using `url_for` instead of hard-coding the URL.

## Code at the start of this lecture

The code is available in the `start` folder.

We've got a simple Flask app with a few sample pages:

- Home
- Login
- Signup

In each page we have a string that tells us what page it is.

In the Login and Signup pages, we also have a link to the other page (to Signup from Login, and to Login from Signup).

The links are using the standard method:

```html
<a href="/login">Log in instead?</a>
```

And there are no links on the homepage.

## Code written in this lecture

First, let's change the links in the Signup and Login pages to use `url_for`:

In the Signup page:

```diff
-<a href="/login">Log in instead?</a>
+<a href="{{ url_for('login') }}">Log in instead?</a>
```

And in the Login page:

```diff
-<a href="/signup">Sign up instead?</a>
+<a href="{{ url_for('signup') }}">Sign up instead?</a>
```

Then, let's also add a navbar to the base page. We could naturally do this using standard links, but we can also use `url_for`:

```html
<ul class="navigation">
  <li><a href="{{ url_for('home') }}">Home</a></li>
  <li><a href="{{ url_for('login') }}">Log in</a></li>
  <li><a href="{{ url_for('signup') }}">Sign up</a></li>
</ul>
```

Notice that we're using a CSS stylesheet, which is linked in the base page like so:

```html
<link rel="stylesheet" href="/static/css/styles.css">
```

We can also use `url_for` here, although the syntax is slightly different:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

Instead of passing just the endpoint name, we pass in `static`. This special name also accepts a `filename` argument which tells us which file to load from the `/static` URL. The final URL will be `/static/css/style.css`.

## Final code at the end of this lecture

This is available in the `end` folder.