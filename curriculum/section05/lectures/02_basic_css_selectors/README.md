---
title: How to target specific elements with CSS selectors
slug: target-specific-elements-css-selectors
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# How to target specific elements with CSS selectors

In this lecture we're going to talk a little bit about the CSS selector syntax, which is how we define which elements a given set of style properties applies to.

To keep things simple we're just going to be changing the text colour of a few elements on the page. Don't worry, we're going to be moving onto more exciting changes shortly!

The HTML document we're going to be working with looks like this:

```html
<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Selectors</title>
    <link rel="stylesheet" href="main.css">
</head>

<body>
    <h1>CSS Selector Playground</h1>
    
    <p>I'm a plain old paragraph element.</p>
    <p class="red">I have a class!</p>
    <p id="orange">I have an id!</p>
    <p class="red" id="purple">
        I'm super fancy. I have a class <em>and</em> an id!
    </p>
</body>

</html>
```

## Element selectors

Element selectors are something we've seen a few times already and, in their most basic form, they're used to select every element of a given type on the page.

For example, if we want to turn the `<h1>` element green, we can write something like this in our `main.css` file:

```css
h1 {
    color: green;
}
```

Try it for yourself!

::: warning Spelling!
Note that CSS properties use American English spellings. That means `color` and not `colour`!
:::

Now let's say we want to make all the text inside the `<p>` elements green as well. We can extend our style definitions in one of two ways.

We can write a whole new block below the first one like this:

```css
h1 {
    color: green;
}

p {
    color: green;
}
```

This is fine, but if these styles are intended to be linked, having this duplication can be a bit of a pain. It's two things we need to update if there are changes to the site design, and there's always a chance we'll miss one.

In those cases, it can be better to write this instead:

```css
h1, p {
    color: green;
}
```

When we separate selectors using a comma like this, it's saying that we want to apply the styles defined in the block below to anything which matches any of the provided selectors.

## Class selectors

Instead of selecting elements by type, it's often a much better idea to select elements using classes. Classes are great, because we can use them to apply like styles across different elements, and we get to choose exactly where they apply. We're not automatically applying styles to every instance of an element type.

In order to use a class selector, we just need to write `.` followed by the class name we want to apply our styles to. In our code above, the class we've applied to two of our `<p>` elements is called `red`, so I'm going to replace the contents of `main.css` with the following:

```css
.red {
    color: red;
}
```

If you save the file and reload the HTML document, you'll see that the second and fourth paragraphs have been turned red, but the rest of the text is set to the default black. Note, however, that the contents of the `<em>` element were also turned red.

:::tip Combining selector types
Note that we can combine different selector types if we want. For example, if we want the text in the `<h1>` element to also be red, we can write the following:

```css
h1, .red {
    color: red;
}
```
:::

## Id selectors

Ids are supposed to be unique identifiers, so they're generally not a great idea to use when styling our site. Why? Because it makes it really hard to reuse our CSS code.

There are also issues when it comes to the concept of **specificity**, which we'll be talking about later in this section.

Nevertheless, we can use ids as selectors if we have a valid reason to. They work just like class selectors, except we add `#` to the start of the id, rather than the `.` we put before class names.

```css
#orange {
    color: orange;
}

#purple {
    color: purple;
}
```

If you replace the content of `main.css` with the code above, and you reload the page in your browser, you'll see that the third paragraph is now orange, and the final paragraph has changed to purple.

## Conflicting selectors

One interesting thing in our HTML markup is that the final paragraph has both a class and an id. So what happens if we use both selectors and we provide conflicting style definitions.

For example, let's say we have the following CSS code. What do we expect to happen?

```css
#purple {
    color: purple;
}  

.red {
    color: red;
}
```

What we find is that the text in the final paragraph is turned purple, but the second paragraph is red. Note that the order of our style definitions don't matter in this case. The purple colour always gets applied and overwrites the red.

We'll be talking about why this is later in the section. For now, just know that not all selector types are equal, and some take precedence over others.

## The universal selector (`*`)

One final selector that we need to talk about is `*`.

`*` is a universal selector, and it selects every element in the document. Use this sparingly, as it can cause serious performance issues if abused.

If we want styles to apply throughout the site, inheritance is often a better mechanism for this. Many styles will be inherited by child elements, and we can rely on this feature to reduce the amount of code we write.

We've already seen one example of this. Remember that the `<em>` element inside the final paragraph also had its text turned red? That's inheritance at work.

We'll be giving inheritance a lot more attention soon, but for now let's turn to colours in CSS.
