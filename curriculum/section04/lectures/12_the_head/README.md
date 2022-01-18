---
title: Document level annotations
slug: document-level-annotations
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Document level annotations

In this last lecture of the section I want to talk briefly about the `<head>` and `<body>` elements, the `<html>` element, and the `DOCTYPE` preamble.

## `DOCTYPE`

The first line of all of your HTML5 documents is going to look like this:

```html
<!DOCTYPE html>
```

This piece of preamble exists for legacy reasons, and its job is to tell the browser that this document should abide by the HTML5 specification.

::: v-pre
## The `<html>` element
:::

The `<html>` element is the root of our HTML document. All of our other HTML elements belong inside this element.

The `<html>` element should always have exactly two child elements: `<head>` and `<body>`. The other elements should be descendents of the `<head>` and `<body>`.

It's important to also provide the language for the page as part of the `<html>` element using the `lang` attribute, like so:

```html{3}
<!DOCTYPE html>

<html lang="en">

    ... document content

</html>
```

::: v-pre
## The HTML `<head>` element
:::

The `<head>` sits inside the `<html>` element, and is going to look largely the same for all of your pages.

There can only be a single `<head>` element in the document, and it contains elements which describe broad features of the page, like the page title, the author, and some required resources like CSS stylesheets.

The `<head>` element is required for all HTML5 documents. If you don't include one, the browser will generate one for you, because the HTML markup is not valid without it.

::: warning
Note that the `<head>` and `<header>` elements are different elements with very different purposes!
:::

### Setting a page title

We can use the `<title>` element to set a title for our page in the HTML `<head>`, like so:

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>This is the page title</title>
    </head>

    ... other document content

</html>
```

::: v-pre
### `<meta>` elements
:::

`<meta>` elements are used to describe meta information about the document which cannot be expressed using other elements, like `<title>`.

A common way to use `<meta>` elements is to set a `name` and `content` attribute which functions as a key value pair. For example, we might do something like this:

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>This is the page title</title>
        <meta name="author" content="Rolf Smith">
    </head>

    ... other document content

</html>
```

:::tip
Note that `<meta>` is a void element!
:::

One `<meta>` element that should be present in all of your documents is this:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

This is a vital component for responsive design, which we'll discuss in more detail in the next section when we learn about CSS.

:::tip Responsive Design
Responsive design is an approach taken to designing and implementing modern websites. The idea is that our sites should be viewable on a wide variety of screen sizes, from mobile displays to ultrawide monitors, and the user experience should be largely the same.

We're going to look at responsive design in a lot of detail in the next section, as its a fundamental cornerstone of modern front end web development.
:::

::: v-pre
### The HTML `<body>` element
:::

The `<body>` element is the main container for the content of the page, along with any associated markup. Generally the `<body>` will have `<header>`, `<main>`, and `<footer>` as direct children, but this is not a requirement.

Much like the HTML `<head>` element, there can only be a single `<body>` element, and it must come after the `<head>`.

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <title>This is the page title</title>
        <meta name="author" content="Rolf Smith">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body>
    
    </body>
</html>
```

The code above is a good starting point for all of the HTML pages you will create. Many editors have features to create this starting code for you with just a couple of key presses. For example, in VS Code, you can type `!` followed by `tab` while inside an HTML document to creating something very similar to what you see above.
