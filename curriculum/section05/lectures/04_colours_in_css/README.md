---
title: "CSS colours: color and background-color"
slug: css-color-background-color
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Colours in CSS: `color` and `background-color`

In this lecture we're going to talk in depth about two properties &mdash; `color` and `background-color` &mdash; and we're also going to cover several different ways to specify colours in CSS.

## The `color` property

We've seen the `color` propery a number of times so far in the course. It's used to change the text color of a given element. However, there's a little bit more to the `color` property, so that's talk about some of those less obvious behaviours.

### `text-decoration`

One thing which may not be immediately obvious is that the `color` property also changes the colour of text decorations. That means things like underlines and strikethroughs. 

We can can set this property separately if we want to change this behaviour. For example, we can specify that the text recoration should be red for this element, regardless of the color like this:

```css
text-decoration-color: red;
```

This might be useful if you're trying to show spelling and grammar issues in a piece of content, where the decoration style and colour is important.

You can find more about text decoration [here](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration).

### `currentcolor`

Setting the `color` property also sets the value of a keyword called `currentcolor`. This acts like a variable, and we can use it in place of a colour value.

This can be useful if you want something like the element's border to match the colour of the text. This saves you having to write out colour definitions twice, which helps reduce bugs.

## The `background-color` property

The `background-color` property is new to us, but it's very straightforward. As you might imagine, it sets the background colour for the elements which we specify.

One subtlety to be aware of is the amount of space an element takes up. For example, if you set the background color on an `<h1>` or `<p>` element, the background is going to reach from one side of the screen to the other, unless there are constraints on the size of these elements. For a `<span>` or `<em>` element, the background is going to stop at the limits of the text by default.

This is due to the default display properties of these elements.

`<h1>` and `<p>` elements have a default style of `display: block;`, and so they fill up the width of their containers.

`<span>` and `<em>` elements have a defauly style of `display: inline;`, and these take up only the space required to acommodate the element's content.

Play around with the `background-color` and `display` properties of different elements to see this in action.

## Different ways to specify colours in CSS

There are many ways to specify colours in CSS, with the most widely used formats being hexadecimal, RGB, and HSL. If you're not familiar with these colour models, refer back to the previous lecture.

All of these colour representations have variants that allow for transparency.

in CSS, we also have special keywords and named colours that we can make use of, such as `white`, `black`, and `red`.

### Named colours

Let's start with named colours, since we've seen several examples of these already.

The number of named colours in CSS is surprisingly large, and has grown with each new version of CSS. We can use any of these specially defined names in place of a colour defined in, say, RGB.

Some of these colour names are aliases for other colours. Most notably `gray` and `grey` can be swapped freely in any colour names which include them.

You can find a complete list of named colours [here](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords).

### RGB

As we learnt previously, RGB represents colours using three channels &mdash; red, green, and blue &mdash; and each of these channels takes a value between `0` and `255`.

In CSS, we can specify an RGB colour by writing `rgb()`. Inside the parenthese, we place the values for the different channels in order, separated by commas.

Pure red would therefore look like this: `rgb(255, 0, 0)`. Black would be `rgb(0, 0, 0)`, and white would be `rgb(255, 255, 255)`.

We can specify any combination of values we like, as long as they fall within the accepted range.

### Hexadecimal values

As we know, we can also represent RGB values using hexadecimal, and this is perfectly valid in CSS. It's actually usually preferable, as hexadecimal representations of colours use fewer characters, and this makes our stylesheets smaller. Reducing the size of our stylesheets helps our pages load faster!

Whe specifying a hexadecimal colour in CSS, we need to write `#` before the values.

To use the same examples as before, pure red would be `#ff0000`; black would be `#000000`; and white would be `#ffffff`.

In case you're wondering, the case of the characters doesn't matter. You can write `#FF0000`, for example, if you prefer.

::: tip Hexadecimal shorthand
In some cases we can represent an RGB colour with fewer values, such as when the values repeat.

For example, let's look at the representation of white, which is `#ffffff` in hexadecimal. Since each pair is the same value twice, we can cut this down to just `#fff` and this is an understood shorthand for the longer `#ffffff`.

We can do the same for black, which is just `#000`.
:::

### HSL

We start an HSL colour definition in much the same way as an RGB colour: `hsl()`.

Inside the parentheses, we need to provide three comma separated values. The first value is an angle, and the other two are percentages, representing the saturation and lightness levels respectively.

:::tip Specifying the angle
One thing to note is that we don't need to write the `°` symbol when writing HSL values. If you want to be explicit about the fact that this is a degree measurement, however, you can add `deg` directly after the angle value.

You can also specify values in radians if you prefer, adding `rad` after the value.
:::

A saturation level of `100%` represents maximum saturation, as you might expect, and `0%` represents the lowest posible level of saturation. This will give you a shade of grey.

For lightness, `100%` will give you pure white, and `0%` will give you black. A lightness level of `50%` is normal lightness.

Here is a representation of the CSS named colour `purple` in HSL as an example: `hsl(300, 100%, 25%)`.

## Transparency and opacity

Both RGB and HSL can be extended to also include an alpha channel, which represents opacity. If you want to use this additional value, you need to write `rgba` or `hsla` as appropriate when defining the colour.

After doing this, you'll be able to provide a fourth value as either a percentage or a decimal, which represents how opaque you want the colour to be. This allows you to create layers of colour for overlapping elements.

A value of `100%` or `1` is fully opaque, which `0%` or `0` is completely transparent.

We can also provide opacity when using hexadecimal representations of RGB by adding a 7th and 8th digit. However, browser support for this feature is not universal, so some colours may not be displayed correctly. It really depends on which browser your users access your site through. This is mostly a problem for mobile browsers, so keep that in mind.

You can find support statistics [here](https://caniuse.com/#feat=css-rrggbbaa).

Instead of using the `rgba` or `hsla` definitions, you can also specify a property called `opacity` which will change the opacity for an entire element. This is useful if you want the opacity effects to apply to all aspects of the element.

There's also a named "colour" called `transparent` which can be used to create a full transparent component. This is roughly equivalent to writing an `rgba` or `hsla` colour with an alpha value of `0`.
