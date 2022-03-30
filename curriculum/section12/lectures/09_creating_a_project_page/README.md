---
title: Creating an individual project page
slug: portfolio-create-project-page
tags:
    - Written
    - Project
categories:
    - Video
section_number: 12
excerpt: In this lecture we create the first project to include in our portfolio page.
draft: true
---

# Creating an individual project page

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/12bfcfcef6654d89a7c57001af8beefd](https://diff-store.com/diff/12bfcfcef6654d89a7c57001af8beefd)
:::

Next up: for each project we've built, we'll write an HTML file.

Another way to do this would be to create a single HTML template for all projects. Then each project would populate the template from a database or even just text in the Python code.

However, different projects may require different layouts, and HTML is already a great language for adding structure and content to a page. Therefore instead of overcomplicating, we can just make a different Jinja template per project and keep it simple!

To create a route that can serve a different file for each project, we'll use the project slugs that we've already defined:

```py
from flask import abort  # among other things

...

slug_to_project = {project["slug"]: project for project in projects}

...

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])
```

Let's use our new endpoint in the `home.html` template:

```diff
 <main class="main main--home">
     <section class="projects">
         {% for project in projects %}
-            <a class="u-bare-link" href="#">
+            <a class="u-bare-link" href="{{ url_for('project', slug=project ['slug']) }}">
                 <article class="project-card">
                     <img
                         class="project-card__image"
                         src="{{ url_for('static', filename=project['thumb']) }}"
                         alt="{{ project['name'] }} hero image"
                     />
```

## The content and HTML

Let's look at what we want our project to display. Remember that since it's an HTML file that we're writing, we can put anything we want in here!

```html
{% extends 'base.html' %}
{% block content %}
    <main class="main main--project">
        <div>
            <img
                class="hero"
                src="{{ url_for('static', filename=project['hero']) }}"
                alt="A hand holding a pen, about to write something in a project planner."
            />

            <article class="project">
                <article class="project__content">
                    <h2 class="project__heading">{{ project['name'] }}</h2>

                    <p>
                        Hi, I'm Bob! I love helping students learn to code and master software development.
                        I've been teaching online for over 6 years, and I founded Teclado to bring software
                        development to everyone—my objective is for you to truly understand everything
                        that goes on behind the scenes.
                    </p>
                    <p>
                        Coding is extremely rewarding. As you learn, things start to click and make sense.
                        You can join the dots of all the things that weren't quite clear before.
                        I'm here to make that journey quick and painless!
                    </p>
                </article>

                <section>
                    <article class="project__meta-group">
                        <h3 class="project__heading project__heading--meta">Technologies used</h3>

                        <ul class="technology-list">
                            <li class="technology-list__item">Python</li>
                            <li class="technology-list__item">HTML</li>
                            <li class="technology-list__item">CSS</li>
                        </ul>
                    </article>

                    <a class="cta" href="{{ project['prod'] }}">
                        <img class="cta__icon" src="{{ url_for('static', filename='img/pointer.svg') }}">
                        View in production
                    </a>
                </section>
            </article>
        </div>
    </main>
{% endblock %}
```

When making multiple project pages, you can always extract parts of this into Jinja macros to reuse them in multiple places.

For example you could extract the sidebar: the technologies and the "View in production" button.

## The CSS

Now we have to style the HTML we've written so that it looks like we want it to!

I'll add the following CSS:

```css
.hero {
  width: 100%;
  margin-bottom: 1.5rem;
}

.project {
  display: flex;
  flex-direction: column;
  font-size: 1.2rem;
  max-width: 50rem;
  padding: 0 1rem;
}

.project__content {
  margin-bottom: 1rem;
  line-height: 150%;
}

@media (min-width: 48.75em) {
  .project {
    flex-direction: row;
    padding: 0;
  }

  .project__content {
    flex: 7;
    margin-right: 3rem;
    padding: 0;
  }
}

.project__heading {
  margin: 0;
  font-size: 2rem;
  line-height: 150%;
}

.project__heading--meta {
  font-size: inherit;
  margin-bottom: 1rem;
}

.project__meta-group {
  margin-bottom: 1rem;
}

.project__meta-group,
.cta {
  padding: 1rem;
  background-color: #d4eafa;
  border-radius: 6px;
}

.cta {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  color: #1c2023;
  text-decoration: none;
}

.cta:hover {
  text-decoration: underline;
}

.cta__icon {
  margin-right: 0.5rem;
  transform: translateY(1px);
}

.technology-list {
  list-style: none;
  padding-left: 0.75rem;
  margin: 0;
  line-height: 1.75;
}

.technology-list__item:before {
  content: "";
  display: inline-block;
  height: 1rem;
  width: 1rem;
  background-image: url("/static/img/list-check.svg");
  background-size: contain;
  background-repeat: no-repeat;
  margin-right: 0.5rem;

  /* necessary for vertical centering */
  transform: translateY(2px);
}
```

But notice that the project page takes up 100% of the width of the window, so what we want to do is constrain it so it only takes up the space needed by its content.

We can do this by changing this:

```css
.main {
  display: flex;
  justify-content: center;
  margin: 0 auto;
}

.main--about {
  flex-direction: column;
  max-width: 500px;
  padding: 0 1rem;
  line-height: 150%;
}
```

I've also changed the `flex-direction` of `.main--about` so that it is a column. Otherwise it would be a row, and the three paragraphs in it would appear side by side.

### New CSS properties

- `background-image`[^mdn_bg_image]: adds an image in the background of an item, taking up the entire content + padding area.
- `background-size`[^mdn_bg_size]: usually one of `cover` (fill element area, stretching the image if necessary) or `contain` (fill element area but without cropping or stretching the image--can result in image tiling).
- `background-repeat`[^mdn_bg_repeat]: if there is image tiling, configures it. For example only horizontally, or not repeating at all.

## Loading the appropriate template in the Flask app

When a user accesses a particular project, they are going to be accessing `/project/project-slug`, where `project-slug` is different for each project.

We'll take the slug, check if it's in our list of projects, and then return the template with name `project_project-slug.html`. If it's not in the list, we'll return a 404 page instead (more on that in the next lecture).

It will be easier if we start off by constructing a dictionary that maps project slugs to projects:

```py
slug_to_project = {project["slug"]: project for project in projects}
```

Then with this we can modify our existing project route:

```py
@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])
```

We'll need to import `abort` from Flask:

```py
from flask import Flask, render_template, abort
```

And with that, when we access `/project/any-project-slug`, that will load the appropriate project template (if it exists), and it will receive the data belonging to that project (again, if it exists).

[^mdn_bg_repeat]: [background-repeat (MDN Documentation)](https://developer.mozilla.org/en-US/docs/Web/CSS/background-repeat)
[^mdn_bg_size]: [background-size (MDN Documentation)](https://developer.mozilla.org/en-US/docs/Web/CSS/background-size)
[^mdn_bg_image]: [background-image (MDN Documentation)](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image)