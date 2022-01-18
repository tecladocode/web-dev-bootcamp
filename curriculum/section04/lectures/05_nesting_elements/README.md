---
title: Nesting HTML elements
slug: nesting-html-elements
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Nesting HTML elements

As we discussed earlier in this section, we can place more than just text between the opening and closing tags of a given element. We can place elements inside one another to create a hierarchy within our document.

Here is a simple example:

```html
<article>
    <h1>Pirate Lingo</h1>
    <p>
        Furl pirate mutiny mast bilge scurvy Davy Jones' Locker.
    </p>
</article>
```

Here we have a new type of element, `<article>`, which denotes any kind of self-contained content in the document.

In the example above, the `<article>` element encloses the `<h1>` and `<p>` elements. The page content here is just some silly pirate themed *lorem ipsum* text.[^lorem]

::: tip Whitespace in HTML
Note that in the example above the opening and closing tags for the `<p>` element are on different lines. This is perfectly legal and extremely common in HTML, especially when lines start getting long.

In almost all cases, any extra whitespace in your HTML document is irrelevant, and will be ignored. This means we can break content up across lines, and we can place empty lines in our document to help with readability.
:::

There are limitations to what can be nested inside other elements. For example, it wouldn't be valid markup if we did something like this:

```html
<h1>
    <article>Some plain text</article>
</h1>
```

We're going to talk about some of these rules in the next lecture.

[^lorem]: [Pirate Ispum](https://pirateipsum.me/)
