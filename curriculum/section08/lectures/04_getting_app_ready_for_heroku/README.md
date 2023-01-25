---
title: Getting our app ready for Render
slug: getting-our-app-ready-for-render
tags:
  - Project
  - Published
categories:
  - Video
section_number: 8
excerpt: "Here we'll add some files that Render needs in order to run our application."
draft: false
---

- [Getting our app ready for Render](#getting-our-app-ready-for-render)

# Getting our app ready for Render

We need to add `gunicorn` to our `requirements.txt` file before we deploy to Render.

You won't be able to run `gunicorn` in Windows, but you can install it. In other platforms, you should be able to run `gunicorn`. Either way, you'll be using `flask run` to run your app locally most of the time. We'll only use `gunicorn` in Render.com for performance benefits.

