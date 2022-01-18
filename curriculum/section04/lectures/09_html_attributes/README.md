---
title: HTML attributes
slug: html-attributes
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# HTML attributes

In this lecture we're going to take a closer look at a pair of important attributes: `class` and `id`.

## The `class` attribute

One thing we're going to be doing a lot in this course is adding `class` attributes to our HTML elements. Classes are used for identifying particular elements when applying styles, or when we need to select certain groups of elements in any JavaScript code.

Unlike many attributes, the `class` attribute can be applied to any HTML element. We call this kind of attribute a *global attribute*.

Here is an example of a `<p>` element with a new `class` attribute. The value of this attribute is `text`, so we've said that this element can be identified by the class `text` elsewhere in our program.

```html
<p class="text">I have a class now. Fancy.</p>
```

We can add multiple classes to an element by writing several class names between the quotation marks, separated by spaces.

```html
<p class="class-one class-two class-three">That's a lot of classes!</p>
```

## The `id` attribute

Another common attribute which can be used with any HTML element is the `id` attribute. Ids are very similar to classes in that they're for identifying particular HTML elements, but unlike classes, ids are supposed to be unique identifiers.

Here is an element with both a `class` and an `id` attribute:

```html
<h1 class="title awesome" id="pageTitle">
    Awesome Page Title
</h1>
```

Unlike classes, ids are not generally used for applying styles, because they make it hard to reuse our CSS code. After all any styles we apply to elements with a given id will only affect a single element.

Being able to reuse CSS styles is important to us as developers, because it reduces the opportunity for error, and it also reduces the overall size of our stylesheets, which leads to faster loading websites.

While not very useful for styling purposes, ids are very useful when working with JavaScript, as we often want to implement behaviour for a particular element only.

::: warning ID uniqueness
Ids are unique in theory, but this is a convention more than a strict rule. If you add the same id to several HTML elements, the parser won't complain, and your site will work just fine.

While nothing will break, you should respect the convention of having unique ids, as having a unique identifier can be extremely useful. We already have classes for identifying groups of elements, so there's no need to duplicate this pattern with ids as well.
:::

## Other attributes

There are lots of other attributes available to us in HTML, many of which are specific to certain element types. We've already seen one example: the `required` attribute.

You don't need to memorise the available attributes, but if you ever need to look something up, you can find a good reference on the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes).
