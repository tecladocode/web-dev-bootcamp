---
title: Deploying our app to Heroku
slug: deploying-our-app-to-heroku
tags:
  - Recorded
  - How to
categories:
  - Video
section_number: 10
excerpt: Easily deploy the habit tracker project to Heroku.
draft: true
---

# Deploying our app to Heroku

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/b898d123dec44165a886b32b0ab599fe](https://diff-store.com/diff/b898d123dec44165a886b32b0ab599fe)
:::

Recap what we need in order to deploy a Flask app to Heroku: a GitHub repo, the `Procfile`, and `runtime.txt`.

Every Python app also needs `requirements.txt`: a file that contains the libraries the app needs in order to run. Heroku will install libraries from this file before running your app.

## Code written in this lecture

To deploy to Heroku, create a GitHub repo and upload your code.

We need to add two files to our repo:

### Procfile

The `Procfile` holds the command to run in order to start our app. It also holds the type of Dyno that our app will use.

```
web: gunicorn "app:create_app()"
```

We're using a `web` type of dyno, running the command `gunicorn "app:create_app()"`.

That runs the `create_app()` function inside `app.py`, and uses the resultant Flask app to pass to gunicorn, who can understand it and run it.

### Runtime

We need to tell Heroku what programming language to use. Here I'll write Python 3.9.6 because that's the version I was using at the time of writing.

If there's a later Python version, try your code with it locally first, and if it works, use it in Heroku as well.

More information available in the [Heroku Python runtimes page](https://devcenter.heroku.com/articles/python-support#supported-runtimes).

This is what my `runtime.txt` contains:

```
python-3.10.2
```

Add those two files to your GitHub repo, and then let's create a project in Heroku. Link it to your GitHub repo as we've already seen, and deploy the `main` branch.

If you have any issues, you can look through the Heroku logs to find what the problem is!