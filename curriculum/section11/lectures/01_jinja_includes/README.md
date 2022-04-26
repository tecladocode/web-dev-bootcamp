---
title: Jinja Includes
slug: jinja-includes
tags:
  - Written
  - How to
categories:
  - Video
section_number: 11
excerpt: Learn about Jinja includes and how to render one template inside of another.
draft: true
---


# Jinja Includes

[[toc]]

## What are Includes?

An Include in Jinja uses the `include` keyword to render a template and add the rendered contents into the current template.

### Includes vs. Macros

Includes are very similar to macros, with one key difference. An included template has access to the rendering context (and all variables) of the template that's doing the including. Imported macros don't have that.

This means that if you want a macro to have access to a certain variable, you need to pass that value as an argument.

So when should you use an include instead of a macro?

This is a tough one, and to be honest I haven't yet found *any* scenarios where I would use an include over a macro.

I'll show you how includes work real quick, because it is a feature of Jinja and you may come across it in the wild, and then I'll tell you a bit about why I never use them.

### Example 1: including a fragment of a page

An include passes the rendering context to the included template, then renders it, and then copies the _result_ onto the template that did the including.

::: v-pre
Here's `header.html`, a navigation bar that you might find in any page. Note that it uses `{{ title }}` in it, so it needs access to that variable.
:::

```jinja2
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

And here's `main.html`, using that template:

```jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
	{% include 'header.html' %}

	<h1 class="title">{{ title }}</h1>
</body>
</html>
```

When we use `include`, Jinja automatically passes the rendering context--so `header.j2` has access to all the same variables that `main.html` has access to.

Seems like a reasonable thing to do! And it is, but if you are going to use the header in multiple pages, I think it's clearer if we make it a macro:

```jinja2
{% macro header(title) %}
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
{% endmacro %}
```

Then, in `main.html`, we'd call it like this:

```jinja2
{% from 'header.html' import header %}
<!DOCTYPE html>
<html>
<head></head>
<body>
	{{ header(title) }}

	<h1 class="title">{{ title }}</h1>
</body>
</html>
```

I prefer this because it's very clear that `header` uses `title`. Without this, `header` could use `title` but it's not obvious. If later on you want to get rid of `title`, you have to go into _every included template_ to see if they use `title`.

Since using a macro vs. doing an include is basically the same amount of work, I see no reason to use an include over a macro in this instance.

### Example 2: including a whole page

In the first example we looked at including a fragment of a page. Now let's look at including a whole page.

Here's a Jinja template, `items.html`, that renders a list of items that a store has in stock:

```jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
	<h1>Items in this store</h1>
	<ol>
		{% for item in items %}
			<li>{{ item['name'] }} - Stock: {{ item['stock'] }}</li>
		{% endfor %}
	</ol>
</body>
</html>
```

And here's another Jinja template, `store.html`, that renders some information about a store:

```jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
	<h1>Store {{ name }}</h1>
	<p>This store is in {{ address }}. It employs {{ employees | length }} people.</p>
</body>
</html>
```

Now let's say that you want to include the item list in the store information template, _while still keeping it in its own renderable template_.

That means you can't just make it a macro, because macros can't be rendered on their own: they need to be called by a template.

So an idea could be to do this in `store.html`:

```jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
	<h1>Store {{ name }}</h1>
	<p>This store is in {{ address }}. It employs {{ employees | length }} people.</p>

	{% include 'items.html' %}
</body>
</html>
```

And this will work fine.

But the problem starts when `items.html` uses an HTML `head` element. Let's say that our items list template looks like this:

```jinja2
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="{{ url_for('static', filename='css/items.css') }}" />
</head>
<body>
	<h1>Items in this store</h1>
	<ol>
		{% for item in items %}
			<li>{{ item['name'] }} - Stock: {{ item['stock'] }}</li>
		{% endfor %}
	</ol>
</body>
</html>
```

Now when we include it from `store.html`, the resulting HTML looks like this:

```html
<!DOCTYPE html>
<html>
<head></head>
<body>
	<link rel="stylesheet" href="/static/css/items.css" />
	<h1>Store My Store</h1>
	<p>This store is in 2 No Name Street. It employs 17 people.</p>

	<ol>
		<li>Chair - Stock: 3</li>
		<li>Table - Stock: 1</li>
		<li>Pen - Stock: 7</li>
	</ol>
</body>
</html>
```

And this is not valid HTML, because `link` elements should not be inside `body`.

Instead, a better choice would be to extract the item list HTML code into a macro, in say `item-list.html`:

```jinja2
{% macro item_list(items) %}
<ol>
	{% for item in items %}
		<li>{{ item['name'] }} - Stock: {{ item['stock'] }}</li>
	{% endfor %}
</ol>
{% endmacro %}
```

And then use this macro in both places:

```jinja2
{% from 'item-list.html' import item_list %}

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="{{ url_for('static', filename='css/items.css') }}" />
</head>
<body>
	<h1>Items in this store</h1>
	{{ item_list(items) }}
</body>
</html>
```

And:

```jinja2
{% from 'item-list.html' import item_list %}

<!DOCTYPE html>
<html>
<head></head>
<body>
	<h1>Store {{ name }}</h1>
	<p>This store is in {{ address }}. It employs {{ employees | length }} people.</p>

	{{ item_list(items) }}
</body>
</html>
```

Unfortunately these are the only two situation where I could imagine using an include, and in both cases the macro is a better approach. Therefore although you should know that includes exist, you should be aware of its limitations.

If you find a situation where using an include is better than a macro, please let me know! I'm still looking for one!

## What are Jinja partials?

Many people use the term "partial" and "include" interchangeably, but I think that's a small inaccuracy.

A partial (meaning _partial template_) is a Jinja template that is a subset of another template.

Partials can be implemented using macros (as we saw above), or includes.

There are times where you may want to render the partial template on its own, without rendering the template that includes it (or uses the macro).

In those occasions, I would create **a macro template** and **a partial template**, using this structure:

```
templates
  | macros/
  |    - item_list.html
  | partials/
  |    - item_list.html
  | - store.html
```

The partial then would just import the macro and use it, like this:

```jinja2
{% from "macros/item_list.html" import item_list %}

{{ item_list(items) }}
```

This is more verbose than only having a partial, and using `include` in `store.html`, but in exchange it's easier to see where variables are used. Plus, if you have a partial template, you know it's getting rendered on its own in one of your endpoints.

If you used includes for everything and not macros, you wouldn't know which Jinja files are rendered on their own and which are only used in includes.

### Why might you render partials on their own?

In some cases you can render a partial on its own, and then use the resultant HTML to replace existing content on a page, using JavaScript.

That can give you a dynamic feel on your website because the content changes without having to reload the page.

It's a very common pattern when using libraries such as [HTMX](https://htmx.org/docs).
