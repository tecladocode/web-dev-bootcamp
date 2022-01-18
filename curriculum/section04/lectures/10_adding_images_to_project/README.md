---
title: Adding images to our project
slug: adding-images-to-project
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Adding images to our project

Now that we've learned about HTML attributes, let's tackle adding some more code to our HTML project.

Here's the code we're starting with:

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

One of the first attributes we'll add to any page is one describing the human language the page is written in. We normally do this in the `<html>` element, with `<html lang="en">`, like so:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
    </body>
</html>
```

We can also add `lang` attributes to other elements, as required, if they contain text in a different human language.

Image elements require the use of HTML attributes, so let's try our hand at adding some images to this page.

First, you need a small photo of yourself to include in the page. I've taken one and placed it in the same folder as my `index.html` file. I've called the photo `profile.png`.

To add an image, we use the [void](../01_elements/README.md) `<img>` element, like so:

```html
<img src="profile.png" alt="Rolf's profile picture." />
```

This has two attributes:

- `src` is the image we want to display. The value of the attribute is a path to the image. Since the HTML document and the image are in the same folder, we can refer to the image directly by its file name.
- `alt` is the text that is displayed if the image can't load. It's also useful for search engines and accessibility tools.

Remember that we can also add any global attributes, like `class`, to `<img>` elements. I'll add one so that later on we can target the image more easily with CSS:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
    </body>
</html>
```

This is all well and good, but the page is looking a bit bare. Let's add a bit of visual interest with another image. I'll add an image of the code that displays the website.

I like generating my code images using [https://carbon.now.sh](https://carbon.now.sh). You give it the code, and it gives you a nice-looking image of the code. This is what most people use on social media to share code!

Let's go to the website and paste our website code. Select a theme you like, and select HTML in the language dropdown. Then, export the image in 2x size.

Copy the image over to your project folder. I'll call mine `code.png`.

Then we can add another descriptive paragraph, and the image itself:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
    </head>
    <body>
        <img class="profile" src="profile.png" alt="Rolf's profile picture." />
        <h1>I'm learning HTML and CSS!</h1>
        <p>Hello, my name is Rolf Smith. I'm learning about web development, and I'm starting with HTML and CSS.</p>
        <p>With HTML and CSS, I can make all sorts of websites. HTML and CSS are the most important languages to learn!</p>
        <p>This website's code looks like this:</p>
        <img class="code" src="code.png" alt="The HTML code for this page." />
    </body>
</html>
```

Now we've got a complete page!

However, it doesn't look the best. The code image is gigantic compared to everything else, and the default styles for text aren't so pretty.

We'll be making this page look _way_ better when we get to learn about CSS, in the next section!