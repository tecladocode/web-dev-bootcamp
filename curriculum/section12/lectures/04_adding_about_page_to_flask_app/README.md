---
title: Adding an about page to our Flask app
slug: portfolio-add-about-page
tags:
    - Written
    - Project
categories:
    - Video
section_number: 12
excerpt: "In this lecture we'll add an 'about' page to our Portfolio project."
draft: true
---

# Adding an about page to our Flask app

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/af011a44b5aa42fcad724641709ecdd9](https://diff-store.com/diff/af011a44b5aa42fcad724641709ecdd9)
:::

Let's continue our Portfolio project by adding the "About" page. These are usually very simple, often with a photo and some text telling the reader about you.

We can start by writing the HTML:

```html
{% extends 'base.html' %}
{% block content %}
    <main class="main main--about">
        <p>
            Hi, I'm Bob! I love helping students learn to code and master software development.
            I've been teaching online for over 6 years, and I founded Teclado to bring software development to
            everyone—my objective is for you to truly understand everything that goes on behind the scenes.
        </p>
        <p>
            Coding is extremely rewarding. As you learn, things start to click and make sense.
            You can join the dots of all the things that weren't quite clear before.
            I'm here to make that journey quick and painless!
        </p>
        <p>
            I can help you with Python and JavaScript issues, particularly in web and backend development.
            I'm experienced with programming libraries and frameworks like Flask, React, React Native, and AngularJS.
            I've worked extensively with UNIX systems, MongoDB, PostgreSQL, and advanced system architecture design.
        </p>
    </main>
{% endblock %}
```

When writing HTML, you should try to keep it simple. This page is a good example of it!

Let's write the CSS next:

```css
.main {
  margin: 0 auto;
}

.main--about {
  max-width: 500px;
  padding: 0 1rem;
  line-height: 150%;
}
```

Here we set the maximum width to 500px, some padding, and center the whole block on the page with `margin: 0 auto`.

And that's about it! A super-simple "About" page. It doesn't need to be anything more complicated than this. Someone who is interested in your work will read a few paragraphs about you to get to know you better.
