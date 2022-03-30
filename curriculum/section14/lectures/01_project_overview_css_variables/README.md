---
title: Project Overview and CSS Variables
slug: project-overview-css-variables
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Look at the movie watchlist project and the starter code files, as well as learn about CSS variables.
draft: true
---

# Project Overview and CSS Variables

Let's work on our final project: the movie watchlist!

In this project you will implement a full app that allows users to store movies they have or intend to watch. Each movie will have its own page with information about the movie, cast, and trailer. Also, users will be able give each movie a rating.

The app will have both light and dark mode, which users will be able to change with the click of a button.

At the end of the section we will also look at how you could take the project further by looking at how you could add features such as user comments or public user profiles.

We'll also use this section to introduce a very popular technology frequently used with Flask: WTForms. This is a library used for creating, validating, and rendering HTML forms. You'll learn how to use the library's components as well as create custom components.

[[toc]]

## Rundown of the project

Let's start by looking at the project design, and what users can do!

You can access the finished version of the project [here](https://movie-library-writing.herokuapp.com/). You can register with a fake e-mail and password if you'd like to try it, as there is no e-mail confirmation.

The design is simple and uses straight lines and a single accent colour. The font is Public Sans, a free, open-source font from Google Fonts.

### User signup and login

SIGNUP IMAGE

The user signup form has two password fields which must match. The validation matching is done in Flask using WTForms validators.

LOGIN IMAGE

The user login form only requires e-mail and password.

We will be hashing user passwords before storing them in the database.

### The movies list

Each user will have a list of movies that they've added. Every movie has a few properties, all of which (except the unique ID) are editable:

- `_id`, a UUID that we will generate.
- `title`, a string.
- `director`, a string.
- `year`, a number.
- `cast`, a list of strings (empty by default).
- `series`, a list of strings (empty by default)
- `tags`, a list of strings (empty by default)
- `last_watched`, a `datetime` object that the user can set to be the "current date".
- `rating`, a number between 0 and 5.
- `description`, a string.
- `video_link`, a string which is the YouTube embed link.

When movies are created, most of the properties are set to either `None`, `0`, or `[]`. That's because the "new movie" page only takes the title, director, and year:

NEW MOVIE PAGE

But users can then edit movies to add more details:

EDIT MOVIE PAGE

### Movie details, rating, and watch date

Each movie will have its own page, which shows all the movie data in the database:

MOVIE DETAILS PAGE

The rating stars are clickable. Upon clicking them, we will change the rating of the movie in the database.

GIF OF RATING CHANGE

Similarly, the "last watched date" is clickable. Clicking it sets the "last watched date" to today.

GIF OF WATCH DATE CHANGE

### Dark mode

In the navigation bar there is a button that users can click to switch between light mode and dark mode.

GIF OF CHANGING MODE

In each mode, the colours change, so we will be using CSS variables to greatly simplify our CSS styling in both modes.

## The starter CSS and CSS variables

Let's take a look at the CSS code that we are giving you as part of the starter code:

```css
:root {
  --text-dark: #000;
  --text-light: #fbf2f2;
  --text-muted: #595959;

  --background-color: #fff;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: #e5e5e5;

  --border: 3px solid #000;
}

.button {
  --background-color: #e2e8f0;
  --background-color-hover: #bdd1eb;
}

.form__field {
  --background-color: #e8e5e5;
}

.form__field,
.nav__link {
  --border: 3px solid #f56565;
}

html {
  /* Sets global font size on small devices */
  font-size: 12px;
}

/* When the screen width hits 960px, we increase the global font size to 14px. This changes
   the scale of all of our relative units (the rems), keeping everything in proportion */
@media screen and (min-width: 60em) {
  html {
    font-size: 14px;
  }
}

/* When the screen width hits 1200px, we once again increase the global font size, this time to 16px */
@media screen and (min-width: 75em) {
  html {
    font-size: 18px;
  }
}

body {
  /* Sets the shared font characteristics, so that that they can be inherited globally */
  font-family: "Public Sans", sans-serif;
  color: var(--text-dark);
  line-height: 1.45;
  background-color: var(--background-color);
}

/* Button styles that we'll share across our site */
.button {
  /* In order to easily position our buttons, we're making them block level elements */
  display: block;

  /* Removes any outlines added when the button is in focus */
  outline: none;

  /* Setting the cursor to pointer indicates to a user that the button is a clickable element */
  cursor: pointer;

  /* Again, with buttons we have to be explicit about inheriting font properties */
  font-size: inherit;
  font-family: inherit;

  /* Slows the background colour change effect when we hover over the button, making
       it take 0.1s with an accelerating colour change */
  transition: background 0.1s ease-in;
}

/* Utility class to use on links within text. */
.link {
  text-decoration: none;
  color: var(--accent-colour);
  white-space: nowrap;
}

.link:hover {
  text-decoration: underline;
}
```

We've added some comments in the code to explain why some CSS properties are there, but the main part is at the top:

```css
:root {
  --text-dark: #000;
  --text-light: #fbf2f2;
  --text-muted: #595959;

  --background-color: #fff;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: #e5e5e5;

  --border: 3px solid #000;
}

.button {
  --background-color: #e2e8f0;
  --background-color-hover: #bdd1eb;
}

.form__field {
  --background-color: #e8e5e5;
}

.form__field,
.nav__link {
  --border: 3px solid #f56565;
}
```

This doesn't actually change any of the targeted elements. Instead, it sets the values of CSS variables.

A CSS variable starts with `--`, and its value can then be accessed using `var(--variable-name)` (e.g. `var(--border)`).

Look at the `--border` variable, for example. It is defined under `:root` (the `html` element in most cases). That means that any element that is inside the `html` element will be able to access the `--border` variable, and retrieve the value `3px solid #000`. However, if we access the `--border` variable inside an element with class `.form__field` or `.nav__link`, then the value will be `3px solid #f56565`.

Doing this means that we only have to define values in one place in our application, which will make it easier to change them later on if we need to.

### CSS reset

I've also added a _CSS reset_ to the starter code. A CSS reset is a CSS file that changes certain properties in certain elements so that elements behave in a consistent way across browsers.

Also, some specific elements just behave differently from all other elements, and that can sometimes be confusing. A CSS reset usually makes all elements behave the same way. For example, `input` elements have `font: inherit` so that they don't use the default system font. Instead, they use the same font as the rest of the HTML.

This is the CSS reset:

```css
/*
  1. Use a more-intuitive box-sizing model.
*/
*,
*::before,
*::after {
  box-sizing: border-box;
}
/*
  2. Remove default margin
  - We added padding: 0 ourselves to remove unwanted padding (e.g. from lists)
*/
* {
  margin: 0;
  padding: 0;
}
/*
  3. Allow percentage-based heights in the application
*/
html,
body {
  height: 100%;
}
/*
  Typographic tweaks!
  4. Add accessible line-height
  5. Improve text rendering
*/
body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}
/*
  6. Improve media defaults
*/
img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}
/*
  7. Remove built-in form typography styles
*/
input,
button,
textarea,
select {
  font: inherit;
}
/*
  8. Avoid text overflows
*/
p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}
```

### Starter HTML

In the starter HTML, `layout.html`, I've linked the Public Sans font and the stylesheets provided, as well as set up the Jinja blocks for use in child templates:


```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>{{ title | default('Movie Watchlist') }}</title>
        <link href="https://fonts.googleapis.com/css?family=Public+Sans:400,600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/reset.css') }}" />
        <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />

        {% block head_content %} {% endblock %}
    </head>
    
    <body>
        <main class="main">
            {% block main_content %} {% endblock %}
        </main>
    </body>
</html>
```

I've created an `index.html` template too, which extends `layout.html`. It's basically empty at the moment.

## Our starter Python code

In `movie_library.__init__.py`, we have a `create_app()` function that should look very familiar to you! It connects to MongoDB and stores the `MongoClient` in the Flask app. It also sets the app secret key:

```py
import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient

from movie_library.routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )
    app.db = MongoClient(app.config["MONGODB_URI"]).get_default_database()

    app.register_blueprint(pages)
    return app
```

### `routes.py`

In `routes.py` I've created a very small `Blueprint`, since you already know how they work, so that we don't have to waste time setting it up:

```py
from flask import Blueprint, render_template


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )
```

### `requirements.txt` and `.flaskenv`

I've set up the `requirements.txt` with everything that we will need in this project:

```
flask
gunicorn
python-dotenv
flask-wtf
pymongo
passlib
```

Also, while developing a large project such as this one I would recommend you use a formatter (I use `black`), and a linter (I use `flake8`).

In the `.flaskenv` file you'll need this so that Flask can find the app and starts it in debug mode:

```
FLASK_APP=movie_library
FLASK_ENV=development
```

## Conclusion

That's it! I strongly recommend you follow along with me in this section, so download the starter code and get familiar with it!

Over the next 20-ish lectures we will be adding a lot of code and functionality to our app. Code with me, and enjoy this section. I'll see you in the next lecture!