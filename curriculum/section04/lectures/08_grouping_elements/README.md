---
title: HTML container elements
slug: html-container-elements
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# HTML container elements

Now that we've looked at which elements *can't* be nested, let's take a look at some elements which are specifically designed to contain other elements.

::: v-pre
## `<section>` elements
:::

The content of a `<section>` element represent a thematically related group of elements, but which form a component of a larger whole.

For example, perhaps we have a website with several blog posts on the home page, but the home page also features an area with links to various pieces of merchandise. There is a clear division in the content here, with the blogs being one thematically related group, and ther merch links being another.

We could use `<section>` elements to distinguish these two distinct groups.

```html
<body>
    <section>
        <!-- Merch items -->
    </section>
    <section>
        <!-- Blog posts -->
    </section>
</body>
```

:::tip An alternative approach to the merch store
In a moment we're going to discuss another element called `<article>`. In the example above, it may actually make more sense to wrap the merch section in an `<article>` element instead.

See what you think after reading the section on `<article>` elements. 
:::

We can also place sections within other elements, including within other `<section>` elements. Our individual blog posts might have subsections, for example, and perhaps we have different types of merch on sale.

As a general rule of thumb, `<section>` elements should contain headings, but this isn't a requirement. If you're writing a heading somewhere on your site, it's probably because you're marking a shift in topic, and this is often a good indicator of where a new section begins.

::: v-pre
## `<article>` elements
:::

`<article>` elements are a somewhat tricky element to understand, because the name "article" comes with a lot of conceptual baggage.

An `<article>` element is used to mark a self-contained composition within a document. That means the content makes sense on its own as a standalone work. In the example site we talked about when discussing `<section>`, the individual blog posts would have been wrapped in `<article>` elements, but likely so would the little cards containing the information for the merch items.

The MDN has another [really good example](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article) of using `<article>` elements:

```html
<article class="forecast">
    <h1>Weather forecast for Seattle</h1>
    <article class="day-forecast">
        <h2>03 March 2018</h2>
        <p>Rain.</p>
    </article>
    <article class="day-forecast">
        <h2>04 March 2018</h2>
        <p>Periods of rain.</p>
    </article>
    <article class="day-forecast">
        <h2>05 March 2018</h2>
        <p>Heavy rain.</p>
    </article>
</article>
```

Here they have a weather forecast widget which is wrapped in an `<article>` element.

This may seem a little weird, but if we think back to what an `<article>` is really for, it's a perfectly reasonable use case. The forecast widget makes sense completely on its own. It's a self-contained composition that makes sense removed from the content around it.

One interesting thing, however, is that the `<article>` contains other `<article>` elements. Each of the daily forecasts is also wrapped in an `<article>`. This again makes some sense. We can completely understand the meaning of the forecasts for the individual days, even if we pluck them out of the contect of the weather widget. Many people have something very similar on their desktops after all, or as a widget on their phone.

`<article>` elements are actually one of your go-to elements, so don't forget about them.

::: v-pre
## `<div>` elements
:::

`<div>` elements, much like `<span>` elements, are very generic by design. They don't carry any inherent meaning, which makes them very useful as generic grouping elements.

We use `<div>` elements primarily to aid in styling a page or to add behaviour to some section of the browser window.

They should be used very sparingly, because we have a lot of more specific container types which describe the content of our document far better, such as `<article>`.

When you're about to add `<div>` to your document, take a moment to think if there's something which you can use instead which better describes the group of elements you're placing inside the `<div>`.

::: v-pre
## `<header>` elements
:::

`<header>` elements are used for introductory content, or things like a header bar which contains a logo and navigation links. In this context the `<header>` element's content is not really vital to the site. If we switch out the logo and change the menu, the overall meaning of the page likely hasn't changed at all.

We can actually have several `<header>` elements in a document, and they're permitted inside other elements, such as `<article>` elements.

We can see this in the documentation on the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines#Other_Semantic_HTML_elements_used_in_Sectioning):

> The header can also be used inside other semantic elements such as `<article>` or `<section>`. A section header might contain the section's heading, author name, etc. `<article>`, `<section>`, `<aside>`, and `<nav>` can have their own `<header>`.

Contrary to most people's intuition, there also no requirement for a `<header>` element to be at the top of whatever element it's placed inside of. Most of the time it will feature at the top, however.

::: v-pre
## `<nav>` elements
:::

`<nav>` elements are used for major navigation blocks within the site. Often there will be a `<nav>` element inside the `<header>`, particularly when it's being used as a header bar.

We can have several `<nav>` elements if appropriate, but be sure to only use them for groups of links that form some kind of major navigation group. We don't want a `<nav>` element because we have a couple of links to an external site. A `<ul>` element might be more appropriate there.

:::tip Accessibility
When we have several `<nav>` elements on a page, we can use special attributes called ARIA (**A**ccessible **R**ich **I**nternet **A**pplications) properties to help with accessibility.

ARIA is a big topic on its own, but you can [read about it on the MDN](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA). There's also a good example of using the `aria-labelledby` attribute in the context of multiple `<nav>` elements which you can find [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements#Labeling_section_content).
:::

::: v-pre
## The `<main>` element
:::

`<main>` represents the main content of the document. It's the content which is unique to this particular page, so it doesn't include things like the header bar, navigation, the page footer, *etc.*

Your document should contain a single `<main>` element, which should be placed inside the `<body>` element.

If you need to support older browsers (predominantly Internet Explorer) and screen readers which rely on them, you should include a special `role` attribute for your `<main>` element like this:

```html
<main role="main">
    <!-- Main content goes here -->
</main>
```

This ensure that the `<main>` element is recognised as the main content element for accessibility reasons.

::: v-pre
## `<footer>` elements
:::

`<footer>` elements typically contain things like social media links, secondary navigation, and site smallprint.

Like with `<header>`, we can have several `<footer>` elements in a given document, and they can be placed inside of things like `<article>` or `<section>` elements. In these cases, they should relate to the parent element in some way. For example, we might have information about an article author in the `<article>` footer.
