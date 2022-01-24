---
title: Jinja Whitespace Control
slug: jinja-whitespace-control
tags:
  - Written
  - How to
categories:
  - Video
section_number: 11
excerpt: "Learn about the whitespace that Jinja adds automatically, and how to remove it if you don't want it!"
draft: true
---

# Jinja Whitespace

When we use Jinja blocks, we may end up with some unwanted whitespace when the blocks get evaluated.

Take a look at this example:

```jinja2
<div>
    {% if True %}
        yay
    {% endif %}
</div>
```

Renders into this:

```html
<div>
    
        yay
    
</div>
```

The whitespace that has been preserved could be classified as:

1. Space between `<div>` and the start of the `if` block.
2. Space between the end of the `if` block and the start of the line inside it.
3. Space between the start of the line and the text, "yay".
4. Space between the end of the line and the start of the `endif` block.
5. Space between the end of the `endif` block and the `</div>`.

99% of the time, we don't want this spacing.

Although HTML will then remove most of the whitespace for us, this can result in a few problems:

- The code in the browser inspector will be bloated and difficult to inspect.
- Sometimes the newlines will not be removed by HTML, depending on where they are. This can lead to janky layouts.
- If we're working with Jinja2 on something other than HTML (e.g. plain text), then the weird spacing will remain.

### How to remove Jinja spacing around blocks

We can use the `-` operator in Jinja blocks to remove some or all of the spacing.

To get rid of (1) above:

```jinja2
<div>
    {%- if True %}
        yay
    {% endif %}
</div>
```

Renders into this:

```html
<div>
        yay
    
</div>
```

To get rid of (2) and (3) above:

```jinja2
<div>
    {% if True -%}
        yay
    {% endif %}
</div>
```

Renders into this:

```html
<div>
    yay
    
</div>
```

We can't get rid of (2) but not (3) using the `-` operator. To do this, we must use an application-wide setting that we'll look at in a moment.

We can do the same with the closing block: `{%- endif %}` would get rid of spacing (4), and `{% endif -%}` would get rid of spacing (5).

Applying all of the whitespace removal signs, we end up with this:

```jinja2
<div>
    {%- if True -%}
        yay
    {%- endif -%}
</div>
```

Which renders:

```html
<div>yay</div>
```

### Settings we can change to automate this

Adding `-` signs everywhere may not be what we want, so there are some settings we can change to automate some of this:

- `lstrip_blocks`
- `trim_blocks`

Here's how we'd set these in a Flask app:

```python
app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
```

With **these two settings enabled**, we can make all the spacing caused by the blocks themselves to be removed. The spacing inside the content is not removed:

```jinja2
<div>
    {% if True %}
        yay
    {% endif %}
</div>
```

```html
<div>
        yay
</div>
```

Note that this is the only way to remove spacings (1), (2), (4), and (5), without removing (3).

In addition to this you can use the `-` sign to remove spacing within the content if desired. Note that this does not remove the spacing after the `div` and after the `yay`, as that is usually not desired:

```jinja2
<div>
    {% if True -%}
        yay
    {% endif %}
</div>
```

```html
<div>
yay
</div>
```

And you can also include the `-` sign at the start of the blocks to remove the newlines after the `div` element and after the `yay` text:

```jinja2
<div>
    {%- if True -%}
        yay
    {%- endif %}
</div>
```

```html
<div>yay</div>
```