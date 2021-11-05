---
title: Jinja Includes
slug: jinja-includes
tags:
  - Not started
  - How to
categories:
  - Video
section_number: 11
excerpt: Learn about Jinja includes and how to render one template inside of another.
---

- [x] Set metadata above
- [ ] Start writing!
- [ ] Create `start` folder
- [ ] Create `end` folder
- [ ] Write TL;DR
- [ ] Create per-file diff between `end` and `start` (use "Compare Folders")


# Jinja Includes

[[toc]]

## What are Includes?

An Include in Jinja uses the `include` keyword to render a template and add the rendered contents into the current template.

### Includes vs. Macros

Includes are very similar to macros, with one key difference. An included template has access to the rendering context (and all variables) of the template that's doing the including. Imported macros don't have that.

So when would you use include instead of a macro?

Let's say you have a template you're already displaying as its own page. For example, a list of items in a store.

Now you've decided that, as well as displaying it as its own page, you want to display that same entire template inside another one (e.g. the store page).

You can include the item list page inside the store page, and Jinja will first render the item list page, and put all its contents inside the store page.

### Example

Here's the item list page:

```language-jinja2
<header>
	<p class="brand">Header</p>
	{% if title %}
		<p class="page-title">{{ title }}</p>
	{% endif %}
	<nav>
		<ul class="links">
			<li class="links__link"><a href="#">Home</a></li>
			<li class="links__link"><a href="#">Blog</a></li>
			<li class="links__link"><a href="#">Profile</a></li>
		</ul>
	</nav>
</header>
```

- `main.j2`

```language-jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
	{% include 'header.j2' %}

	<h1 class="title">{{ title }}</h1>
</body>
</html>
```

## Code written in this lecture
