# Anatomy of an HTML tag

In this section we're going to dive into the HTML syntax. Don't worry, HTML is not very complicated, and you'll have a good understanding of what everything means in no time!

## What is an HTML tag?

First of all, what is a tag?

An HTML document is composed of units which describe the structure and meaning of a page's content. These components are called HTML *elements*. We write elements using tags, which delimit the start and end a particular element within the document. Content between these two tags are considered to be *inside* the element.

::: tip Void elements
Some elements aren't permitted to have content like this and are called *void elements*. These are written with a single tag in HTML5, rather than an opening an closing tag.

We'll look at some examples thoughout this chapter.
:::

We can place other tags inside the start and end tags of other elements, and this is how we construct a hierarchy within the document. We can also place plain text between tags, which is generally how we add text content to a page.

## An example HTML element

Let's look an example of a common element: the `<p>` element. `<p>` elements represent paragraphs, but in HTML this means more than breaking up chunks of text.[^p]

Below you'll find a simple example of a `<p>` element with a small amount of text content.

```html
<p>Hello! I'm inside a paragraph element.</p>
```

`<p>` elements have an opening and closing tag, because they're permitted to have content. They wouldn't be much use otherwise!

The opening tag is the name of the element &mdash; `<p>` &mdash; but the closing tag contains a forward slash, which marks it as a closing tag: `</p>`. If we omit this forward slash, it looks like we're trying to create a second paragraph element inside the first.

::: warning Missing closing tags
The HTML parser in our browsers will do its best to fill in missing closing tags when we omit them, but we shouldn't rely on this. It might not put the closing tag where you intended!

Sometimes whole elements will be added if they're missing as well. A good example is the `<html>` element which encapsulates the document's content.
:::

## Nested HTML elements

As I mentioned already, we can place elements inside the tags of another element like this:

```html
<article>
    <h1>Pirate Lingo</h1>
    <p>
        Furl pirate mutiny mast bilge scurvy Davy Jones' Locker.
    </p>
</article>
```

Here we have two new types of element: `<article>` and `<h1>`.

`<article>` elements denote any kind of self-contained content in the document, and `<h1>` elements represent the primary heading for the page.

In the example above, the `<article>` element encloses the `<h1>` and `<p>` elements. The page content here is just some silly pirate themed *lorem ipsum* text.[^lorem]

::: tip Whitespace in HTML
Note that in the example above the opening and closing tags for the `<p>` element are on different lines. This is perfectly legal and extremely common in HTML, especially when lines start getting long.

In almost all cases, any extra whitespace in your HTML document is irrelevant, and will be ignored. This means we can break content up across lines, and we can place empty lines in our document to help with readability.
:::

## HTML attributes

In the examples we've seen so far, the opening tag for an element has just been the name of the element, but we can also write attributes in this opening tag as well.

Different HTML elements accept different attributes, and they're used for a wide variety of purposes. For example, we can use an attribute to declare that a form field is required, or we can add anchors that make it easy to refer to a particular element or group of elements.

An attibute is composed of three parts: the attribute name, an assignment operator (`=`), and the value to be associated with this attribute. This value is surrounded by quotation marks.

Let's look at some examples of common attributes in practice.

### The `class` attribute

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

### The `id` attribute

Another common attribute which can be used with any HTML element is the `id` attribute. Ids are very similar to classes in that they're for identifying particular HTML elements, but unlike classes, ids are supposed to be unique identifiers.

Here is an element with both a `class` and an `id` attribute:

```html
<h1 class="title awesome" id="pageTitle">
    Awesome Page Title
</h1>
```

Ids are not generally used for styling purposes, because it makes it hard to reuse styles. After all any styles we apply to elements with a given id will only affect a single element. However, ids are very useful when working with JavaScript, as we often want to implement behaviour for a particular element only.

::: warning ID uniqueness
Ids are unique in theory, but this is a convention more than a strict rule. If you add the same id to several HTML elements, the parser won't complain, and your site will work just find.

While nothing will break, you should respect the convention of having unique ids, as having a unique identifier can be extremely useful. We already have classes for identifying groups of elements, so there's no need to duplicate this pattern with ids as well.
:::

### Shorthand attributes

In some cases, you may see attributes written as just the attribute name, without the following `=` and value. This is a shorthand for writing `=""` after the attribute name, and it's used for attributes which don't take any value.

An example is the `required` attribute for form fields, which can be written as either `required=""` or, more commonly, as `required`.

### Other attributes

There are lots of other attributes available to us in HTML, many of which are specific to certain element types. We've already seen one example: the `required` attribute.

You don't need to memorise the available attributes, but if you ever need to look something up, you can find a good reference on the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes). The MDN &mdash; short for **M**ozilla **D**eveloper **N**etwork &mdash; is a great resource for looking up and learning about web technologies. It's an invaluable tool that you should spend some time getting familiar with.

[^p]: [The usage of `<p>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)

[^lorem]: [Pirate Ispum](https://pirateipsum.me/)
