---
title: Getting our app ready for Heroku
slug: getting-our-app-ready-for-heroku
tags:
  - Project
  - Published
categories:
  - Video
section_number: 8
excerpt: "Here we'll add some files that Heroku needs in order to run our application."
draft: false
---

- [Getting our app ready for Heroku](#getting-our-app-ready-for-heroku)
  - [The `runtime.txt` file](#the-runtimetxt-file)
  - [The `Procfile` file](#the-procfile-file)
  - [Install `gunicorn` in Heroku](#install-gunicorn-in-heroku)

# Getting our app ready for Heroku

We need to tell Heroku:

- What language our app uses.
- How to run our app.
- The dependencies required for our app.

We do this with three different files:

- `runtime.txt`, for the language.
- `Procfile`, for "how to run the app".
- `requirements.txt`, for the dependencies.

## The `runtime.txt` file

Here we want to tell Heroku what language and what version to use.

The contents of this file are very specific. You need to pick from the available languages and versions here: [https://devcenter.heroku.com/articles/python-runtimes](https://devcenter.heroku.com/articles/python-runtimes).

In our case, we're going with this content inside the file:

```
python-3.10.2
```

::: tip
Other versions (e.g. older versions of Python) may also work. See this link for more information: https://devcenter.heroku.com/articles/python-support#supported-runtimes
:::

## The `Procfile` file

::: warning
The file should be called `Procfile`, and **not** `Procfile.txt`!
:::

Here we're going to tell Heroku how to run our app:

```
web: gunicorn "app:create_app()"
```

This uses the `web` dyno type, and in it executes the `gunicorn "app:create_app()"` command. That will start our app with `gunicorn` serving it.

## Install `gunicorn` in Heroku

We need to add `gunicorn` to our `requirements.txt` file before we deploy to Heroku.

You won't be able to run `gunicorn` in Windows, but you can install it. In other platforms, you should be able to run `gunicorn`. Either way, you'll be using `flask run` to run your app locally most of the time.