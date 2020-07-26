# Colours in CSS: `color` and `background-color`

In this lecture we're going to talk in depth about two properties &mdash; `color` and `background-color` &mdash; and we're going to cover several different ways to specify colours in CSS.

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

There are many ways to specify colours in CSS, with the most widely used formats being hexadecimal, RGB, and HSL. All of these have variants that allow for transparency.

We also have special keywords and named colours that we can make use of.

### Named colours

Let's start with named colours, since we've seen several examples of these already.

The number of named colours in CSS is surprisingly large, and has grown with each new version of CSS. We can use any of these specially defined names in place of a colour defined in, say, RGB.

Some of these colour names are aliases for other colours. Most notably `gray` and `grey` can be swapped freely in any colour names which include them.

You can find a complete list of named colours [here](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords).

### RGB colours

RGB is an additive colour model, where we add **r**ed, **g**reen, and **b**lue channels in different combinations to produce a wide variety of different colours.

::: tip Why red, green, and blue?
While many of us are taught in school that red, blue, and yellow are the primary colours, this isn't the actually the case.

There are two sets of primary colours: one set for additive mixing, and one for subtractive mixing.

The primary colours for subtractive mixing are cyan, magenta, and yellow. In subtractive mixing, each of the colours blocks out some portion of the light spectrum, and what we see is what's left behind. Subtractive mixing is often used in printing, which is why your printer has cyan, magenta, and yellow ink.

The primary colours for additive mixing are red, blue, and green. In additive mixing, we add light of different wavelengths, and the combination of these different light sources produces a composite colour.
:::

We generally specify these values individually using values between `0` and `255` for 8-bit colour, where `rgb(0, 0, 0)` is black, and `rgb(255, 255, 255)` is white. We can also use percentages, but this is very uncommon in practice.

The CSS named colour `purple` is represented as `rgb(128, 0, 128)`. As you can see, we need a moderate amount of red light, no green light, and a moderate amount of blue light to produce this colour.

I recommend you play around with these different values and see how they combined to produce different colours.

::: warning RGB and consistency
RGB colours are not entirely consistent across different devices, or even consistent for the same device over time. You may notice if you open a website on your computer, and then the same site on your phone, that the colours on that site are not quite the same.

One way to combat this is to calibrate devices to a standard colour space like sRGB. If you're doing colour sensitive work, this is something you may need to look into.
:::

### Representing RGB using hexadecimal values

We can represent RGB colours using hexadecimal values, which are much more succinct. This can help reduce the size of our CSS files, potentially improving loading speeds.

Hexadecimal is a base-16 number system, with the numerals `0-9`, plus `a`, `b`, `c`, `d` , `e`, and `f`. `f` is therefore equivalent to the number `15` in decimal. `ff` is `15` x `15`, which is `255`. In case you're wondering, the case of the characters doesn't matter.

Hexadecimal values are usually three pairs of two digit values, preceeded by a `#`. This `#` is required in CSS.

To take the example of `purple` again, the hexadecimal equivalent is `#800080`. `128` is `8` lots of `16`, with no remainder, so we get a hexadecimal value of `80` for the red and blue channels, and a value of `00` for the green channel.

::: tip Hexadecimal shorthand
In some cases we can represent an RGB colour with fewer values, such as when the values repeat.

For example, let's look at the representation of white, which is `#ffffff` in hexadecimal. Since each pair is the same value twice, we can cut this down to just `#fff` and this is an understood shorthand for the longer `#ffffff`.

We can do the same for black, which is just `#000`.
:::

### HSL

The HSL colour model is somewhat different to RGB. The initialism stands for **H**ue, **S**aturation, and **L**ightness, and what may be surprising to you is that the first value is an angle.

HSL uses a cylindrical model to represent the available colour space. The angle provded as a value for the hue is essentially a direction on a colour wheel, as though you were looking directly down on the coloured cylinder.

At an angle of `0°` we find the colour red; at `120°` we find the colour green; and at `240°` we find the colour blue.

As we move from the edge of the cylinder to the centre, the colours change from very vibrant to dull. This change is represented by the saturation value, which we write as a percentage in CSS.

A value of `100%` indicates a fully saturated colour, but what this looks like is dependent on the lightness value. A value of `0%` will be some shade of grey.

Lightness, also represented as a percentage, indicates the amount of white and black added to the colour. A lightness value of `100%` will produce the colour white, while `0%` will produce pure black. At a lightness value of `50%`, a saturation value of `100%` will produce the most saturated version of a given colour.

A lightness value of `50%` is sometimes referred to as "normal" lightness.

Here is a representation of `purple` in HSL: HSL(300, 100%, 25%).

::: tip Specifying angles for HSL values
One thing to note is that we don't need to write the `°` symbol when writing HSL values. If you want to be explicit about the fact that this is a degree measurement, however, you can add `deg` directly after the angle value.

You can also specify values in radians if you prefer, adding `rad` after the value.
:::

### Transparency


