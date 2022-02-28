---
title: Adding a nav bar
slug: add-nav-bar-movie-library-project
tags:
    - Not started
    - How to
categories:
    - Video
section_number: 14
excerpt: Add a styled navigation bar to the project, including an icon.
draft: true
---

- [x] Set metadata above
- [ ] Start writing!
- [ ] Create `start` folder
- [ ] Create `end` folder
- [ ] Write TL;DR
- [ ] Create per-file diff between `end` and `start` (use "Compare Folders")


# Adding a nav bar to the movie library

Let's take a look at the nav bar that we'll be adding to our app.

NAVBAR IMAGE

You can see two main parts:

- On the left we've got the brand icon and name. The icon will be an SVG, and clicking on the icon or text will send us to the homepage.
- On the right we've got some links to pages within the app. These change depending on whether the user is logged in or not.

## Writing the HTML for our nav bar

We can start by creating a `templates/macros/nav.html` page. I'm putting this inside `macros` because the navbar will be a Jinja macro.

Inside that file, let's add the smallest amount of code we can to get started:

```html
{% macro header(email, theme) %}
<header class="header">
    <div class="nav-container">
        <a href="{{ url_for('pages.index') }}" class="header__logo">
            <span class="logo__name">Watchlist</span>
        </a>
        <nav class="nav">
            {% if not email %}
                
            {% else %}
                
            {% endif %}
        </nav>
    </div>
</header>
{% endmacro %}
```

I'm adding a `header` element, which contains a `div.nav-container`. This nesting will be useful for styling later on.

There are two elements within the `div`:

- `a.header__logo`, which will contain the brand logo and name.
- `nav.nav`, which will contain all the internal navigation links.

Let's add the icon first. Usually, icons added to this sort of web app are SVG files, but we can just add the SVG code directly into the HTML code:

```html {4-6}
<header class="header">
    <div class="nav-container">
        <a href="{{ url_for('pages.index') }}" class="header__logo">
            <svg xmlns="http://www.w3.org/2000/svg" class="logo__icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z" />
</svg> <span class="logo__name">Watchlist</span>
        </a>
        <nav class="nav">
            {%- if not email %}
```

This icon may be very large though, we will need to adjust the size using CSS later.

Let's first move on to the internal links. Inside each of the if statement branches, we need to add some links:

```html {3-14}
<nav class="nav">
    {% if not email %}
        <a
            href="#"
            class="nav__link"
        >
            <span class="nav__item">Log in</span>
        </a>
        <a
            href="#"
            class="nav__link"
        >
            <span class="nav__item">Register</span>
        </a>
    {% else %}
    {% endif %}
</nav>
```

For each of the links I'm adding an `a.nav__link` element. Inside it, there is a `span.nav__item` with the link text. I've set up this structure to help styling later on.

When an `email` is not provided--the user hasn't logged in--then we display "Register" and "Log in" links.

When the user is logged in, we will display "Movies" and "Log out":

```html {16-28}
<nav class="nav">
    {%- if not email %}
        <a
            href="#"
            class="nav__link"
        >
            <span class="nav__item">Log in</span>
        </a>
        <a
            href="#"
            class="nav__link"
        >
            <span class="nav__item">Register</span>
        </a>
    {% else %}
        <a 
            href="{{ url_for('pages.index') }}"
            class="nav__link {{ 'nav__link--active' if url_for('pages.index') in request.path }}"
        >
            <span class="nav__item">Movies</span>
        </a>
        <a
            href="#"
            class="nav__link"
        >
            <span class="nav__item">Log out</span>
        </a>
    {% endif %}
</nav>
```

## Writing the CSS for our nav bar

