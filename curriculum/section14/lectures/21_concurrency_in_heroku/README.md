---
title: The lecture title goes here
slug: lecture-title
tags:
    - Not started
    - How to
categories:
    - Video
section_number: 0
excerpt: An excerpt of the lecture's content goes here.
draft: true
---

- [ ] Set metadata above
- [ ] Start writing!
- [ ] Create `start` folder
- [ ] Create `end` folder
- [ ] Write TL;DR
- [ ] Create per-file diff between `end` and `start` (use "Compare Folders")


# Lecture Title

Very easy: set a config var `WEB_CONCURRENCY` with a value equal to the number of Gunicorn workers you'd like to run.

Though your Dyno must be able to power all the workers you have running, so this is a balancing act. More workers will give you more simultaneous users that can access your app. Too many workers will crash your Dyno and force your app to restart, or make it so slow that it is unusable.

From the Heroku documentation[^heroku_gunicorn_docs]:

> Each forked system process consumes additional memory. This limits how many processes you can run in a single dyno. With a typical Django application memory footprint, you can expect to run 2–4 Gunicorn worker processes on a free, hobby or standard-1x dyno. Your application may allow for a variation of this, depending on your application’s specific memory requirements.

[^heroku_gunicorn_docs]