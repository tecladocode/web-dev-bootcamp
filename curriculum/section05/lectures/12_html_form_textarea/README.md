# HTML forms: working with textareas

Now that we've learned how to send data using HTML forms, let's look at the specific form elements that we'll need for the microblog project.

Most form elements behave similarly. Give them a `name` attribute, and that's what the form data will be called. Give them an `id` and that's what will be used to link the `<label>` element to them.

So we can add a textarea to our form like this:

```html
<form method="POST">
    <label for="entry">Entry contents</label>
    <textarea id="entry" name="content"></textarea>
    <input type="submit" value="Add entry" />
</form>
```

There are a few things to note here:

- I'm using `POST` because an entry could be quite long, and extremely long URLs can lead to problems and are unsightly.
- The `<textarea>` is not a void element, but it doesn't have any content. You can place pre-written content inside the textarea within the tags.
- I often get confused with the submit button, and I do this: `<input type="submit">Add entry</input>`. That's incorrect as `<input>` is a void element!

## Grouping inputs and their labels

It is usually a good idea to group together inputs and their labels, so that styling them is a bit easier. In our form, which has a single input and label, this is not so important. But in longer forms it can become so!

For the purposes of learning a better practice, I would do this in our form:

```html
<form>
    <div class="form__input">
        <label for="entry">Entry contents</label>
        <textarea id="entry" name="content"></textarea>
    </div>
    <input type="submit" value="Add entry" />
</form>
```

## Giving classes to our elements

So that elements are later targettable with CSS more easily, we can give them class names that help identify them:

```html
<form method="POST" class="form">
    <div class="form__input">
        <label for="entry" class="form__label">Entry contents</label>
        <textarea id="entry" name="content" class="form__text"></textarea>
    </div>
    <input type="submit" class="form__submit" value="Add entry" />
</form>
```