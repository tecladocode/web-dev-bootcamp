---
title: "Finishing the header and navigation"
slug: finishing-the-header-and-navigation
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Finishing the header and navigation

This is the code we've got in the header at the moment:

```html
<header>
    <img src="./logo.svg" alt="The Microblog Logo" />
</header>
```

In this lecture we'll continue writing the header, and add navigation links to it.

This is the final code:

```html
<header class="navbar">
    <div class="navbar__brand"><img class="navbar__logo" src="./logo.svg" />Microblog</div>
    <ul class="navbar__navigation">
        <li class="navbar__navigation-item"><a href="#" class="navbar__link">Recent</a></li>
        <li class="navbar__navigation-item"><a href="#" class="navbar__link">Calendar</a></li>
    </ul>
</header>
```