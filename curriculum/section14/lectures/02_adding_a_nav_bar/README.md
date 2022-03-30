---
title: Adding a nav bar
slug: add-nav-bar-movie-library-project
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Add a styled navigation bar to the project, including an icon.
draft: true
---

# Adding a nav bar to the movie library

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/422036bb6641424b84c1011675eac445](https://diff-store.com/diff/422036bb6641424b84c1011675eac445)
:::

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
            class="nav__link {{ 'nav__link--active' if request.path == url_for('pages.index') }}"
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

This is the CSS for the nav bar. The CSS is explained line by line in the video lecture.

```css
.header {
  padding: 0 2rem;
  border-bottom: var(--border);
}

.header__logo {
  display: flex;
  align-items: center;
  height: 4rem;
  color: inherit;
  text-decoration: none;
}

.header__logo:hover {
  color: var(--accent-colour);
}

.logo__icon {
  width: 2.5rem;
  height: 2.5rem;
}

.logo__name {
  margin-left: 0.5rem;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 20px;
}

.nav-container {
  display: flex;
  justify-content: space-between;

  /* limits the width of the navigation area to 1200px and centres it within the header */
  max-width: 75rem;
  margin: 0 auto;
}

.nav {
  display: flex;
}

.nav__link {
  /* Setting display: flex and align-items: center places the links inside the list items
       vertically in the center of the list item */
  display: flex;
  align-items: center;
  padding: 0 0.5rem;

  /* Removes standard underlines from these links. Explicitly inherits text colour from the body */
  text-decoration: none;
  color: inherit;
}

/* Sets the background colour and text colour of our navigation items when the item has 
   the .nav__link--active class, indicating the current page */
.nav__link--active {
  background: var(--accent-colour);
  color: var(--text-light);
}

/* Adds 1 relative unit of padding (determined by font size) to the right margin of all .nav__item
   elements as long as they are not the last element in their parent */
.nav__link:not(:last-child) {
  margin-right: 1rem;
}

/* Adds a bottom border and applies a negative margin to the element, to nudge it over the
   existing header bar border */
.nav__link:hover {
  margin-bottom: -3px;
  border-bottom: var(--border);
}

.nav__item {
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
}

/* Sets the size of the icon (light/dark theme toggle) to be the same as the font size
    So that it takes up more or less the same amount of space as the links */
.nav__icon {
  width: 1em;
  height: 1em;
}
```