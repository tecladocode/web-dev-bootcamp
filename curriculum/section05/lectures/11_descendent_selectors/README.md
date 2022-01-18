---
title: "More CSS Selectors: Descendents and Siblings"
slug: more-css-selectors-descendents-and-siblings
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# More CSS Selectors: Descendents and Siblings

In this lecture we're going to explore some more complex CSS selectors for targeting descendent and sibling elements.

Before we start, a quick word on terminology.

*Descendent elements* are any elements which are part of the content of another element (known as the *ancestor*). They need not be direct children of the element in question.

*Siblings elements* are any elements which share a parent element.

## The Descendent Combinator

The descendent combinator is a means of combining two or more selectors to describe an ancestral relationship. We achieve this by placing one or more spaces between the selectors.

```css
ul li {
    color: blue;
}
```

The result is a descendent selector, that will target any `<li>` element which is a descendent &mdash; but, not necessarily a direct child &mdash; of a `<ul>` element.

### Chaining Descendent Combinators

We can have a chain of many such selectors if we like, describing a more elaborate ancestral relationship in the document.

```css
ul li a {
    text-decoration: none;
}
```

Here we're setting the value of the `text-decoration` property to `none` for every `<a>` element which is inside an `<li>` element, where that `<li>` element is itself a descendent of a `<ul>` element.

<!-- TODO: I think it would be a good idea to add an image to hammer home this chain -->

We can make these chains of selectors arbitrarily long, but it's rarely a good idea to create very complex chains. Not only does it tie out styles very closely to the structure of our document, it also makes it hard to reuse out styles.

## The Child Combinator

We can specify a more precise ancestry relationship using a child combinator. When using a child combinator, we place `>` between two selectors instead of a space.

When we do this, we're saying that the element targeted by the left hand selector must be a direct parent of any targeted by the right hand selector.

To demonstrate this concept, we're going to use a description list. A description list is used to match terms and definitions, like you might find in a dictionary. Instead of using `<li>` elements, we use `<dt>` and `<dd>` elements in a decription list, which contain terms and the definitions respectively.

For more information, you can look on the [MDN page for description lists](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl).

Let's say we have a selector like this:

```css
dl > dt {
    font-weight: 700;
}
```

Here we're saying that we want to select any `<dt>` element which is a direct child of a `<dl>` element.

If we take the HTML code below, the `<dt>` element will be selected, because the `<dt>` element is a direct child of the `<dl>` element. In other words, the `<dt>` element is directly inside the `<dl>` element.

```html
<dl>
    <dt>Dog<dt>
    <dd>A man's best friend.</dd>
</dl>
```

However, if we add a container for our `<dt>` and `<dd>` elements &mdash; which is quite common when we want to group the elements for styling purposes &mdash; the selector no longer matches our `<dt>` element.

```html
<dl>
    <div>
        <dt>Dog<dt>
        <dd>A man's best friend.</dd>
    </div>
</dl>
```

This is because our `<dt>` element is now a direct child of the `<div>`, not the `<dl>` element. If we stick with the family tree metaphor, we might think of `<dt>` being a "grandchild" of our `<dl>` element, but our selector only targets direct children.

## The General Sibling Combinator

The general sibling combinator is used to select siblings of a given element which matches some selector. The symbol for this combinator is `~`.

```css
label ~ input {
    padding: 5px 10px;
}
```

Here we're selecting any `<input>` elements which are siblings of an `<label>` element. However, not *all* sibling `<input>` elements will be matched by this selector: only those which come *after* the `<label>` are matched.

So in the following code snippet, only the second `<input>` element would be selected:

<!-- TODO: Create a more realistic form for the example below -->

```html
<form>
    <input><input>
    <label></label>
    <input><input>
    <input><input>
</form>
```

Note that the `<input>` element need not come directly after the `<label>`. There can be other sibling elements in between the two.

## The Adjacent Sibling Combinator

Sometimes we only want to select an element that comes directly after another element. For example, perhaps we want to select `<input>` elements which directly follow a `<label>`. In other words, if the element directly before an `<input>` is not a `<label>`, this `<input>` shouldn't be selected.

We can achieve this by using the *adjacent sibling combinator*, the symbol for which is `+`.

```css
label + input {
    padding: 5px 10px;
}
```

The `label + input` selector above would select the every `<input>` element which directly follows a `<label>` in a document.

If we look at the form below, only the first of the `<input>` elements will be selected by the `label + input` selector, as the second `<input>` element doesn't directly follow the `<label>`.

```html
<form>
    <label></label>
    <input><input>
    <input><input>
</form>
```
