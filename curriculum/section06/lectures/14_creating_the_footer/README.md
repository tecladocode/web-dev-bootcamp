---
title: "Creating the Microblog footer"
slug: creating-the-microblog-footer
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Creating the Microblog footer

## Step 1

Start with a `footer` that contains everything (full-width, for the background color), and an inner `div` to hold the content.

```html
<footer class="footer">
    <div class="footer__content">
    </div>
</footer>
```

## Step 2

Inside it, we'll have two sections: a left (about the programmer) and a right (site info)

```html
<footer class="footer">
    <div class="footer__content">
        <section class="left">
        </section>
        <section class="right">
        </section>
    </div>
</footer>
```

## Step 3

We then add either `footer__item` directly, or inside another `div` which will serve as columns in the right-hand side.

Why not rows, instead of columns? The elements will be left-aligned within a column, and it's easier to separate them evenly using CSS later on rather than working with rows.

```html
<footer class="footer">
    <div class="footer__content">
        <section class="left">
            <a class="footer__item">Made by Jose Salvatierra</a>
            <a class="footer__item">Check out my other project</a>
        </section>
        <section class="right">
            <div class="footer__column">
                <a class="footer__item">Recent</a>
                <a class="footer__item">Calendar</a>
            </div>
            <div class="footer__column">
                <a class="footer__item">About</a>
                <a class="footer__item">How this was made</a>
            </div>
        </section>
    </div>
</footer>
```