---
title: "HTML forms: working with textareas"
slug: html-forms-working-with-textareas
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# HTML forms: working with textareas

Now that we've learned how to send data using HTML forms, let's look at the specific form elements that we'll need for the microblog project.

Most form elements behave similarly. Give them a `name` attribute, and that's what the form data will be called. Give them an `id` and that's what will be used to link the `<label>` element to them.

So we can add a textarea to our form like this:

```html
<form method="POST">
    <label for="entry">Entry contents</label>
    <textarea id="entry" name="content"></textarea>
    <button type="submit">Add entry</button>
</form>
```

There are a few things to note here:

- I'm using `POST` because an entry could be quite long, and extremely long URLs can lead to problems and are unsightly.
- The `<textarea>` is not a [void element](/section04/lectures/01_elements/), but it doesn't have any content. You can place pre-written content inside the textarea within the tags.

## Grouping inputs and their labels

It is usually a good idea to group together inputs and their labels, so that styling them is a bit easier. In our form, which has a single input and label, this is not so important. But in longer forms it can become so!

For the purposes of learning a better practice, I would do this in our form:

```html
<form>
    <p class="form__input">
        <label for="entry">Entry contents</label>
        <textarea id="entry" name="content"></textarea>
    </p>
    <button type="submit">Add entry</button>
</form>
```

::: tip
It might look weird to surround our label and textarea with a `<p>` element, but they are intended for that purpose!

The [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) states:

> HTML paragraphs can be any structural grouping of related content, such as images or form fields.
:::

## Giving classes to our elements

So that elements are later targettable with CSS more easily, we can give them class names that help identify them:

```html
<form method="POST" class="form">
    <p class="form__input">
        <label for="entry" class="form__label">Entry contents</label>
        <textarea id="entry" name="content" class="form__textarea"></textarea>
    </p>
    <button type="submit" class="form__submit">Add entry</button>
</form>
```