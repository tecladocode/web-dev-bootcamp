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

In addition to describing these general ancestry relationships, we can be more precise using a child combinator. Instead of using spaces, we can place `>` between two element instead.

When we do this, we're saying that the element targeted by the left hand selector must be a direct parent of one targeted by the right hand selector.

```css
ul > li {
    font-weight: 700;    
}
```

The child selector above, `ul > li`, selects any `<li>` element which is a direct child of a `<ul>` element.

That means it would select the `<li>` element featured below:

```html
<ul>
    <li>A list item</li>
</ul>
```

But it wouldn't select this one:

```html
<ul>
    <div>
        <li>A list item</li>
    <div>
</ul>
```

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
</form>
```

Note that the `<input>` element need not come directly after the `<label>`. There can be other sibling elements in between the two.

