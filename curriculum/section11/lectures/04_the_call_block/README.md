---
title: The call block
slug: the-call-block
tags:
  - Written
  - How to
categories:
  - Video
section_number: 11
excerpt: The call block allows us to pass a macro to another macro.
draft: true
---

# The call block

The call block is used to pass a macro to another macro. This is one of the only ways we have in Jinja to extend the functionality of a macro dynamically.

I know that's a bit vague, so let's look at some examples!

## Call block without arguments
::: v-pre
The example on the [official Jinja2 documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/#call) is very good, and it's a perfect example for using the call block: message dialogs.


Here's a macro that renders a dialog, but notice that inside the contents `div`, we've got a new keyword: `{{ caller() }}`.

```jinja2
{% macro render_dialog(title) -%}
    <div>
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}
```

We use `{{ caller() }}` to get data from the `call` block. This way it's easier to give the `render_dialog` its contents, without passing them as an argument.

```jinja2
{% call render_dialog('Hello World') %}
    This is a <strong>simple dialog</strong> rendered by using a macro and
    a call block.
{% endcall %}
```

This would render into this:

```html
<div>
    <h2>Hello World</h2>
    <div class="contents">
        This is a <strong>simple dialog</strong> rendered by using a macro and
    a call block.
    </div>
</div>
```

If we didn't want to use the call block here, we'd have to add another parameter to the `render_dialog` macro, and do something like this when calling it:

```
{% set contents = "This is a <strong>simple dialog</strong> rendered by using a macro and a call block." | safe %}
{{ render_dialog("Hello World", contents) }}
```

Personally, I prefer using the `call` block here. When used with a well-defined macro, you can almost _treat the `call` block as the very dialog you want to display_. That's great for the readability of the code!

## Call block with arguments

Let's say you've got two pages in your app. In one, you show detailed information about the items a shop sells (item name, stock quantity, price, supplier). In another page, you only show the item names and the amount of stock.

In both cases you need a list of items, but in one case each row has more data.

Here's how we could do this with HTML and Jinja2:

```jinja2
<table>
    {% for item in items %}
        <tr>
            <td>{{ item['name'] }}</td>
            <td>{{ item['stock'] }}</td>
        </tr>
    {% endfor %}
</table>
```

and:

```jinja2
<table>
    {% for item in items %}
        <tr>
            <td>{{ item['name'] }}</td>
            <td>{{ item['stock'] }}</td>
            <td>{{ item['price'] }}</td>
            <td>{{ item['supplier'] }}</td>
        </tr>
    {% endfor %}
</table>
```

Let's also say these two pages are _the only places_ where this information will be stored.

So, it doesn't make sense to make two macros because each macro would only be used in one place. Normally, we make macros to reuse the code.

But there is a part of the code we definitely _can_ reuse: the table and the loop.

We can make that into a macro, and let the caller of the macro define what data to include in each row:

```jinja2
{% macro item_table(items) %}
<table>
    {% for item in items %}
        {{ caller(item) }}
    {% endfor %}
</table>
{% endmacro %}
```

Note that `caller()` is the Jinja keyword, and here we're using it to pass the `item` value to the caller. Let's define the `call` block below.

Assume that `all_items` is a list of all the items in the store. This value would be passed from our Flask app.

```jinja2
{% call(item) item_table(all_items) %}
<tr>
    <td>{{ item['name'] }}</td>
    <td>{{ item['stock'] }}</td>
    <td>{{ item['price'] }}</td>
    <td>{{ item['supplier'] }}</td>
</tr>
{% endcall %}
```

In the page where we require less information about each item, we could just do this:

```jinja2
{% call(item) item_table(all_items) %}
<tr>
    <td>{{ item['name'] }}</td>
    <td>{{ item['stock'] }}</td>
</tr>
{% endcall %}
```

So this is a way to still reduce code duplication in a way that we couldn't do without the `call` block!
:::