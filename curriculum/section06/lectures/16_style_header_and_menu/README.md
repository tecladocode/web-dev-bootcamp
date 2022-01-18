---
title: "How to style the header and menu bar"
slug: how-to-style-the-header-and-menu-bar
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# How to style the header and menu bar

First, create a new CSS file and link it:

```html
<link rel="stylesheet" href="styles.css" />
```

## Starting code

Nothing!

## Final code

```css
.navbar {
    max-width: 640px;
    margin: 50px auto;
    padding: 0 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    font-size: 24px;
}

.navbar__brand {
    display: flex;
    align-items: center;
}

.navbar__logo {
    margin-right: 30px;
}

.navbar__navigation {
    display: flex;
    flex-direction: row;
    align-items: center;
    list-style: none;
    color: #5C6B70;
}

.navbar__navigation-item {
    margin-left: 50px;
}

.navbar__link {
    text-decoration: none;
    color: inherit;
}
```