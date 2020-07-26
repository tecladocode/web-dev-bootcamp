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

## Different ways to define colours in CSS
