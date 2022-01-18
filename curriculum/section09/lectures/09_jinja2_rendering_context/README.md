---
title: The Jinja2 Environment and Rendering Context
slug: jinja2-environment-rendering-context
tags:
    - Concept
    - Published
categories:
    - Video
section_number: 9
excerpt: Learn what names Jinja2 has access to during rendering by looking at the Environment and Context.
draft: false
---

# Jinja2 Environment and Context

The Environment and Context are two key parts of how Jinja evaluates templates.

The Environment contains things like the available **filters**, **configuration**, or **tests** (and more). The Context contains the variables that will be available in the rendered template, as well as any exported variables from evaluating the template (such as macros).

Something important to note is that if we render one template and pass it a Context, but that template tries to import something from another, the latter won't have access to the Context. It will have access to the Environment though. When we include a template, it does have access to the Context by default.

This means that the Context is used on a per-template basis, but the Environment is global to all templates.

It is because of this that the Environment has a `globals` property that can contain variables to be shared across all rendered templates.

## How we use the Environment and Context

When we pass in values to the `render_template` function, that adds values to the Context. Similarly, we can also tell Flask to add values to the Context through a few other means.

In addition, both Flask[^flask_filters] and Jinja2 provide values that are included in the Environment's `filters`[^builtin_filters] and `tests`[^builtin_tests] by default.

Flask also adds some values to the context that is passed to every rendered template as well.

Jinja2 provides some builtin functions[^builtin_functions] which are part of the Environment, and are global.

## Flask context values

When we call `render_template` in a Flask app, Flask passes the following values to the Context of the rendered template:

- `config`: the current configuration object of our Flask app, `flask.config`.
- `url_for()`: a function used to generate URLs given a Flask endpoint function name.
- `get_flashed_messages()`: a function used to retrieve the messages that have been stored in the flashed messages stack.

Flask will also add the following, if the template is rendered with an active request context (i.e. within a Flask endpoint):

- `request`: the current request object, `flask.request`.
- `session`: the current session object, `flask.session`.
- `g`: the request-bound object for global variables, `flask.g`.

It's important to note that these are in the Context, and not in the Environment. As such, if your rendered template imports or includes another template, that template won't have access to any of these variables by default.

## Adding values to the context

### With `render_template`

We've already discussed how to add new values to the Context using `render_template`: pass them in as keyword arguments.

```py
...
return render_template("home.html", name="Bob")
...
```

If you do that, the template's Context's `vars` dictionary will have `{"name": "Bob"}` inside it. You can then interpolate `{{ name }}`, and Jinja will be able to find the correct value from there.

### With context processors

If you want to include variables in every template you render, without having to pass them manually as keyword arguments to `render_template`, then you can use a context processor, like so:

```py
@app.context_processor
def latest_posts():
    return {"latest": database.get_posts(limit=3, sort="date")}
```

Note the code above assumes that `database` exists and it returns a list with the latest 3 posts.

## Registering filters with the Environment

If you want a particular template to use a particular Python function, you can pass it in as a keyword argument. This would add it to the Context for that template:

```py
def format_currency(value, currency):
    return f"{amount:.2f}{currency}"

@app.route("/")
def home():
    return render_template("home.html", format_currency=format_currency)
```

::: v-pre
Then, within the template, you could do `{{ format_currency(15.67, "£") }}`.
:::

However, if you want that same function to be available to _all_ templates, you could register a filter. This would add it to the Environment that Flask uses to render templates.

The difference is that you'd have to use it as a filter instead of as a function call. This is how that would work:

```py
@app.template_filter("format_currency")
def format_currency(value, currency):
    return f"{amount:.2f}{currency}"

@app.route("/")
def home():
    return render_template("home.html")
```

::: v-pre
That template (and all other templates) would be able to use the filter like so: `{{ 15.67 | format_currency("£") }}`.
:::

Note that when defining custom filters, the value before the pipe (`15.67` in this case) is passed as the first argument.

# Conclusion

We've learned how the Environment and Context work, as well as how they're different from each other.

If you want to:

- Pass a particular piece of data to a specific template, pass it as a keyword argument when using `render_template`.
- Pass data to all templates you are rendering, use a context processor.
- Allow access to a function in all your templates, consider registering a filter.


[^jinja2_context]: [The Context (Jinja Official Documentation)](https://jinja.palletsprojects.com/en/2.11.x/api/#the-context)
[^builtin_filters]: [List of Builtin Filters (Jinja Official Documentation)](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-filters)
[^flask_filters]: [Standard Filters (Flask Official Documentation)](https://flask.palletsprojects.com/en/1.1.x/templating/#standard-filters)
[^builtin_tests]: [List of Builtin Tests (Jinja Official Documentation)](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-builtin-tests)
[^builtin_functions]: [List of Global Functions (Jinja Official Documentation)](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-global-functions)
