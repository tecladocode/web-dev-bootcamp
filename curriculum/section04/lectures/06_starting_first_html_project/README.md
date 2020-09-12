# Starting our first HTML project

The best way to learn how to code is by writing code. In this lecture we'll get started with our very first HTML project.

Throughout this section and the next, we'll turn this seemingly simple HTML document into a fully-fledged web page!

I'll start by creating a file to hold our HTML code. Normally when starting an HTML project, the initial "home" page lives in a file called `index.html`.

Then, any HTML file usually starts with a `DOCTYPE` declaration:

```html
<!DOCTYPE html>
```

This tells the browser to read this code as an HTML5 document.

Every HTML document needs to have an `html` element, as well as the `head` and `body` elements inside it:

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
    </body>
</html>
```

To start this project, we'll add a title and some text inside paragraphs.

To do this, we'll use `h1` and `p` elements, like so:

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
    </body>
</html>
```

We've added an `h1` element, which contains the most important title of a page. Then, inside `p` elements I've added some information about what the page is about.

In later lectures we'll also learn how to give the page a title, include images, and link CSS files!
