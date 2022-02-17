---
title: Making a 'login required' decorator
slug: flask-login-required-decorator
tags:
    - Written
    - How to
categories:
    - Video
section_number: 13
excerpt: "Make a decorator for Flask endpoints that redirects to the login page if the user isn't logged in."
draft: true
---

# Making a 'login required' decorator

Earlier this section we wrote a simple check in our `/protected` endpoint which acted as a gate for logged-out users.

If the user is not logged in, they are redirected to the login page. Otherwise, the rest of the route runs as normal.

This is such a common thing to do, that it's likely almost all your endpoints will have a check like that one:

```py
@app.get("/protected")
def protected():
    if not session.get("email"):
        abort(401)
    return render_template("protected.html")
```

## Writing the decorator

A decorator in Python is a function that acts on another function, extending it by running some code either before or after it.

I'd recommend learning about decorators in depth[^decorators_series_teclado] before continuing!

Here's what our decorator looks like:

```py
def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for("login"))

        return route(*args, **kwargs)

    return route_wrapper
```

And this is how we use it:

```diff
 @app.get("/protected")
+@login_required
 def protected():
     return render_template("protected.html")
```

With that, the `protected` function is _replaced by_ the `route_wrapper` function (although it keeps its name and docstring, if any):

```py
def route_wrapper(*args, **kwargs):
    if session.get("email") is None:
        return redirect(url_for("login"))

    return route(*args, **kwargs)
```

Note that `route(*args, **kwargs)` is calling what was previously the `protected` function. What we've done is extracted the log in check so that any of our endpoints can be decorated with `@login_required` so the check runs before anything else does in the endpoint.

[^decorators_series_teclado]: [How to write decorators in Python (The Teclado Blog)](https://blog.teclado.com/decorators-in-python/)