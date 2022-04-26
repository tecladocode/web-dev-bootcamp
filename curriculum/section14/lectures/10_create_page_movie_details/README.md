---
title: Creating the movie details page
slug: movie-details-page
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Display detailed information about a single movie in one page.
draft: true
---



# Create the movie details page

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/ee701882aede4ba4a4e644b1df665825](https://diff-store.com/diff/ee701882aede4ba4a4e644b1df665825)
:::

## Add an endpoint for the movie details page
Let's start by adding an endpoint that will:

1. Retrieve a single movie from the database.
2. Create a `Movie` object with that data.
3. Render a template with that movie data.

```py
@pages.get("/movie/<string:_id>")
def movie(_id: str):
    movie = Movie(**current_app.db.movie.find_one({"_id": _id}))
    return render_template("movie_details.html", movie=movie)
```

## Create the movie details template
Start by creating the `templates/movie_details.html` file. Inside it we'll display information about the movie passed to the template.

While you're here, create a `static/css/movie_details.css` file as well. Leave it empty for now!

Then let's set up our template:

```jinja2
{% from "macros/svgs.html" import star, pencil %}

{% extends "layout.html" %}

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/movie_details.css') }}" />
{% endblock %}

{% block main_content %}
<div class="container">

</div>
{% endblock %}
```

### The movie heading
In the movie details page, the heading is very important. It will show us a few things:

- Title
- Rating
- Last watched date
- Genre
- An edit button so we can add more information to the movie

```jinja2
{% from "macros/svgs.html" import star, pencil %}

{% extends "layout.html" %}

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/movie_details.css') }}" />
{% endblock %}

{% block main_content %}
<div class="container">
    <header class="movie__header">
        <div class="header__row">
            <div class="movie__name">
                <h1>{{ movie.title }}</h1>
                <div class="movie__rating">
                    {{ movie.rating }}
                </div>
            </div>
            <div class="movie__watched">
                {% if movie.last_watched %}
                    <p>
                        Last watched: <a href="#" class="watched__link">
                            <time datetime="{{ movie.last_watched }}">{{movie.last_watched.strftime("%d %b %Y")}}</time>
                        </a>
                    </p>
                {% else %}
                    <p><a href="#" class="watched__link">Not watched yet</a></p>
                {% endif %}
                <a class="movie__edit" href="#">Edit {{ pencil("pencil") }}</a>
            </div>
        </div>
        <div class="header__row">
            <ul class="movie__tags">
            {% for tag in movie.tags %}
                <li class="movie__tag">{{ tag }}</li>
            {% endfor %}
            </ul>
        </div>
    </header>
</div>
{% endblock %}
```

I've set it up as two rows (using `div.header__row`) inside a `header.movie__header` element.

The first row shows the movie title, rating, last watched date, and edit button.

The second row shows the movie tags (or genres).

### The embed video link

If we have already added a video link to our movie, it should be displayed. Note that when we create a new movie, it won't have a video link since the default value for that field is `None`.

Using a Jinja if statement we can display the YouTube embed only if the link is available:

```jinja2
{% if movie.video_link %}
    <iframe
        class="movie__video"
        src="{{ movie.video_link }}"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
{% endif %}
```

### The description, cast, and series information

Finally, we can show a description, cast list, and series information if each is present in the movie data:

```jinja2
{% if movie.description %}
    <p class="movie__description">{{ movie.description }}</p>
{% else %}
    <p class="movie__description">No description yet. <a class="link" href="#">Add one?</a></p>
{% endif %}

<div class="movie__meta">
    {% if movie.cast %}
        <div class="movie__casting">
            <h2>Casting</h2>
            <ul class="list">
            {% for actor in movie.cast %}
                <li class="list__item">{{ actor }}</li>
            {% endfor %}
            <ul>
        </div>
    {% endif %}
    {% if movie.series | length %}
        <div class="movie__series">
            <h2>Series</h2>
            <ul class="list">
            {% for movie_in_series in movie.series %}
                <li class="list__item">{{ movie_in_series }}</li>
            {% endfor %}
            <ul>
        </div>
    {% endif %}
</div>
```

### The completed code

Below is the full code for our movie details page!

```jinja2
{% from "macros/svgs.html" import star, pencil %}

{% extends "layout.html" %}

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/movie_details.css') }}" />
{% endblock %}

{% block main_content %}
<div class="container">
    <header class="movie__header">
        <div class="header__row">
            <div class="movie__name">
                <h1>{{ movie.title }}</h1>
                <div class="movie__rating">
                    {{ movie.rating }}
                </div>
            </div>
            <div class="movie__watched">
                {% if movie.last_watched %}
                    <p>
                        Last watched: <a href="#" class="watched__link">
                            <time datetime="{{ movie.last_watched }}">{{movie.last_watched.strftime("%d %b %Y")}}</time>
                        </a>
                    </p>
                {% else %}
                    <p><a href="#" class="watched__link">Not watched yet</a></p>
                {% endif %}
                <a class="movie__edit" href="#">Edit {{ pencil("pencil") }}</a>
            </div>
        </div>
        <div class="header__row">
            <ul class="movie__tags">
            {% for tag in movie.tags %}
                <li class="movie__tag">{{ tag }}</li>
            {% endfor %}
            </ul>
        </div>
    </header>
    {% if movie.video_link %}
    <iframe
        class="movie__video"
        src="{{ movie.video_link }}"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    {% endif %}

    {% if movie.description %}
        <p class="movie__description">{{ movie.description }}</p>
    {% else %}
        <p class="movie__description">No description yet. <a class="link" href="#">Add one?</a></p>
    {% endif %}
    
    <div class="movie__meta">
        {% if movie.cast %}
            <div class="movie__casting">
                <h2>Casting</h2>
                <ul class="list">
                {% for actor in movie.cast %}
                    <li class="list__item">{{ actor }}</li>
                {% endfor %}
                <ul>
            </div>
        {% endif %}
        {% if movie.series | length %}
            <div class="movie__series">
                <h2>Series</h2>
                <ul class="list">
                {% for movie_in_series in movie.series %}
                    <li class="list__item">{{ movie_in_series }}</li>
                {% endfor %}
                <ul>
            </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

## Style the movie details template

```css
.container {
  max-width: 50rem;
  margin: 0 auto;
}

.movie__header {
  display: flex;
  flex-direction: column;
  margin-bottom: 2.5rem;
}

.header__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.movie__name {
  display: flex;
  align-items: center;
}

.movie__rating {
  margin-left: 1rem;
}

.movie__watched {
  display: flex;
}

.watched__link {
  color: inherit;
  text-decoration: none;
  font-weight: 600;
}

.watched__link:hover {
  text-decoration: underline;
}

.movie__edit {
  display: flex;
  text-decoration: none;
  align-items: center;
  margin-left: 1rem;
  color: inherit;
}

.movie__edit:hover {
  text-decoration: underline;
}

.pencil {
  width: 1em;
  height: 1em;
  margin-left: 3px;
}

.movie__tags {
  list-style: none;
  display: flex;
}

.movie__tag {
  padding: 3px 8px;
  background-color: var(--tag-colour);
}

.movie__tag:not(:first-of-type) {
  margin-left: 1rem;
}

.movie__video {
  width: 100%;
  aspect-ratio: 16/9;
  margin-bottom: 2.5rem;
  box-shadow: 0 5px 15px 0 rgba(0, 0, 0, 0.25),
    0 15px 35px 0 rgba(0, 0, 0, 0.25);
  border-radius: 4px;
}

.movie__description {
  margin-bottom: 2.5rem;
}

.movie__meta {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.list__item {
  margin-top: 1rem;
}
```

## Link to the new endpoint from our table

```diff
             year=form.year.data,
         )

         current_app.db.movie.insert_one(asdict(movie))

-        return redirect(url_for(".index"))
+        return redirect(url_for(".movie", _id=movie._id))
 
     return render_template(
         "new_movie.html", title="Movies Watchlist - Add Movie", form=form
     )
```