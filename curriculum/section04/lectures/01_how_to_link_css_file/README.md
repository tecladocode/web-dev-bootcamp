# How to link CSS files with HTML

When we write CSS for a web page, we generally do so inside a dedicated `.css` file. So how do we hook this CSS file up to our HTML document?

We do this using a special HTML element called `<link>` which lives inside the `<head>` of our HTML document.

Let's imagine we have an HTML file like this, called `index.html`:

```html
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>My Home Page</h1>
    <p>
        Welcome to my home page.
        There's not much here right now, but check back soon!
    </p>
</body>
</html>
```

This is some fairly typical boilerplate HTML which you'll be including in all of your HTML documents.

:::tip Top tip
Because this is code we have to write all the time, many editors give us useful shortcuts to save us writing this tedious markup out by hand.

For example, in VS Code, you can `!` followed by `tab` when inside an HTML document to generate a document similar to the one above.
:::

Now let's say we have a css file called `main.css`, which looks like this:

```css
h1 {
    color: blue;
    margin-bottom: 24px;
    font-size: 24px;
}

p {
    color: red;
}
```
