---
title: Toggling dark mode
slug: toggle-dark-mode-flask-app
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to toggle between light and dark mode in a Flask app using session data.
draft: true
---


# Toggling dark mode in the movie watchlist project

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/dd9e6043ca734167b4fd06de3d1b05cd](https://diff-store.com/diff/dd9e6043ca734167b4fd06de3d1b05cd)
:::

To toggle dark mode all we have to do is change the CSS variables under `:root`. At the moment, all the variables are set up to support light mode. If we change them to support dark mode, the site will become dark.

Before we do any "toggling", let's just try to change the variables into dark mode.

These are the "light mode" variables in `main.css`:

```css
:root {
  --text-dark: #000;
  --text-light: #fbf2f2;
  --text-muted: #595959;

  --background-color: #fff;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: #e5e5e5;

  --border: 3px solid #000;
}
```

Change them to this:

```css
:root {
  --text-dark: #fbf2f2;
  --text-light: #000;
  --text-muted: #595959;

  --background-color: #1c2023;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: var(--accent-colour-2);

  --border: 3px solid #fff;
}
```

If you refresh the page, you'll see the whole website changes, and now it's in dark mode!

This is because we've used these CSS variables everywhere, so as long as we continue to do so, this small change will take care of changing everything, site-wide.

To toggle between light and dark mode though, we need to have both sets of variables. A simple and effective way to do this is to use light mode by default, and then set dark mode based on a CSS class name. We can do this like so:

```css {14}
:root {
  --text-dark: #000;
  --text-light: #fbf2f2;
  --text-muted: #595959;

  --background-color: #fff;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: #e5e5e5;

  --border: 3px solid #000;
}

:root.dark-mode {
  --text-dark: #fbf2f2;
  --text-light: #000;
  --text-muted: #595959;

  --background-color: #1c2023;
  --accent-colour: #f56565;
  --accent-colour-2: #3bb54a;
  --tag-colour: var(--accent-colour-2);

  --border: 3px solid #fff;
}
```

What this means is that if our `html` element has the `dark-mode` class, the site will be in dark mode. If it doesn't have that class, it will be in light mode.

## Setting theme in the `html` element

Let's go to `layout.html` and make a small change.

We are going to store a setting in the Flask session, which will tell us whether the chosen theme is dark or light.

```diff
 {% from "macros/nav.html" import header %}
 {% from "macros/footer.html" import footer %}

<!DOCTYPE html>
-<html lang="en">
+<html lang="en" class="{{ 'dark-mode' if session.get('theme') == 'dark' }}">
     <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
         <meta http-equiv="X-UA-Compatible" content="ie=edge" />
         <title>{{ title | default('Movie Watchlist') }}</title>
```

The key part there is that we're adding the `dark-mode` class if there is a `theme` in the `session`, and its value is `'dark'`.

## A route to toggle dark mode in Flask

Let's create a Flask route that, when accessed, changes the `theme` property of the `session`.

To do so we will check if the theme is `dark`. If it is, we'll set it to `light`. If it isn't, we'll set it to `dark`.

Inside `routes.py`, I'll add this:

```py
from flask import (
    Blueprint,
    redirect,
    render_template,
    session,
    request,
)

...

@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))
```

This route returns something a bit weird: `redirect(request.args.get("current_page"))`.

That is because when we access this endpoint, we need to send the user back to the page they were on. But Flask is not going to know which page the user was on, unless we tell it that information.

The current page will be sent in a query string, such as `?current_page=/movies`.

## Adding a button to toggle the theme in the nav bar

### Defining the icons

We are going to use an icon in the nav bar that, when clicked, will send a request to the endpoint defined above.

First let's create `templates/macros/svgs.html`, where we will define two macros: one for the "light theme" icon and one for the "dark theme" icon.

While we're at it, let's also define two other icons we'll need later: a star for the ratings and a pencil for the "Edit" button in the movies page. Just copy the code below.

```jinja2
{% macro star(class_) %}
<svg xmlns="http://www.w3.org/2000/svg" class="{{ class_ }}" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
</svg>
{% endmacro %}

{% macro pencil(class_) %}
<svg xmlns="http://www.w3.org/2000/svg" class="{{ class_ }}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
</svg>
{% endmacro %}

{% macro moon(class_) %}
<svg xmlns="http://www.w3.org/2000/svg" class="{{ class_ }}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
</svg>
{% endmacro %}

{% macro sun(class_) %}
<svg xmlns="http://www.w3.org/2000/svg" class="{{ class_ }}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
</svg>
{% endmacro %}
```

::: tip
Each macro can receive a `class_` argument, which then passes CSS classes to the SVG code. We will use this to set the SVG icon size in CSS.
:::

### Creating a link in the nav bar to toggle dark mode

Finally, we can go to our nav bar and add a link there!

Inside `nav.nav`, we will add a third `a` element which will only contain the icon. The link `href` will be our new Flask route, and we need to remember to pass in the `current_page` query string argument as well.

This is what we'll add:

```jinja2
<a
    href="{{ url_for('pages.toggle_theme', current_page=request.path) }}"
    class="nav__link"
>
    <span class="nav__item">
        {% if theme == "dark" %}
            {{ sun("nav__icon") }}
        {% else %}
            {{ moon("nav__icon") }}
        {% endif %}
    </span>
</a>
```

Again, this goes at the end of the `nav` element.

Remember to import the SVG macros at the top of the file:

```jinja2
{% from "macros/svgs.html" import moon, sun %}
```

And with that, we're done! Now there's an icon in the nav bar that, when clicked, goes to the `/toggle-theme` endpoint. It passes the current page as a query string parameter, so that the endpoint can send us back to where we were. Since it changes the session data, when the HTML reloads it will have the `dark-mode` class, which uses the new CSS variables to change the whole page to dark mode.

All that's left is to make sure to use our CSS variables throughout the rest of our CSS, and never use any static colour values unless we want to use the same colour in both light and dark modes.