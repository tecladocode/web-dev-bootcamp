# HTML Element Categories

HTML elements are grouped into content categories based on their function. These categories are important for understanding what constitutes valid markup in HTML. We'll see some example of this in the next lecture when we talk about nesting HTML elements.

Some categories are subsets of other categories. For example, all elements which fall into the *phrasing content* category also fall into the *flow content* category.

We're not going to cover all of the HTML categories here, but there are a few that we should know about.

:::tip Note
Not all HTML elements have a content category. A notable example is the `<html>` element which surrounds all of our HTML markup.
:::

## Flow content

Elements which fall into the flow content category generally contain text or ebedded content such as images or videos.

Almost all HTML elements fall into this category, and every other category we're going to discuss in this section is going to be a special subset of flow content.

Common elements which don't fall within these special subcategories include `<div>` elements, which are used as generic grouping elements, and `<form>` elements.

::: tip Text
Note that plain text is also considered flow content in HTML.

If the text contains more than just whitespace characters, it's also considered phrasing content. This is to distinguish the spaces used for indentation from actual text content.
:::

You can find a complete list of flow content element [here](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Flow_content).

## Sectioning content

Sectioning content includes specific container types for grouping other elements into meaningful collections. This category includes elements like `<article>`, `<section>` and `<nav>`.

`<article>` elements mark some self-contained content within the HTML document. This might be product cards on an e-commerce site, or blog posts. Like many HTML elements, its use case is a lot broader than the name would initially imply.

The `<section>` element is similar to `<article>`, but a `<section>` represents content which wouldn't stand on its own. It requires some additional context.

Note that `<article>` elements can be inside `<section>` elements, but `<section>` elements also make sense inside `<article>` elements, particularly in the context of something like a news report.

`<nav>` is perhaps the most straightforward elemenent in this category to undestand. It's a container for navigation items, like links in a header bar.

::: warning Notable exceptions
One thing to note is that the `<header>`, `<main>`, and `<footer>` elements are not considered sectioning content. Instead, they're considered flow content.
:::

You can find a complete list of sectioning content element [here](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Sectioning_content).

## Heading content

The heading content category is reserved for the six heading elements in the HTML specification. These heading elements represent six levels of heading, and are numerically ordered from 1-6.

The most prominent of these headings is the `<h1>` element, which is usually reserved for something like a page title.

All heading elements can only contain phrasing content.

## Phrasing Content

For the most part, phrasing content represents the text of the document and the elements which mark up that text. However, phrasing content also includes some unexpected elements: `<img>`, `<audio>`, `<video>`, and others. This is because these elements revert to being plain text if the relevant resource can't be retrieved.

All elements which accept phrasing content are expected to have a decendent which contains some amount of plain text, and this is expected to contain content other than whitespace.

You can find a complete list of phrasing content element [here](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#Phrasing_content).
