---
title: "Showing only the user's movies"
slug: showing-only-logged-in-user-movies
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: "Learn how to add personalization to our app by showing only the currently logged in user's movies."
draft: true
---


# Showing only the logged in user's movies

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/532c113cec1d48909a2f1fd0aec5d27e](https://diff-store.com/diff/532c113cec1d48909a2f1fd0aec5d27e)
:::

## Adding the `login_required` decorator

In the lecture on Adding a `login_required` decorator, in section 13, I said that the decorator code would come in handy in many future projects. This is one such project, so let's bring the decorator in to `routes.py`:

```py
import functools

...

def login_required(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        if session.get("email") is None:
            return redirect(url_for(".login"))

        return route(*args, **kwargs)

    return route_wrapper
```

Then we can use it to decorate a few of our endpoints:

- `index`
- `add_movie`
- `edit_movie`
- `watch_today`
- `rate_movie`

Remember that the `@login_required` decorator should be applied between the `@pages.route(...)` decorator and the `def function_name(...)` line.

## Adding movies to this user's movie list

Since we are going to require login before being able to add a movie, we will know the user that is making the request to the `add_movie` endpoint.

Since we know the user, we can add the newly-added movie to their profile by adding it to this user's `movies` list.

In the `add_movie` endpoint I'm adding these lines:

```py
current_app.db.user.update_one(
    {"_id": session["user_id"]}, {"$push": {"movies": movie._id}}
)
```

Using `session["user_id"]`, we can go directly into MongoDB, and use `$push` to add a new value to the `movies` list. Note that we didn't need to create a `User` object since all we need is already in the `session`.

## Showing only this user's movies in the `index`

At the moment our `index` endpoint does this to load movie data:

```py
movie_data = current_app.db.movie.find({})
```

Now want to load the user's data, and then check the user's movies and only load the movies in that list:

```py
user_data = current_app.db.user.find_one({"email": session["email"]})
user = User(**user_data)

movie_data = current_app.db.movie.find({"_id": {"$in": user.movies}})
```

Using `$in` with MongoDB only gives us movies whose `_id` property is one of the `user.movies`.

And with that, we've added personalization to our app. Instead of showing all movies to everyone, we only show this user's movies.

Note that we could add another endpoint to view _all movies added by all users_, and that would be identical to our `index` endpoint before we made changes. That would be useful if we wanted to allow comments or reviews for movies added by other users, for example.