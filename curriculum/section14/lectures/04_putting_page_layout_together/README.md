---
title: Putting the page layout together
slug: complete-page-layout-movie-watchlist
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Put together the page layout, including the navigation, main content, and footer.
draft: true
---


# Putting the page layout together

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/f3d05e2353764824a91003cbfd8aecd9](https://diff-store.com/diff/f3d05e2353764824a91003cbfd8aecd9)
:::

Now that we've got our header navigation and our footer, it's time to add them to `layout.html`.

We will also need to add some styling so that the footer is pushed up against the bottom of the page, even if the page content is small.

Let's start at `layout.html`, and import and call our macros:

```jinja2 {1,2,19,25}
{% from "macros/nav.html" import header %}
{% from "macros/footer.html" import footer %}

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="X-UA-Compatible" content="ie=edge" />
        <title>{{ title | default('Movie Watchlist') }}</title>
        <link href="https://fonts.googleapis.com/css?family=Public+Sans:400,600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/reset.css') }}" />
        <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />

        {% block head_content %} {% endblock %}
    </head>
    
    <body>
        {{ header(session.get("email"), session.get("theme")) }}

        <main class="main">
            {% block main_content %} {% endblock %}
        </main>
        
        {{ footer() }}
    </body>
</html>
```

Now that we've got this, we can go ahead and work on our styling.

The first thing we want to do is use `flex` on the `body`:

```css{2,3}
body {
  display: flex;
  flex-direction: column;
  font-family: "Public Sans", sans-serif;
  color: var(--text-dark);
  line-height: 1.45;
  background-color: var(--background-color);
}
```

With that, our three elements (`header`, `main`, and `footer`) will be displayed in a column.

Remember that, by default, flex containers have these properties:

```css
justify-content: flex-start;
align-items: stretch;
```

In the case of columns, that means that horizontally elements will be stretched to take up 100% of the width of the container (`stretch`), but they will be as close to the top of the element as possible (`flex-start`).

::: tip
Important to note that the CSS reset, `reset.css`, it setting the `html` and `body` elements to be full-height:

```css
html,
body {
  height: 100%;
}
```
:::

With that, we now want to make the `main` element as large as possible vertically, so that it will push the footer down to the bottom of the page.

```css
.main {
  flex-grow: 1;
  padding: 3rem 1.5rem 2rem 1.5rem;
}
```

I also took the chance to add some padding to the `main` element so that any text or child elements we add will not be pushed up against its edges.

And with that, our footer will be pushed down to the bottom of the page, because the `main` element takes up all the available space in the container, which it itself takes 100% of the height of the window.

Another change we should do now is take care of spacing in the `main` element when the screen size gets larger. We can use a media query to do that:

```css
/* The following media query increases the distance
of the main content from the header as the
window size increases. */
@media screen and (min-width: 30em) {
  .main {
    padding-top: 5rem;
  }
}
```