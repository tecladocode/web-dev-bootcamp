---
title: Front end vs. back end development
slug: frontend-vs-backend-development
tags:
  - How to
  - Published
categories:
  - Video
section_number: 3
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Front end vs. back end development

When you first start learning about web development, you'll very quickly encounter the terms *front end* and *back end* development. This can often be an area of confusion for new students, so it's worth spending a little time to understand what these terms mean.

## Front end development

Front end development concerns everything that a user interacts with directly. In web development this means the things the user sees and does within the browser window.

It's the content on the page: the images, buttons, text, etc.

The code we write to produce this interface and behaviour is sometime called *client-side* code, because it executes in the user's browser.

The languages we use to write this code in modern web development are are HTML5, CSS3, and JavaScript, each of which fills a specific role. We'll talk about these technologies in detail in the next lecture and throughout the next couple of sections.

::: warning Compatibility
Because our HTML, CSS, and JavaScript executes in the user's browser, it's up to the browser vendors to implement the behaviour defined in the specifications for these languages.

While there's a single description of how these features should work, different browsers sometimes interpret this specification differently. Older browsers may also lack support for newer features of these languages.

Browser compatibility is a big part of writing front end code, so make sure that you're testing things in several browsers as you work through the course!
:::

## Back end development

The back end is the other side of the coin. When we do things in the browser which trigger requests to a server &mdash; such as when we submit a form &mdash; the back end code is what handles and responds to this request.

Back end or *sever-side* code is predominantly concerned with storing informating and controlling the flow of data. This might mean restricting access to certain pages, storing and retrieving user information, or dynamically populating pages with content.

Many languages can be used for writing back end code, such as Ruby, JavaScript, Go, and PHP. In this course, we're going to be using Python, and a framework called Flask, which making writing backend code in Python much easier.
