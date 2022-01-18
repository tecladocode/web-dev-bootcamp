---
title: Common HTML elements
slug: common-html-elements
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Common HTML elements

In this lecture we're going to introduce a handful of really common HTML elements so that we can start writing some real HTML code for ourselves.

We're going to be discussing what these elements are used for, and some important attributes associated with some of these elements.

::: v-pre
## `<span>` elements
:::

`<span>` elements are generally used to annotate small pieces of text, usually because we want to apply some specific styles, or because we want to add some behaviour that doesn't apply to the surrounding content.

`<span>` elements are extremely generic by design: they don't inherently represent anything. As such, `<span>` elements should really be treated as a last resort element for when we can't offer a better description of the content with other, more specific elements.

For example, if we have some content like this:

```html
<p>Ticket availability is extremely limited!</p>
```

We may want to highlight the word "extremely" to give it additional emphasis. Perhaps we want to change its appearance as part of this to visually distinguish the word from the rest of the content.

This is **not** a good job for `<span>`, because we have an HTML element which is specifically designed to describe stress emphasis in text: `<em>`.

```html
<p>Ticket availability is <em>extremely</em> limited!</p>
```

If we wanted to change the colour of the word "ticket", however, we the `<span>` element would be a great choice, because there's no special meaning we can ascribe to the word "ticket" in this instance. We simply need the `<span>` to make targetting the word easier with our styles.

::: v-pre
## `<a>` elements
:::

`<a>` element are called *anchor elements*, and they're used for links. They're really one of the most important elements we have in our arsenal, and the Internet as we know it is built on these linking elements.

We can provide a destination for a link using the `href` attribute, which stands for **h**ypertext **ref**erence. The content between the opening and closing tags of the `<a>` element is what the user will click on to trigger the link.

```html
<a href="www.google.com">Go to Google!</a>
```

:::tip Interesting destinations
We can actually do a lot more than link to websites using an `<a>` tag. For example, if we start the `href` attribute value with `tel:`, we can use this link to start a phone call, or we can open an email application with `mailto:` followed by the email address of the intended recipient.

We can also link to specific parts of a page by using the `#` symbol at the end of a URL, followed by an id of an element on the page. This will cause the page to open at the location of that element. If the link is to the current page, the user will be navigated to that section of the page. This can be really useful for intra-page navigation.
:::

::: v-pre
## List elements: `<ol>`, `<ul>`, and `<li>`
:::

There are several elements which we can use to structure lists in HTML, and we have several *types* of list available to us.

The most common types of list are ordered and unordered lists, represented by `<ol>` and `<ul>` respectively. A third, less common type of list is a definition list, where we map terms to descriptions.

::: v-pre
### `<ol>`
:::

Ordered lists are used when the order of the list is vital to the meaning of the content. For example, we might use an ordered list when providing instructions. If the steps are performed out of order, the result may not be the same, so here the order of the elements determines the meaning of the content.

::: v-pre
### `<ul>`
:::

Unordered lists are used when the order isn't important to the content. This kind of list might be appropriate for things like a shopping lists. Ultimately, the order in which we write our shopping list doesn't have any real bearing on the meaning of the list.

A good rule of thumb is, if you'd write the list with bullet points instead of numbers, you want an unordered list.

::: v-pre
### `<li>`
:::

The individual list items for both types of list are placed inside `<li>` elements.

These `<li>` elements are placed within the opening and closing tags of the `<ol>` or `<ul>` element. We're going to be discussing this kind of element nesting in more detail in an upcoming lecture.

Here is an example of an ordered list:

```html
<ol>
    <li>Mix butter and sugar.</li>
    <li>Add eggs and flour.</li>
    <li>Pour the mixture into a cake tin.</li>
    <li>Bake at 180°C for 25 minutes.</li>
</ol>
```

Here we're listing the steps for baking a cake. The order of the steps is vital. It wouldn't make much sense if the baking step came first, and then we added the ingredients!

Below you'll find an example of an unordered list:

```html
<ul>
    <li>Dogs</li>
    <li>Cats</li>
    <li>Hamsters</li>
    <li>Rabbits</li>
    <li>Goldfish</li>
</ul>
```

Here we might be listing the animals we have available at our pet shop, and the order here is irrelevant. We're not listing dogs first because we have more of them, or because they're more important than the other animals. It's completely arbitrary, and that's why we should use a `<ul>` element.

::: v-pre
## `<form>` elements
:::

Forms are a vital part of many websites. We use them every time we want to log into a site, or fill out delivery information for online purchases.

Because this is such a common component of sites, there is a whole host of HTML elements surrounding forms. For now I just want to talk about the `<form>` element itself.

There are two special attributes that we can apply to `<form>` elements which determine what the form does when the user submits it. These are `action` and `method`.

The `action` is where we want to send the form data when the form is submitted. When writing our server-side code, we'll write handler functions to deal with this form data.

The `method` determines the type of HTTP request which gets submitted. Generally speaking, we're going to be submitting `POST` requests. More on that later.

```html
<form action="/login" method="post">

    ... form content goes here

</form>
```

::: v-pre
## `<img>` elements
:::

`<img>` elements are one of several elements that can be used to display an image in the browser window. A path to the image file is provided through an attribute called `src`, short for "source". This can be a complete URL, or file path relative to the HTML document.

```html
<img src="https://placekitten.com/200/300">
```

::: tip
Note that the `<img>` element doesn't have a closing tag! It's a void element.
:::

While `src` is the only required attribute for the `<img>` element, we should strive to add another attribute whenever possible: `alt`.

`alt` is used to provide a text description of the image content. It's displayed in the event that the image fails to load, and it can really help with site accessibility for those who are visually impaired.

```html
<img src="https://placekitten.com/200/300" alt="A cute fluffy kitten!">
```
