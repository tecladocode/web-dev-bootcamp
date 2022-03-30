---
title: Adding a footer
slug: add-footer-movie-library-project
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to add a footer that is stuck to the bottom of the screen, or lower if the content of the page is taller.
draft: true
---


# Adding a footer to the movie watchlist project

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/08856f2be5b2491eb502b68c82214654](https://diff-store.com/diff/08856f2be5b2491eb502b68c82214654)
:::

Let's start by creating `templates/macros/footer.html`. Inside it, we'll place another Jinja macro that renders the footer HTML code:

```html
{% macro footer() %}
<footer class="footer">
    <small>Copyright &copy;2022. Movies Watchlist. All rights reserved.</small>
</footer>
{% endmacro %}
```

As you can see, nothing too complicated. The `&copy;` text will get replaced by the browser and display as a copyright symbol.

The `small` element tells the browser or screen reader that the text is smaller and less important, and it's inside a `footer` element.

Let's style the footer next, inside `main.css`

```css
.footer {
  padding: 1rem 0;
  color: var(--text-muted);
  text-align: center;
}
```

Simply, here we set some padding and the text color to be a light gray. We also align the text so it is in the centre of the footer.

Remember that `footer` elements are block-level elements, so they take up 100% of the width of their container. In this case, this will be placed inside the `body` of the page, which takes 100% of the width of the page--so the footer will be full-width.