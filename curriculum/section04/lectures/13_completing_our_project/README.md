---
title: Completing our project with document-level annotations
slug: completing-project-document-level-annotations
tags:
    - How to
    - Published
categories:
    - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Completing our project with document-level annotations

In this lecture, let's continue with our HTML project. Every HTML document needs some document-level annotations in the `head`.

This is the code we're starting with:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
        <p>This website's code looks like this:</p>
        <img class="code" src="code.png" alt="The HTML code for this page." />
    </body>
</html>
```

The first thing to do is add a `title` element. This is used by browsers, so users get a bit more information about the page, as well as by search engines so they know what a page is about:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Rolf Smith - Learning HTML</title>
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
        <p>This website's code looks like this:</p>
        <img class="code" src="code.png" alt="The HTML code for this page." />
    </body>
</html>
```

We usually also want to add some meta-information. For example, the [charset](https://www.w3.org/International/questions/qa-what-is-encoding) of the page. Normally we also want to add viewport information, which helps browsers resize the page correctly on different devices:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <title>Rolf Smith - Learning HTML</title>
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
        <p>This website's code looks like this:</p>
        <img class="code" src="code.png" alt="The HTML code for this page." />
    </body>
</html>
```

Finally, a quick sneak peek of what we'll be doing in the next section. We can link a CSS file in the `head` as well. Doing this means that the browser will try to load the CSS file when it loads the HTML document.

It will then try to apply the styles defined in the CSS file, into this document.

Create another file and call it `styles.css`. Then, add this line to link the CSS file with our HTML document:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <title>Rolf Smith - Learning HTML</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
        <p>This website's code looks like this:</p>
        <img class="code" src="code.png" alt="The HTML code for this page." />
    </body>
</html>
```

The CSS file is empty for now, but we'll be writing code in there throughout the next section!
