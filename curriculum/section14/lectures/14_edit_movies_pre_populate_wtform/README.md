---
title: Editing movies and pre-populating a form
slug: edit-movies-prepopulate-wtform
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn about pre-populating WTForm forms while adding movie editing functionality to our app.
draft: true
---


# Editing movies and pre-populating a form

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/f1ab983f36ca49088c491b771d9580aa](https://diff-store.com/diff/f1ab983f36ca49088c491b771d9580aa)
:::

Now that we've create the `ExtendedMovieForm` for movie editing, let's add a Flask endpoint to serve it to our users and handle form submissions, as well as a template to display the form.

## The Flask endpoint for editing movies

We've already rendered a WTForms form before, so doing it again is just the same!

The only new thing is that we want to pre-populate the form with some starting data. For this, it will really help if our `Movie` objects have properties with the same name as the form field names.

In our case, they do! So pre-populating the form will be very easy. All we have to do is pass the `Movie` object that we want to use to pre-populate the form to the `ExtendedMovieForm` constructor when we create it:

```py
@pages.route("/edit/<string:_id>", methods=["GET", "POST"])
def edit_movie(_id: str):
    movie = Movie(**current_app.db.movie.find_one({"_id": _id}))
    form = ExtendedMovieForm(obj=movie)
    if form.validate_on_submit():
        movie.title = form.title.data
        movie.director = form.director.data
        movie.year = form.year.data
        movie.cast = form.cast.data
        movie.series = form.series.data
        movie.tags = form.tags.data
        movie.description = form.description.data
        movie.video_link = form.video_link.data

        current_app.db.movie.update_one({"_id": movie._id}, {"$set": asdict(movie)})
        return redirect(url_for(".movie", _id=movie._id))
    return render_template("movie_form.html", movie=movie, form=form)
```

I've also added the movie-updating functionality here, since it doesn't use anything new.

Note that the form pre-population mechanism is the `obj=movie` part.

## Rendering the extended movie form

First, let's edit the `templates/macros/fields.html` template to add the a new macro in order to render the custom field:

```jinja2
{% macro render_area_field(field) %}
<div class="form__group">
    {{ field.label(class_="form__label") }}
    {{ field(rows=4, class_="form__field", style="resize: none") }}

    {%- for error in field.errors %}
        <span class="form__error">{{ error }}</span>
    {% endfor %}
</div>
{% endmacro %}
```

And then create the `templates/movie_form.html` template:

```jinja2
{% from "macros/fields.html" import render_text_field, render_area_field %}

{% extends "layout.html" %}

{%- block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/forms.css') }}" />
{% endblock %}

{% block main_content %}

    <form name="add_movie" method="post" novalidate class="form">
        <div class="form__container">
            {{ form.hidden_tag() }}
            {{ render_text_field(form.title) }}
            {{ render_text_field(form.director) }}
            {{ render_text_field(form.year) }}

            {{ render_area_field(form.cast) }}
            {{ render_area_field(form.series) }}
            {{ render_area_field(form.tags) }}

            {{ render_area_field(form.description) }}
            {{ render_text_field(form.video_link) }}
    
            <div>
                {{ form.submit(class_="button button--form") }}
            </div>
        </div>
    </form>

{% endblock %}
```

Finally we can update the anchor tags in the `templates/movie_details.html` template since we now can edit the fields:

```diff
...
                 {% else %}
                     <p><a href="{{ url_for('pages.watch_today', _id=movie._id) }}" class="watched__link">Not watched yet</a></p>
                 {% endif %}
-                <a class="movie__edit" href="#">Edit {{ pencil("pencil") }}</a>
+                <a class="movie__edit" href="{{ url_for('pages.edit_movie', _id=movie._id) }}">Edit {{ pencil("pencil") }}</a>
             </div>
         </div>
         <div class="header__row">
...
```

```diff
...
     {% if movie.description %}
         <p class="movie__description">{{ movie.description }}</p>
     {% else %}
-        <p class="movie__description">No description yet. <a class="link" href="#">Add one?</a></p>
+        <p class="movie__description">No description yet. <a class="link" href="{{ url_for('pages.edit_movie', _id=movie._id) }}">Add one?</a></p>
     {% endif %}
...
```

Also nothing new here!

Note that our custom WTForm field is identical to the `TextAreaField`, except when it comes to receiving form data and putting it in our Python object. Everything else behaves the same way as the parent class.

That's it! There we have movie editing functionality added!

