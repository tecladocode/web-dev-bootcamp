---
title: Making the Flask app for our project
slug: portfolio-flask-app
tags:
    - Written
    - Project
categories:
    - Video
section_number: 12
excerpt: In this lecture we start the Portfolio project by making the Flask app for it.
draft: true
---


# Making the Flask app for our project

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/014e90fa830a48b8b7fea88ddff11c77](https://diff-store.com/diff/014e90fa830a48b8b7fea88ddff11c77)
:::

So far we've been writing Flask apps using a very simple project structure:

```
project_folder
  | - app.py
  | - requirements.txt
  | - templates/
  | - static/
  | - ...
```

While this is a perfect structure for a simple, small app, when apps start to get a bit larger it can overpopulate the root folder. It's not a problem _per se_, but it can make it a bit more cumbersome to navigate your project if the root folder has dozens of files in it.

::: tip
When making a larger Flask app, you may have files for:

- Configuration
- Testing
- Multiple requirements files
- Environment variables
- Git-related configuration
- Markdown files for README and CONTRIBUTING
- And more!
:::

So it's fairly common to have this kind of structure in Flask apps:

```
project_folder
  | - .git                  # Git folder
  | - requirements.txt      # Requirements file(s)
  | - run.py                # Entry point to app
  | - config.py             # Global app configuration
  | - .venv                 # Virtual environment
  | - app/                  # Flask app code
      | - __init__.py       # App definition (previously, app.py)
      | - templates/
      | - static/
      | - views/            # Or views.py if not too long
      | - models/           # Or models.py if not too long
```

This way, your app source code is all within `app` (or an alternative name such as `portfolio` if that's your project name).

Any global code files, configuration, Git-related files, environment files, etc, will go in the top level.

## Creating our project structure

For this project, we'll create the following structure:

```
portfolio_project           # This is the root folder
  | - .flaskenv             # Flask-specific configuration
  | - .git                  # Git folder
  | - .venv                 # Virtual environment
  | - README.md             # Project description
  | - requirements.txt      # Requirements file
  | - requirements-dev.txt  # Development requirements
  | - portfolio/            # Flask app code
      | - __init__.py       # App definition
      | - templates/
      | - static/
```

::: warning Changes to code imports
It's important to note that, from now on, our imports will always be:

```py
from portfolio.whatever import what_we_need
```

And since our Flask `app` will be located inside `portfolio/__init__.py`, it can be accessed just like this:

```py
from portfolio import app
```
:::

## Coding our Flask app

The Flask part of this project is simple: one route for each page that we want to show, plus a single route for all the project pages.

```py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
```

The homepage doesn't have any information about the projects that it will display yet. We will work on that in a couple of lectures' time.

## Our template files

Let's also make some of the template files we'll need:

```
templates/
  | - base.html
  | - home.html
  | - about.html
  | - contact.html
```

These can be empty for now, we'll populate them as we go!

## Create the virtual environment

To finish the set-up, let's make our virtual environment.

Using your preferred Python version (I always recommend the latest version unless there is a compatibility issue with a specific library you want to use), do the below:

### On Mac OS (bash or zsh)

```
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### On Windows (cmd.exe)

```
/path/to/python.exe -m venv .venv
.venv\Scripts\activate.bat

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Conclusion

Now we've got all our requirements installed, we're ready to go on to the next lecture and start coding!