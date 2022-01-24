---
title: 'Key web technologies: HTML, CSS, JavaScript'
slug: key-web-technologies-html-css-javascript
tags:
  - How to
  - Published
categories:
  - Video
section_number: 3
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Key web technologies: HTML, CSS, JavaScript

In this lecture we're going to talk about HTML, CSS, and Javascript. In particular, we're going to talk about what each of these languages is for, and how we use them in modern web development.

## HTML

HTML is a markup language, which means it's for annotating the content of a document. Since the introduction of HTML5, these annotations have had a very specific purpose: to describe the structure and meaning of this content.

This is in stark contrast to older versions of HTML, and many other markup languages, which are concerned with the *appearance* of the content. A good example of this is Markdown, which is commonly used by instant messaging services and forums to change the appearance of text.

Our HTML documents are going to contain the main content of our pages, augmented by annotations in the form of HTML tags. This includes things like images and videos, forms, and of course the text content of our pages.

We'll be covering HTML in a lot of detail in the next section.

## CSS

CSS is used to describe the *presentation* of a document. In other words, it's for changing how things look on our web pages.

Modern CSS is extremely versatile and powerful. We can even create complex animations with nothing but CSS.

CSS uses a system of selectors, which describe *what* we should change the appearance of, combined with property definitions, which describe *how* the appearance of that things should change.

We'll be covering CSS in section 5.

## JavaScript

JavaScript is a fully fledged programming language which is supported by every major browser. This makes it somewhat unique. We can't just execute our Python code in the browser, for example. The browser simply doesn't understand it.

JavaScript is primarily used for handling complex user interactions and manipulating the other code that exists on the page. This might include adding and removing elements or making requests to the server without reloading the page.

::: warning
There's been something of a trend recently to try to do everything with JavaScript, but I actually suggest you avoid JavaScript as much as possible. There are definitely legitimate use cases for JavaScript, but it's important we don't rely on it too heavily for core site functionality.

Many people browse the web with JavaScript disabled in their browser. They do this for security reasons, as JavaScript is a powerful tool, and can be used maliciously. By relying on JavaScript, you are preventing these users from accessing your service. That may be totally fine, but it's something you should consider when making the decision to use JavaScript as an integral part of your site.
:::
