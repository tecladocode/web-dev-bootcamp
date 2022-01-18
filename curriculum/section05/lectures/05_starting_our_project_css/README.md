---
title: Starting to write our project's CSS file
slug: starting-project-css-file
tags:
  - How to
  - Published
categories:
  - Video
section_number: 5
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Starting to write our project's CSS file

In this lecture, let's continue working on our "Learning HTML" project.

The first thing we're going to do is make a single-line change that is surprisingly impactful on any website: changing the font.

In most operating systems and browsers, the default styles give your HTML pages a serif font like Times New Roman. Although there's nothing wrong with that font, nowadays most operating systems use a very different style of font for their desktop applications.

:::tip Serif and sans-serif typefaces
Serifs are the little extra lines we see attached to the larger strokes of letters in some typefaces. You can see an example below of a typeface with the serifs highlighted.

![A typeface with the serifs highlighted in red.](./assets/Serif_and_sans-serif_03.svg)
<small style="display: block;">Image created by Stannered, <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0 License.</a></small>

Fonts which include these serifs are called serif fonts, and those without are called sans-serif fonts. Sans just means "without".
:::

On modern OS X versions, that font is "San Francisco". On Windows 10, it's "Segoe UI", and on Ubuntu it's a font called "Ubuntu".

If we tell our CSS file to use the "San Francisco" font, then it'll use that font if it's available in the user's computer. That'll likely mean the user is on a computer running OS X.

So if we want our website to use the default font of the user's computer, we can tell it to try the following:

1) Use "San Francisco".
2) If that's not available, use "Segoe UI".
3) If that's not available, use "Ubuntu".
4) If that's not available, use a default sans-serif font.

The `font-family` declaration in CSS allows us to pass a list of fonts, where the first one will be used if available, and if not it'll try the second one. Then the third one, and so on:

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif
```

::: tip
Note that `-apple-system` and `BlinkMacSystemFont` are two ways of referring to the default OS X font. Different browsers use different names, so that's why we're putting both in the declaration.
:::

Let's add the `font-family` declaration to the `body` selector, so that the font will change in the entire page:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
}
```

## Should you use black text?

Completely black text on a completely white background can look a little bit harsh, so something that we do quite frequently is make the black _slightly grey_. You can also make it a dark shade of blue (or any other colour).

In this case, let's go for `#002244`, a dark shade of blue. It'll be almost unnoticeable, but your users will thank you long term!

We can add the `color` property to the `body` selector as well:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
  color: #002240;
}
```

## Improving paragraph readability

Finally, I feel like the default styles for paragraphs result in lines that are very close together. I like to separate my paragraph lines a bit more than normal to improve readability.

We can do this with the `line-height` declaration:

```css
p {
  line-height: 150%;
}
```

That's about it! We've improved the look of our page quite a bit, but we still have more work to do.

In the next few lecture we're going to look at inheritance and spacing around and within elements. With that knowledge, we'll be able to improve the look of our site even further!