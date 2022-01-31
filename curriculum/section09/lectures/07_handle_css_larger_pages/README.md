---
title: How to handle CSS in larger pages
slug: handle-css-larger-pages
tags:
  - How to
  - Published
categories:
  - Video
section_number: 9
excerpt: 'When we start working on larger applications, having CSS styles in the HTML can become too cumbersome. In this lecture, let''s revisit BEM and how to use it!'
draft: false
---

- [How to handle CSS in larger pages](#how-to-handle-css-in-larger-pages)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code at the start of this lecture](#code-at-the-start-of-this-lecture)
  - [Code written in this lecture](#code-written-in-this-lecture)
  - [Final code at the end of this lecture](#final-code-at-the-end-of-this-lecture)

# How to handle CSS in larger pages

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/b95f3d07a8cd4a3aa02d1ce1f1a3844a](https://diff-store.com/diff/b95f3d07a8cd4a3aa02d1ce1f1a3844a)
:::

Using BEM and an external stylesheet (or more than one) is still the best way to go, for example by giving out `todo.html` paragraphs classes:

```html
{% if completed %}
    <p class="todo todo--completed">You've completed this todo! 🚀</p>
  {% else %}
    <p class="todo todo--pending">You haven't completed this yet. Why not do it now?</p>
  {% endif %}
```

However, in some pages that are self-contained and don't have elements which will be reused in other pages, it can be OK to have some inlined styles.

I would keep inline styles here for `not-found.html`:

```html
{% block head %}
  <style>
    .notfound {
      background-color: gray;
      font-size: 125%;
    }
  </style>
{% endblock %}
```

## Code at the start of this lecture

Available at `start`. The same as last lecture's `end` code.

## Code written in this lecture

The decision to go with inline styles vs. separate stylesheets is very much one of maintainability and reusability.

If you think the styles you create in a stylesheet will be used in multiple places, and they're getting longer or more complex, then it's worth separating them into their own stylesheet.

When the styles are simple or they're only used in one place, then keeping them inline can be acceptable.

It very much comes down to personal preference!

I'll start with giving my elements classes following the BEM convention. The block will be called `todo` and it will have a modifier, either `--completed` or `--pending`:

```html
{% if completed %}
    <p class="todo todo--completed">You've completed this todo! 🚀</p>
  {% else %}
    <p class="todo todo--pending">You haven't completed this yet. Why not do it now?</p>
  {% endif %}
```

Then we can go to `base.html` and link a stylesheet that will be used in all templates:

```html
<link rel="stylesheet" href="/static/css/style.css" />
```

We can then create the `static` top-level folder, and a `css` folder inside it, and `style.css` inside that.

We'll give the `.todo` block all the shared styles between the completed and pending todos:

```css
.todo {
  margin: 8px 16px;
  padding: 12px 24px;
  border: 1px solid black;
  border-radius: 4px;
}
```

Then we can define the modifiers below it, only changing those properties that differ:

```css
.todo--completed {
  background-color: aquamarine;
}

.todo--pending {
  background-color: darkred;
  color: white;
}
```

That's everything, but remember you can always go into `not-found.html` and do something similar.

We could remove the inline style, and add it to the CSS file.

There's also one more thing that can be a factor when deciding to go with inline vs. stylesheet: caching.

If your HTML document has a lot of inline styles, then it'll be a bigger size. When users request it, they'll have to download the code in order to run it. If the code is bigger, it'll take them longer to download.

This is also true for the CSS stylesheet. If you have all your styles in a single sheet, it'll be bigger and take longer to download.

However, once the stylesheet has been downloaded, browsers will cache it so that on subsequent requests it won't be downloaded again. This can speed up your website.

So all in all:

If your inline style is used in one place, is simple, and is small in size (simplicity and size will usually go hand in hand), then that's OK.

For anything else, use the stylesheets.

And before you ask, it's OK to have multiple separate stylesheets--such as `style.css`, `menu.css`, and `typography.css`. It'll take a bit longer to load initially, but when they're cached the page load times will be identical to having them all in one page.

## Final code at the end of this lecture

Available at the `end` folder. For the sake of example we're keeping inline styles in `not-found.html`, and using the stylesheet in `todo.html`.
