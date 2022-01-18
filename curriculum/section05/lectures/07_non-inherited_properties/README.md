---
title: Non-inherited Properties
slug: non-inherited-properties
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Non-inherited Properties

As we discussed in the last lecture, not all properties are inherited by default. In this lecture I want to go over some of the more common non-inherited properties.

## Layout properties

A broad categoty of non-inherited properies can be thought of as "layout properties": properties which change the size of the element in some way, or how it interacts with the elements around it.

These properties include things like `margin`, `padding`, `height`, `width`, `box-sizing`, `position`, and `display`.

The reason these properties don't inherit by default is simply that it doesn't make a lot of sense. For example, if we want to put some space underneath an element, it doesn't really make much sense to add this much space to every single child element as well.

Similarly, if we set the `height` of an element explicitly, we'll clearly run into a lot of trouble if every child element also became this size.

`display` is another case where we could run into major problems. `<p>` elements have a display style of `block`, which means they fill the width of their container. We often put things like `<span>` and `<a>` elements inside `<p>` elements, and usually we want them to fit into the normal flow of the text content. We generally don't want these elements forced onto their own lines.

If these properties were inherited, we'd inevitably end up writing far more code just to correct the issues being caused by inheritance!

## Borders and outlines

Border and outline properties &mdash; much like layout properties &mdash; are not inherited by default, and for much the same reason.

Just because we want a border around a `<p>` element, it doesn't mean we want a border around every element inside the `<p>` element as well. Correcting these issues would become a real headache, as we'd have to set `border: none;` on every child of that `<p>` element.

In the very unlikely case that we *do* want to inherit the border of some parent element, remember we can set `border: inherit;` on the child elements to force the inheritance of non-inherited properties.

## Background properties

For simple cases, like setting a matte colour, it's not really obvious why this property wouldn't be inherited. After all, if the background of a given container is `red`, and the child elements don't have a background colour set, then they're going to appear to have a `red` background.

However, we can produce far more elaborate backgrounds for elements than this, and in those cases we'd end up in hot water.

For example, say we decide to use an image as a background for a given element. If the child elements inherited this property value, then we'd get a new version of the image for each of these elements, each placed in a different element's space. This is almost certainly not what we want.

We can end up in a similar situation when setting a gradient as the background for an element. We don't want all of the child elements to have their own gradient background, as they won't match the overall background.

There are also problematic cases with a matte background as well. For example, what if we set a `position` property on a child element which places it outside of its parent element somehow. In those cases, it's not clear that we'd want this background to extend beyond the parent element, so it's better left for the developer to specify this explicitly.

## Designed for the common case

One pattern you're likely seeing emerge here is that CSS is defined to provide sane inheritance behaviour for the common use case. While there may be a niche use case for inheriting borders, the overwhelming majority of projects would be hindered by the inheritance of this property, and would be forced to correct the unwanted behaviour.

If you're not sure if a property is inheritable, think about whether or not it would be helpful for this property to be inherited in the majority of cases. If not, it likely isn't inherited by default.

You can also find this information on the MDN for any CSS property.
