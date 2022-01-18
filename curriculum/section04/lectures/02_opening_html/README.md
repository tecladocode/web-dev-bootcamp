---
title: A quick example of using HTML and CSS
slug: quick-html-css-example
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# A quick example of using HTML and CSS

In this lecture, let's take a look at some HTML and CSS code. This will help you get familiar with the syntax of both languages, and understand how they interact with each other.

Although we'll go over the code quite quickly in this lecture, throughout the next two sections we'll dive into everything in detail. Don't worry if things aren't fully clear just yet!

## HTML

Modern websites generally are built using HTML5 — the latest version of HTML. HTML5 documents almost always start with similar code:

```html
<!DOCTYPE html>
<!-- Tell the browser this is an HTML document -->
<!-- Start the HTML document -->
<html lang="en">
    <!-- Page-level data that the user doesn't see directly -->
    <head>
        <!-- The character set the code uses -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- Page title (shown in the browser window) -->
        <title>Example HTML File</title>
    </head>

    <!-- What the user sees in the page -->
    <body>
    </body>
</html>
```

We have the `DOCTYPE`, which tells the browser that this is an HTML5 document. The browser will receive this code (which basically, is just text written in a specific way). If we tell the browser this is HTML code, then it can try to understand it by following the HTML rules it knows.

Then there's an `<html>` element, and inside it, we have `<head>` and `<body>`. I've indented some of the elements, which means I've placed spaces in front of the element's tags. We do this to organise our code, making it easy to see what is inside a given element. HTML doesn't care about that though. Everything could be on one line, for all it cares!

The `<head>`, for the most part, contains information for the browser. The `<body>` contains what the user will see in the page.

We've got a couple `<meta>` elements, which include information like the character set the browser uses[^character_sets], or information to help determine how the page will scale with the size of different devices.

Then we've got a `<title>` element, that gives the window a title. This is shown in your browser and in your browser tabs. Search engines like Google can also use the contents of this element in their search results.

Let's add a bit more code to the `<body>` so something shows up when we open the file:

```html
<!DOCTYPE html>
<!-- Tell the browser this is an HTML document -->
<!-- Start the HTML document -->
<html lang="en">
    <!-- Page-level data that the user doesn't see directly -->
    <head>
        <!-- The character set the code uses -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- Page title (shown in the browser window) -->
        <title>Example HTML File</title>
    </head>
    <body>
        <!-- A top-level title -->
        <h1>First HTML File!</h1>
        <!-- A paragraph -->
        <p>Welcome to your first HTML file!</p>
        <p>
            While we work with HTML documents, designing the pages and their
            structure, we often don't want to worry about the text contents of the
            page. We can write those after we write the code for the page.
        </p>
    </body>
</html>
```

I've added three new elements inside the body: an `<h1>`, which is the most important title in the page, and two `<p>` elements, which are for paragraphs. We'll discuss both of these in more detail later on!

If we open the page now though, you can see that the title looks large and bold. The paragraphs, on the other hand, look smaller, and they're slightly separated from each other. That's because my browser applies some default styles to `<h1>` and `<p>` elements. We can change those, and we will do in a moment!

Let's add a bit more code to the HTML file first:

```html
<!DOCTYPE html>
<!-- Tell the browser this is an HTML document -->
<!-- Start the HTML document -->
<html lang="en">
    <!-- Page-level data that the user doesn't see directly -->
    <head>
        <!-- The character set the code uses -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- Page title (shown in the browser window) -->
        <title>Example HTML File</title>
    </head>
    <body>
        <!-- A top-level title -->
        <h1>First HTML File!</h1>
        <!-- A paragraph -->
        <p>Welcome to your first HTML file!</p>
        <p>
            While we work with HTML documents, designing the pages and their
            structure, we often don't want to worry about the text contents of the
            page. We can write those after we write the code for the page.
        </p>
        <p>
            For that reason, we use sample placeholder text like this
            <i lang="la">Lorem ipsum</i>:
            <!-- Idiomatic text element to describe 'Lorem ipsum' -->
        </p>
        <!-- Added lang="la" to add language information since it's different from the html element -->
        <blockquote lang="la">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ultrices
            libero eu porttitor luctus. Nam sollicitudin fringilla mi a varius.
            Aliquam vel tincidunt risus. Vestibulum rhoncus fringilla justo, nec
            feugiat leo. Donec lobortis tortor ut porta ullamcorper. Quisque diam
            lectus, maximus ut lacus vitae, ornare tempus tortor. Vivamus gravida in
            mi vitae auctor. Ut imperdiet sed dui eget lacinia. Etiam lobortis neque
            ut lacus rhoncus, nec hendrerit mauris bibendum. Maecenas sagittis, felis
            et iaculis feugiat, arcu diam laoreet leo, venenatis facilisis nibh turpis
            vitae urna. Donec eget eleifend turpis. Fusce vestibulum leo lectus, ac
            semper mauris ornare vitae. Nam eleifend erat accumsan eros malesuada,
            eget blandit dui mollis. Curabitur sit amet venenatis risus. Integer eu
            lobortis ante, ut tincidunt nibh. Nunc non dignissim purus.
        </blockquote>
        <!-- A link that takes us to a different page (href = hypertext reference) -->
        <a href="https://lipsum.com">
            <!-- Below, using a span to be able to style the finger differently from the rest of the text -->
            Go to the Lorem ipsum generator <span class="finger">👉</span>
        </a>
    </body>
</html>
```

I've added another paragraph that has some plain text and an `<i>` element inside it. These `<i>` elements are used for _idiomatic text_. Here I've added an attribute, `lang="la"`, that tells the browser that this is a Latin piece of text. It can be particularly helpful for things like screen readers. Also, since it's a separate tag, we can apply different styles to it to those of the surrounding text.

The `<blockquote>` element has a similar attribute applied to it. This element is used to quote someone else, so we'll apply a different set of styles to make that clear to the reader of the page.

Finally, at the bottom, we've added an _anchor_ or `<a>` element to link away to the original site. The `href` attribute is the link that the user will navigate to upon clicking, and inside the element we can put text that will be clickable. Note that I've added a `<span>` element inside it to hold the emoji. That's so we can style that differently. As you'll see, we have to do that to make sure the emoji is properly vertically aligned, to match the rest of the text.

## CSS

If I refresh the site, you can see the page loads without a problem, using the default styles of my browser for each element.

It doesn't look so good, so let's change that!

I'll create a CSS file, which I'll call `style.css`, and link to it from the HTML document. We put links to stylesheets that the HTML page needs in the `<head>` of the document:

```html {8}
<head>
    <!-- The character set the code uses -->
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Page title (shown in the browser window) -->
    <title>Example HTML File</title>
    <!-- Link the CSS file -->
    <link rel="stylesheet" href="style.css" />
</head>
```

Then we can go into `style.css`, and start writing CSS code!

CSS is made up of selectors and properties. A selector tells the browser _which_ elements to modify. A property modifies a particular style of the element(s) selected.

For example:

```css
body {
    font-size: 36px;
}
```

If we write this code and refresh the page, you'll see the fonts have gotten much bigger! We've targeted the `body` element, but notice the font sizes for `h1` and `p` have changed too. This is due to inheritance, which we'll learn more about in the next section.

I don't want my text to be this big though, so I'll add slightly different styles:

```css
/* Target the `body` element of the HTML page */
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 16px;
  max-width: 576px;
  /*
   * Set no margins top and bottom, and equal margins left and right.
   * The left and right margins will be as big as possible,
   * which keeps the `body` centered on the page.
   */
  margin: 0 auto;
}
```

Now we can refresh the page, and we'll see the page looks like a single column, centered on the page. Because we set the maximum with to `576px` and the margins to `0 auto`, the page is centered horizontally. We'll learn more about what all this means later on!

I'm going to add a couple more styles to the paragraphs and the blockquote:

```css
/* Here we're targeting all `p` and `blockquote` elements */
p,
blockquote {
  line-height: 24px;
  margin-bottom: 24px;
}

blockquote {
  /*
   * This short-hand for margin sets all 4 sides at once.
   * It starts at the top and goes clockwise:
   * top: 0, right: 0, bottom: 36px, left: 0
   */
  margin: 0 0 36px 0;
  padding-left: 30px;
  border-left: 6px solid #1c2023;
  font-style: italic;
}
```

Now the text will be more readable, and we've also made the blockquote look a bit more like a blockquote with the border and italics text.

Let's also change the link. Instead of a link, I want this to look like a clickable button.

```css
a {
  /*
   * block elements by default occupy 100% of the width of their container.
   * This also enables margin top and bottom.
   */
  display: block;
  /* width: fit-content makes the block element take up only as much width as needed by its content. */
  width: fit-content;
  margin: 0 auto;
  font-size: 24px;
  padding: 8px 16px;
  background-color: #1c2023;
  color: white;
  text-decoration: none;
  border-radius: 6px;
}
```

In order to make it look even more clickable, we can add different styles when the user is hovering over the link with their mouse. If we add a small shadow when that happens, the link will look much more interactable:

```css
/* Here we're targeting any `a` element, but only while the user is hovering over it with their mouse */
a:hover {
  /*
   * Adds a shadow under the element.
   * The properties shown here are
   *  - horizontal separation (x distance): 0
   *  - vertical separation (y distance): 5px
   *  - blur amount: 15px
   *  - shadow color: black, at 25% opacity
   */
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.25);
}
```

Finally, look at how the finger emoji isn't _quite_ centered with the text. It's just slightly too low!

We have to _nudge_ it into place by adding a bit of spacing underneath and to the left of it:

```css
.finger {
  /* This alters the default position of the icon, by separating it from the bottom and left slightly.
   * We'll learn more about this later in the course!
   */
  position: relative;
  bottom: 0.25rem;
  margin-left: 0.25rem;
}
```

## Conclusion

That's about everything for this lecture! I know we've gone very quickly, but I don't expect you to have learned and understood everything we've talked about just yet. This was more of an introduction, so you start seeing what HTML and CSS can do!
