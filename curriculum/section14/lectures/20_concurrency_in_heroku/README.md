---
title: Concurrency in Heroku
slug: concurrency-heroku-flask-apps
tags:
    - Not started
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to get Heroku to run multiple copies of your Flask app in a single dyno using gunicorn.
draft: true
---


# Concurrency in Heroku with gunicorn

Something you may not know about Python is that it is single-process and single-thread. That means that, under normal circumstances, a Python app can only receive a single user's request at a time, and therefore can only handle one user at a time in your app.

This is not as big a problem as you might think, because if your app responds to requests quickly (within about 100-200ms), then you can still handle many users at the same time. Remember that when users access your website, they're not all making requests constantly. Most people stay on each page for at least a few seconds in between requests.

However, when your number of concurrent users starts to grow (probably about 20-30), then it becomes more important to be able to handle more than one request at a time.

There are two ways to do this:

- Run two or more copies of your Flask app at once, so each app can handle one user; or
- Do something a bit crafty and try to handle more than one user at a time by:
    - Processing the response you'll send to a user while another user is sending you data (their request)
        - This way you could have many users sending you their requests, and you'd handle them as they complete, without having to wait for each request once it starts

The first method is what we'll be doing, as Flask doesn't support the second method. If you wanted to do the second method, you'd need to use something like FastAPI or Quart.

The good thing is that the first method is very good, very simple, and works well.

Running multiple Flask apps in a single dyno is no problem, because each app is small. One dyno can run between 2 and 4 Flask apps simultaneously before it starts to run into performance problems.

## How to enable concurrency in Heroku for your Flask apps

Set a config var `WEB_CONCURRENCY` with a value equal to the number of Gunicorn workers you'd like to run.

Your Dyno must be able to power all the workers you have running, so this is a balancing act. More workers will give you more simultaneous users that can access your app. Too many workers will crash your Dyno and force your app to restart, or make it so slow that it is unusable.

From the Heroku documentation[^heroku_gunicorn_docs]:

> Each forked system process consumes additional memory. This limits how many processes you can run in a single dyno. With a typical Django application memory footprint, you can expect to run 2–4 Gunicorn worker processes on a free, hobby or standard-1x dyno. Your application may allow for a variation of this, depending on your application’s specific memory requirements.

So that's it! When you set your config var, your dyno should automatically restart and run more than one Flask app at a time.

[^heroku_gunicorn_docs]: [Deploying Python Applications with Gunicorn (Heroku Dev Center)](https://devcenter.heroku.com/articles/python-gunicorn#basic-configuration)