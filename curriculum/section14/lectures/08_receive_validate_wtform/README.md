---
title: Receive and validate data using WTForms
slug: receive-validate-data-wtforms
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn to receive data from an HTML form and validate it using WTForms.
draft: true
---


# Receive and validate data using WTForms

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/37b94bc3a3344c27b45a6a4e93da36eb](https://diff-store.com/diff/37b94bc3a3344c27b45a6a4e93da36eb)
:::

## Validate form data
Now that we've got our form and our endpoint, it's time to connect them and receive the form data in Flask!

Doing so with Flask-WTF is very simple:

```py {5}
@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        pass

    return render_template(
        "new_movie.html", title="Movies Watchlist - Add Movie", form=form
    )
```

Instead of checking whether the `request.method` is `"POST"`, we're running a method of the `MovieForm` class: `validate_on_submit()`.

This does two things:

1. It checks that the form has been submitted (similar to doing `if request.method == "POST" and request.form`).
2. It runs validation on the form, and stores any errors back into the `form` object. It returns `True` if the validation yielded no errors.

So we will go into the `if` statement if the form was submitted and it validated without errors. Bingo!

Inside the if statement we can now grab the data and insert it into MongoDB.

## Insert movies into MongoDB
The simplest way to grab the form data and insert it into MongoDB would be to do something like this:

```py
import uuid
from flask import current_app, url_for  # amongst other things

...

@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = {
            "_id": uuid.uuid4().hex,
            "title": form.title.data,
            "director": form.director.data,
            "year": form.year.data
        }

        current_app.db.movie.insert_one(movie)

        return redirect(url_for(".index"))

    return render_template(
        "new_movie.html", title="Movies Watchlist - Add Movie", form=form
    )
```

And this would work just fine! However, there's one small issue.

We know that movies need to have more data in them than just `_id`, `title`, `director`, and `year`. We need to store genre, cast members, the last time we watched it, and a bunch more stuff!

So now is a good time to find a way to collect all the data about a movie in one place.

I think one of the best ways to do this is a `dataclass`. This is a Python object that is made for defining a cohesive group of data and interacting with it easily.

## Create a class for storing movie data
Let's start by creating a `movie_library/models.py` file. Inside it, we'll define a class that represents a movie.

::: tip
I made a diagram to help you visualize the change from dictionary to class for handling data and interacting with MongoDB. Hope it helps!

Link: [https://snappify.io/view/b0880dd5-59c8-4d4b-902b-ca26b1681bb2](https://snappify.io/view/b0880dd5-59c8-4d4b-902b-ca26b1681bb2)
:::

To "represent" a movie we'll define the properties of an object of said class, so that when we create an object, it will have all those properties.

Using the `dataclasses` module, you'd do it like this:

```py
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list)
    series: list[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0
    tags: list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None
```

This uses **type hinting** to define the field name and its data type. The `dataclasses` module then does a few things for you, such as define an `__init__` method, a `__repr__` method, and a few others.

You can think of data classes as a **code generation tool**. You give it the fields and types, and it generates a bunch of methods for you so you don't have to.

Two things that are especially important:

- Some fields have default values. This is so that we don't _have to_ pass in a value when we create the object. We must do this so when we create a new movie and don't have all its data yet, we are allowed to do so.
- Some fields have "fairly reasonable" default values, like `0` or `None`. Others have a value of `field(default_factory=list)`. This looks a bit weird, so let me explain.

### The `field` object and `default_factory`
When we want a bit more control over the default behaviour of fields in our data classes, we can use the `field` value.

This allows us to modify things such as:

- Whether the field should be included in the generated `__repr__` method
- Whether the field should expect a value in the `__init__` method
- Whether the field's value should be used for comparisons between objects of this dataclass
- A few other settings[^dataclass_field]

One of the things it also allows us to do is define a function as a default value, so that the function will run when the object is created, and the function's return value will be used as the value for the field.

This is necessary for when we want to define mutable values as the default value for the field.

If we did this:

```py
@dataclass
class Movie:
    cast: list[str] = []
```

Then this has a problem that isn't easy to spot!

The problem is that when you create two movie objects, they will both have **the same** list as a value for `cast`. When you modify one, the other will be modified too[^default_mutable_args].

To circumvent that, we create a different list for each field _when the object is created_:

```py
@dataclass
class Movie:
    cast: list[str] = field(default_factory=list)
```

This means that, when the object is created, it runs `list()`, which creates a new list, and assigns it to the field.

Because the list is created as part of the object initialisation, it won't be shared between two or more objects of the same class.

## Use the data model class for saving to MongoDB
Now that we've got our data class, let's use it in our endpoint!

All we have to do is import it:

```py
from dataclasses import asdict
from movie_library.models import Movie
```

And then in the endpoint we can create an object with the values:

```py {6-13}
@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie(
            _id=uuid.uuid4().hex,
            title=form.title.data,
            director=form.director.data,
            year=form.year.data,
        )

        current_app.db.movie.insert_one(asdict(movie))

        return redirect(url_for(".index"))
```

::: tip
Note that we are using `asdict(movie)` to turn the data class object into a dictionary. Handy!
:::

And that's it! The default values will go into MongoDB so we have some sensible data there for when we want to add that to the movie, and the code hasn't gotten much more complicated than using only dictionaries.

[^dataclass_field]: [`dataclasses.field` (Official Python Documentation)](https://docs.python.org/3/library/dataclasses.html#re-ordering-of-keyword-only-parameters-in-init)
[^default_mutable_args]: [Mutable default values (dataclasses, Official Python Documentation)](https://docs.python.org/3/library/dataclasses.html#mutable-default-values)