---
title: Which HTML elements can't be nested?
slug: which-html-elements-cant-be-nested
tags:
  - How to
  - Published
categories:
  - Video
section_number: 4
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# Which HTML elements can't be nested?

This is not an easy question to answer, because different elements within a given content category permit wildly different content. For example, the `<a>` element and the `<select>` element are both [phrasing content](../04_html_categories/#phrasing-content); however, the `<a>` element is permitted to contain any non-interactive [flow content](../04_html_categories/#flow-content), while `<select>` is limited to zero or more `<option>` or `<optgroup>` elements.

Navigating this tangle of element relationships is one of the hardest parts about writing good HTML. Luckily there are great resources out there which can help us, such at the [MDN](https://developer.mozilla.org/).

The MDN &mdash; short for **M**ozilla **D**eveloper **N**etwork &mdash; is a great resource for looking up and learning about web technologies. It's an invaluable tool that you should spend some time getting familiar with.

We can look up the page for the `<a>` element [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#Properties), where we can find all kinds of information about the `<a>` element, including its content categories, and its permitted content.

We can do the same thing for `<select>`[^select], `<option>`[^option], `<optgroup>`[^optgroup] too.

If you're unsure whether or not something is valid markup, you should double check the permitted content and permitted parent elements for the elements you're trying to use. Over time you'll have to reference the documentation less and less as you get familiar with the rules surrounding many of the core elements.

::: tip Invalid markup and browsers
Browsers are incredibly forgiving of invalid markup in our HTML code. You're not going to crash your website by putting a `<p>` element inside a `<select>` element, or a `<div>` inside a `<span>`.

While the browser is going to forgive our mistakes, we should still strive to write correct markup. HTML is for describing the content of our page, and if we break the rules for permitted content, we're probably writing something which doesn't make a lot of sense from a semantic viewpoint.
:::

## Heading elements

One very consistent category of elements are those in the heading content category. `<h1>` to `<h6>` elements can *only* contain phrasing content. One interesting side effect of this is that heading elements cannot be empty.

To quote [the documentation](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Phrasing_content), plain text is only considered phrasing content in HTML under certain circumstances:

> ... plain text (not only consisting of white spaces characters).

Plain text which contains no characters, or only spaces, is therefore not considered to be phrasing content. That means if we write something like this:

```html
<h1> </h1>
```

This is not valid markup. It makes a lot of sense in this case. How can we have a heading which doesn't have any content? It's completely meaningless, and we can remove it without changing the meaning of the document at all.

[^select]: [The usage of `<select>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select#Technical_summary)
[^option]: [The usage of `<option>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
[^optgroup]: [The usage of `<optgroup>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
