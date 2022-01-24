---
title: Borders in CSS
slug: css-borders
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Borders

We've already discussed borders as a component of the CSS box model, but in this lecure we're going to talk about some of the specific border properties available to us in CSS.

## `border-color`, `border-style`, and `border-width`

When defining a border, we need to specify three main aspect of the border: the colour of the border, the style or type or border, and the thickness of that border.

### Colour

<!-- TODO: Add code examples for this section -->

The `border-color` property allows us to specify the first of these components. By default, the border takes on the same colour as the `color` property of the element. This is because setting the `color` property changes the meaning of a keyword called `currentcolor`, and `currentcolor` is the default value for the border colour.

The `border-color` property is actually a shorthand property, which lets us define several properties at once. Those properties are `border-top-color`, `border-right-color`, `border-left-color`, and `border-right-color`.

We can use these properties to specify a different border colour for the different edges of the element's box.

We can also use the `border-color` property to set several colours at once.

- If we provide a single colour for the `border-color` property, every border edge is set to the same colour.

- If we provide two colours, the first colour is used for the top and bottom border edges, while the second colour is used for the left and right edges.

- If we provide three colours, the first colour is used for the top edge, the second colour is used for the left and right edges, and the third colour is used for the bottom edge.

- If we provide four colours, the first colour applied to the top edge, and the remaining colours are applied in a clockwise direction.

### Style

The `border-style` property allows us to apply a pattern to the border.

Most borders use the value `solid`, but it's possible to use dashed and dotted borders. While very common on the early Internet, these alternative properties have fallen heavily out of fashion.

If you're interested, you can see some examples on the [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style).

Just like with `border-color`, `border-style` is a shorthand property for all the different edge style properties. We can also use multiple styles, just like with `border-color`, and this works in the same way.

Using a value of `none` for any of a border edge will cause it to become invisible. This is he default value for every border edge.

### Thickness

We can specify the thickness of the border using `border-width`.

Once again, this is a shorthand property and we can specify a different border width for every edge of the element.

By default, if a border edge has a style other than `none`, the border thickness will be `medium`. This isn't a precise value, but you'll often find the border defaulting to `2px`.

You can change these width values using any sizing units you like, but percentage values are not valid for borders.

Generally we use pixels for border thicknesses, because we want them to be very narrow, so using relative sizing elements like `rem` and `em` don't have a meaningful effect.

## The `border` property

We can specify a value for the `border-color`, `border-style`, and `border-width` in one go using the `border` property.

When using `border`, the order of the values doesn't matter, and we can specify one, two, or three values. The browser is able to determine what these values refer to, because the different component properties expect very different types of values.

The default property value will apply for any values we don't provide.

## Border radius

These days its extremely common to see rounded corners on boxes and buttons when browsing the Web. This is an effect we can achieve by using the `border-radius` property.

Interestingly, you can use the `border-radius` property, even if you don't have a visible border. This means we can create rounded corners for an element with only a background, for example.

Just like with the other border properties we've looked at so far, `border-radius` is a shorthand property for four other properties: `border-top-left-radius`, `border-top-right-radius`, `border-bottom-right-radius`. `border-bottom-left-radius`. Each of these is quite a mouthful, and thankfully we rarely need to use them.

Because `border-radius` lets us set values for several properties at once, the syntax can get extremely complicated, because each of these properties can be given multiple values. You can look at [the MDN page](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius#Syntax) for more information.

More often than not, you'll be setting a uniform border radius, which will be applied to every corner of the box. In these cases we can provide a single value to `border-radius`, which will be applied to all of the component properties.

### Percentages vs absolute units

Depending on the unit type we use to define the `border-radius` value, the effect of the property may be different.

This is because values defined using a percentage are based on the height and width of the element, and these measurements can be uneven. As such we can end up with the border radius being elliptical.

When using an absolute value, such as `5px`, the border radius is always circular.

[The MDN page](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius#Examples) for the `border-radius` property features a number of examples where you can see this difference more clearly.

It's possible to achieve the same elliptical effect using absolute units by providing a pair of values for a given corner. Again, you can find details of the syntax on the MDN page if you're interested in experimenting with this feature.
