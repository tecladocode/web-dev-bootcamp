---
title: What is semantic HTML?
slug: what-is-semantic-html
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# What is semantic HTML?

In this lecture we need to talk about an important concept in modern HTML which cuts to the core of what HTML is actually for.

So far we've discussed HTML in the context of describing and structuring the content on the page. When we talk about describing the content of the page, it's worth asking, what features are we interested in describing? And, who are we describing these features for?

## What are we trying to describe?

When writing HTML we're interested in describing the meaning of the page's content, particularly how a given piece of content relates to other content on the page. In other words, we're interested in describing the role a block of content plays in the context of the document.

This is a major departure from older HTML versions, and many other markup languages, where the markup might be largely for presentational purposes. Markdown is an excellent example, which is commonly used for formatting posts on forums and instant messaging services. In the case of Markdown, the markup describes what we want something to look like. This isn't the goal of HTML.

### Default styles
It's worth noting that while HTML is not for describing the appearance of a given page, the HTML elements we use will produce visual changes when we load the HTML page in the browser. This is because different HTML elements have default CSS styles applied to them.

For example, the content inside `<b>` and `<strong>` elements will generally be rendered in bold.

Despite this, you should resist the temptation to use HTML to create these visual effects on your websites. If you want some text to be italicised, you shouldn't just wrap that text in an `<em>` element, because this element has special meaning. It means that the content between the opening closing tags of the element is something we want to emphasise.

There are lots of situations where this might not be inappropriate, for example if we're trying to italicise foreign words, like *etc*., or *per se*. These words are not words we're trying to emphasise because they carry some additional importance.

The correct element to describe these foreign words is `<i>`, but there's no guarantee that this will produce this italicised style. To quote [the documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i#Usage_notes):

> A browser will typically still display the contents of the `<i>` element in italic type, but is, by definition, no longer required to do so.

There may also be words which we want to italicise for no other reason than aesthetics.

In all of these cases, we should be writing CSS to italicise the text, and we should leave the HTML to purely describe the meaning of the document.

## Who are we describing the content for?

When we write HTML, we're generally concerned with describing the content for computers. HTML is machine readable, and programs can be written to decipher pertinent content from an HTML document.

If you go onto a search engine like Google, and you type in a search term, the page titles that you see are taken directly from the HTML, either using content in the HTML `<head>`, or sometimes using the content of the page's `<h1>` element.

HTML is also a vital tool for things like screen readers, and our HTML markup provides context and a means of navigation for people with accessibility issues. Poor markup can makes sites difficult to navigate or understand in this context.

In older versions of HTML, these accessibility concerns were handled using special attributes like ARIA tags, but in HTML5, effective accessibility solutions are baked right into the language.
