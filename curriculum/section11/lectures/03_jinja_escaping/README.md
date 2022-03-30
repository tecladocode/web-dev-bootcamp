---
title: Jinja Escaping
slug: jinja-escaping
tags:
  - Written
  - How to
categories:
  - Video
section_number: 11
excerpt: Escaping in Jinja allows us to treat code that would be parsed by either Jinja or the browser, and tell them to treat it as plain text to be displayed instead.
draft: true
---

# Jinja Escaping

Sometimes we may need to include some text in our HTML templates that Jinja2 will want to parse. For example, if we're writing a tutorial about Jinja2!

```jinja2
<p>This is how you write a Jinja2 for loop:</p>

<pre><code>
{% for user in users %}
	<p>{{ user['name'] }}</p>
{% endfor %}
</code></pre>
```

If we do this, Jinja2 will try to run through the loop and evaluate it. If we don't pass in a `users` variable, we'll get an error.

This is where the Jinja2 `raw` block comes in handy:

```jinja2
<p>This is how you write a Jinja2 for loop:</p>

<pre><code>
{% raw %}
{% for user in users %}
	<p>{{ user['name'] }}</p>
{% endfor %}
{% endraw %}
</code></pre>
```

For more information, please check the [official documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/#escaping).

## `raw` vs `safe` and `e`

The `raw` block tells Jinja2 to _not_ render the Jinja2 code before sending it to the user.

The `e` block _escapes_ HTML code so that the browser doesn't use it to paint in the browser window (it doesn't run it as HTML).

The `safe` block _unescapes_ HTML code that has been previously escaped, so that the browser _does_ use it and run it as HTML.

Do you need to use both `safe` and `e`? 

No. Just use one of the two, depending on your application settings.

As of Jinja 3, **autoescaping is disabled** when used on its own, but **autoescaping is enabled in Flask apps**[^flask_autoescaping] in certain templates. You don't need to escape variables in `.html`, `.htm`, `.xml`, or `.xhtml` templates.

You do need to escape variables if you use `.jinja2`, `.j2`, or `.jinja` templates.

- `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

html_code = """<div><p>This is a <strong>Test</strong>.</p></div>"""


@app.route("/")
def home():
    return render_template("main.jinja2", html_code=html_code)
```

- `main.jinja2`

```jinja2
<!DOCTYPE html>
<html>
<head></head>
<body>
<div>
{{ html_code }}

{{ html_code | safe }}

{{ html_code | e }}

{% raw %}
{{ html_code }}
{% endraw %}
</div>
</body>
</html>
```

- Here's the browser output:

```html
<html><head></head>
<body>
<div>
<div><p>This is a <strong>Test</strong>.</p></div>

<div><p>This is a <strong>Test</strong>.</p></div>

&lt;div&gt;&lt;p&gt;This is a &lt;strong&gt;Test&lt;/strong&gt;.&lt;/p&gt;&lt;/div&gt;


{{ html_code }}
</div>

</body></html>
```

In my code, autoescaping is disabled (as is by default). Therefore, the `| safe` filter doesn't do anything. It unescapes something that has been escaped, but nothing's been escaped.

The `| e` filter does do something: it escapes the HTML. Then the browser treats it as text that it doesn't have to run--it just displays it.

I've included the `raw` block in there to show you that that simply displays `{{ html_code }}`. Jinja2 never ran that, so it is shown as plain text.

If you disable autoescaping (which the documentation suggests [would result in a performance boost](https://jinja.palletsprojects.com/en/3.0.x/templates/#html-escaping)), then you **should** escape all potentially unsafe strings, such as those that could contain untrusted HTML code. For example, any text that is coming from your users.

<BottomCallout></BottomCallout>

[^flask_autoescaping]: [Jinja setup (Flask docs)](https://flask.palletsprojects.com/en/2.0.x/templating/#jinja-setup)