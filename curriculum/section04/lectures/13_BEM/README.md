# A Better Approach to CSS Selectors

In this section I want to present an approach to writing CSS selectors which you'll find in lots of production code. As part of this, we're going to talk about a naming scheme called BEM, which will provide a natural way to group our styles, while keeping specificity low throughout out stylesheets.

## What is BEM?

You can think of BEM as both a CSS methodology and a naming scheme. BEM compliant CSS makes almost exclusive use of classes, with most selectors being formed of only a single class. This to keep specificity uniform across the stylesheet, which makes it easier to overwrite styles simply by paying attention to the order of the code.

The name BEM stands for **B**lock **E**lement **M**odifier. These three components provide a structure for our style definitions, and determine the names of our classes.

Let's start by taking a look at what each of these components represents so that we can better understand the BEM methodology.

### Blocks

A *block* in BEM is a meaningful, standalone entity. Some examples might be a header bar, a menu, or a form.

Block classes are generally single words which describe the role of a given element, but we can use several words linked by hyphens where more than one word is required.

Here are some example block classes:

```css
.header {
    padding: 1rem 2rem;
}

.menu {
    list-style: none;
}

.form {
    display: flex;
    flex-direction: column;
}
```

### Elements

An *element* is a part of a block where the meaning of this component is tied to the block. An item in our menu might be a good example.

Elements classes are written using the following format: `block__element`. The block name comes first, then a pair of underscores, and finally the a descriptive name for the element.

An item in our menu might use the `menu__item` class, for example.

This structure is useful for a couple of reasons.

First, it shows very clearly how a given element fits into the overall structure of our stylesheet. This is not some generic standalone item we're describing: it's an item specific to the `menu`. This gives us a lot of context, and it helps to keep our code organised.

The other reason this structure is handy is that we only need to use a single class for these child elements. They also don't even need to be nested within the HTML document. This is far preferable to using combinators to construct more complex selectors, as that introduces issues with specificity. By using a single class, we can easily overwrite the styles with a single class.

### Modifiers

This brings us nicely to modifiers. Modifiers represent some variant on the basic styles for a block or element.

The modifier component of a class name takes the form of two hyphens followed by the modifier name. This gives us two possible naming schemes: `block__element--modifier` or `block--modifier`.

Let's say we want to highlight the currently selected menu item in our document by changing the background. To do this we'd create a modifier class which we apply only to the element we want to modify. This is used in conjunction with the unmodified class, so we'd have an `<li>` element like this:

```html
<li class="menu__item menu__item--selected">...</li>
```

Our stylesheet might then contain declarations like these:

```css
.menu {
    list-style: none;
}

.menu__item {
    display: block;
    padding: .25rem 0;
}

.menu__item--selected {
    background-color: #89CFF0;
}
```

Modifiers are a vital tool for creating reusable styles, as we can create many variations on some core component throughout our site as necessary.
