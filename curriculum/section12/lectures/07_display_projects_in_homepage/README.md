---
title: Displaying projects in the portfolio
slug: displaying-portfolio-projects
tags:
    - Not Started
    - Project
categories:
    - Video
section_number: 12
excerpt: In this lecture we move to the Portfolio project homepage to display individual projects there.
draft: true
---

- [x] Set metadata above
- [ ] Start writing!
- [ ] Create `start` folder
- [ ] Create `end` folder
- [ ] Write TL;DR
- [ ] Create per-file diff between `end` and `start` (use "Compare Folders")


# Displaying projects in the portfolio

Let's work on displaying all our projects in the homepage.

For each project, we will display an image, the project title, and some of the technologies we used when developing it.

## The project data

Let's start by defining our projects. To do this, and to keep things simple, I'll just put them together with the Flask app code. You could conceivably store them in a database if you prefer:

```py
projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]
```

Each project has a few properties:

- The `name` is what will be displayed on the homepage.
- The `thumb` is the image shown on the homepage.
- The `hero` is the image shown on each project page.
- The `categories` are shown on the homepage.
- The `slug` is the URL which is unique to each project (e.g. `/project/habit-tracking` would be the URL for the first project).

We also have to pass the projects to the homepage endpoint:

```py
@app.route("/")
def home():
    return render_template("home.jinja2", projects=projects)
```

## The HTML

Now that we've got the project data being passed to `home.jinja2`, let's write the HTML.

```html
{% extends 'base.jinja2' %}
{% block content %}
    <main class="main main--home">
        <section class="projects">
            {% for project in projects %}
                <a class="u-bare-link" href="{{ url_for('project', slug=project['slug']) }}">
                    <article class="project-card">
                        <img
                            class="project-card__image"
                            src="{{ url_for('static', filename=project['thumb']) }}"
                            alt="{{ project['name'] }} hero image"
                        />

                        <header class="project-card__meta">
                            <ul class="categories">
                                {% for category in project["categories"] %}
                                    <li class="categories__tag">{{ category}}</li>
                                {% endfor %}
                            </ul>

                            <h2 class="project-card__name" ">{{ project['name'] }}<h2/>
                        </header>
                    </article>
                </a>
            {% endfor %}
        </section>
    </main>
{% endblock %}
```

Using the `content` block, we define the `main` element as well as a `section` element for the projects.

Then, within a Jinja for loop, we define an `a` element for each project. The entire Project card (image, title, categories, and all the space in between) is clickable. That's why the `a` element encompasses everything else.

Inside the `a` element we've got an `article` for each project, which contains the thumbnail image inside an `img` element, and also a `header` element which contains the categories as a list and the name as an `h2`.

This doesn't look anything like what we want it to look, so let's get to CSS!

## The CSS

```css
.projects {
  display: grid;
  grid-template-columns: 1fr;
  grid-column-gap: 1.25rem;
  justify-content: center;
  justify-items: center;
  max-width: 21.875rem;
  margin: 0 auto;
}

@media (min-width: 48.75em) {
  .projects {
    grid-template-columns: repeat(2, 1fr);
    max-width: 45rem;
  }
}

@media (min-width: 70em) {
  .projects {
    grid-template-columns: repeat(3, 1fr);
    max-width: 68rem;
  }
}

.project-card {
  padding: 0.75rem 0;
}

.project-card__image {
  max-width: 100%;
  margin-bottom: 1rem;
  transition: transform 0.2s ease-in-out;
}

.project-card__meta {
  padding: 0 1.25rem;
}

.project-card__name {
  margin: 0;
  font-size: 1.5rem;
  line-height: 2.25rem;
  color: #1c2023;
}

.project-card:hover .project-card__image {
  transform: translateY(-0.5rem);
}

.project-card:hover .project-card__name {
  text-decoration: underline;
}

.categories {
  display: flex;
  padding: 0;
  margin: 0 0 0.75rem;
  color: #3d84a3;
  list-style: none;
  line-height: 1.45;
  text-transform: uppercase;
  font-size: 1.1rem;
  letter-spacing: 0.075rem;
}

/* Adds an ::after pseudo-element to each category tag, except the last one.
   This psuedo-element contains a pipe character (|), which acts as a seperator
   between the tags. */

.categories__tag:not(:last-of-type)::after {
  content: "|";
  margin: 0 0.25rem;
}

/* Utility class to remove link styles */
.u-bare-link {
  text-decoration: none;
}
```

Here we're using CSS grid to build a 3-column grid to place projects.