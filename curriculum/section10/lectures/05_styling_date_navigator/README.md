---
title: Styling the date navigator
slug: styling-the-date-navigator
tags:
  - Recorded
  - How to
categories:
  - Video
section_number: 10
excerpt: Improve the look and feel of our date navigator using CSS.
draft: true
---


# Styling the date navigator

[[toc]]

## In this video... (TL;DR)

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/0e898f37ca13458ba8cfacba3cfe0fa4](https://diff-store.com/diff/0e898f37ca13458ba8cfacba3cfe0fa4)
:::

## Implementation

At the moment our date navigator looks _not very good_. Let's fix that!

Remember that what we've got to work with here is 7 `a` elements, each one with a `time` element inside it. The `a` elements have a `dates__link` class, and the current date also has a `dates__link--current`  class.

All these elements are inside a `section` element with the `.dates` class.

So let's begin by laying out the container. We'll use flex with a row layout and the `space-around` justification to evenly distribute the elements:

```css
.dates {
  display: flex;
  justify-content: space-around;
  color: #000;
  font-size: 1.1rem;
  margin-bottom: 2.5rem;
}
```

Then we'll style the links themselves, by removing the default styling and adding a border radius and padding:

```css
.dates__link {
  /* Removes the default styles applied to links */
  color: inherit;
  text-decoration: none;
  outline: none;

  padding: 0.25rem 0.75rem;
  border-radius: 6px;
}
```

I'll also add a background colour to the currently selected date, as well as center the text within each date so that the day number and name are centered with respect to each other:

```css
/* Changes the background colour of the current date. This class is applied conditionally by logic in the jinja template */
.dates__link--current {
  background: #f9dba0;
}

/* Ensures the day of the week and the date number sit on top of each other and are centered within the allotted space */
.date {
  display: flex;
  flex-direction: column;
  align-items: center;
}
```

Finally, we'll add some media queries--CSS code that allows us to change properties depending on some condition.

We'll start by hiding the first 2 and last 2 dates, and then our media queries will conditionally show them.

```css
/* Selects the first, second, penultimate and final elements in the dates__link section
and hides them on small screens. As the screen gets larger, we gradually display more 
and more of the date elements.

See the media queries below */
.dates__link:first-of-type,
.dates__link:nth-of-type(2),
.dates__link:last-of-type,
.dates__link:nth-last-of-type(2) {
  display: none;
}

/* Comes into effect when the screen is 400px wide. Reveals the second and second-to-last date link */
@media screen and (min-width: 25rem) {
  .dates__link:nth-of-type(2),
  .dates__link:nth-last-of-type(2) {
    display: block;
  }
}

/* Comes into effect when the screen is 560px wide. Reveals the first and last date link */
@media screen and (min-width: 35rem) {
  .dates__link:first-of-type,
  .dates__link:last-of-type {
    display: block;
  }
}
```

And with that, our styling for the date navigator is done!

## Code written in this lecture

```diff
--- static/css/main.css
+++ static/css/main.css
@@ -70,3 +70,63 @@
   align-self: flex-end;
   border: none;
 }
+
+.dates {
+  display: flex;
+  justify-content: space-around;
+  color: #000;
+  font-size: 1.1rem;
+  margin-bottom: 2.5rem;
+}
+
+.dates__link {
+  /* Removes the default styles applied to links */
+  color: inherit;
+  text-decoration: none;
+  outline: none;
+
+  padding: 0.25rem 0.75rem;
+  border-radius: 6px;
+}
+
+/* Selects the first, second, penultimate and final elements in the dates__link section
+and hides them on small screens. As the screen gets larger, we gradually display more 
+and more of the date elements.
+
+See the media queries below */
+.dates__link:first-of-type,
+.dates__link:nth-of-type(2),
+.dates__link:last-of-type,
+.dates__link:nth-last-of-type(2) {
+  display: none;
+}
+
+/* Comes into effect when the screen is 400px wide. Reveals the second and second-to-last date link*/
+@media screen and (min-width: 25rem) {
+  .dates__link:nth-of-type(2),
+  .dates__link:nth-last-of-type(2) {
+    display: block;
+  }
+}
+
+/* Comes into effect when the screen is 560px wide. Reveals the first and last date link */
+@media screen and (min-width: 35rem) {
+  .dates__link:first-of-type,
+  .dates__link:last-of-type {
+    display: block;
+  }
+}
+
+/* Changes the background colour of the current date. This class is applied conditionally
+by logic in the jinja template */
+.dates__link--current {
+  background: #f9dba0;
+}
+
+/* Ensures the day of the week and the date number sit on top of each other and are
+centered within the allotted space */
+.date {
+  display: flex;
+  flex-direction: column;
+  align-items: center;
+}
```