---
title: Displaying a table of all movies
slug: display-table-all-movies
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to load all movie data and display a table of all movies.
draft: true
---


# Displaying a table of all movies

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/b93744ff420c414aadb2023677d752f4](https://diff-store.com/diff/b93744ff420c414aadb2023677d752f4)
:::

## Load the data from MongoDB
Let's start with getting data from MongoDB and into our template! Let's go to our `index` route:

```py{3,4,9}
@pages.route("/")
def index():
    movie_data = current_app.db.movie.find({})
    movies = [Movie(**movie) for movie in movie_data]

    return render_template(
        "index.html",
        title="Movies Watchlist",
        movies_data=movies,
    )
```

Here I'm creating a `Movie` object with the data coming from the database. By passing each movie using `**movie`, this turns the dictionary from MongoDB into keyword arguments that are fed to the `Movie`'s `__init__` method.

## Display the data in an HTML table
Now that we've passed our movies as the `movies_data` variable to the `index.html` template, we need to create an HTML table to display the data!

There is a limitless number of ways to write the HTML and CSS for this, so I've opted for what I think is a fairly straightforward approach--if maybe not the most flexible. It's great for simpler tables though!

First we'll start with creating the table and defining the columns and their sizes:

```html
{% extends "layout.html" %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
            <colgroup>
                <col style="width: 60%">
                <col style="width: 25%">
                <col style="width: 15%">
            </colgroup>
            <thead>
                
            </thead>
            <tbody>
                
            </tbody>
        </table>
    {% endif %}
{% endblock %}
```

Next, we'll define the headers:

```html
{% extends "layout.html" %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
            <colgroup>
                <col style="width: 60%">
                <col style="width: 25%">
                <col style="width: 15%">
            </colgroup>
            <thead>
                <th class="table__cell table__cell--header">Title</th>
                <th class="table__cell table__cell--header">Release Date</th>
                <th class="table__cell table__cell--header"></th>
            </thead>
            <tbody>
                
            </tbody>
        </table>
    {% endif %}
{% endblock %}
```

Note that I've added four columns, but only three headers. That's because the last column is a "header-less" column since its purpose will be fairly obvious to any user.

And finally, with a `for` loop, put the data in the table:

```html
{% extends "layout.html" %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
            <colgroup>
                <col style="width: 60%">
                <col style="width: 25%">
                <col style="width: 15%">
            </colgroup>
            <thead>
                <tr class="table__header">
                    <th class="table__cell table__cell--header">Title</th>
                    <th class="table__cell table__cell--header">Release Date</th>
                    <th class="table__cell table__cell--header"></th>
                </tr>
            </thead>
            <tbody>
                {% for movie in movies_data %}
                    <tr>
                        <td class="table__cell">
                            <p class="table__movieTitle">{{ movie.title }}</p>
                            <p class="table__movieDirector">By {{ movie.director }}</p>
                        </td>
                        <td class="table__cell">{{ movie.year }}</td>
                        <td class="table__cell"><a href="#" class="table__link">View</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endif %}
{% endblock %}
```

What should we do when `movies_data` is an empty list?

Let's add some text in there to tell users to add a new movie when that happens:

```html
{% extends "layout.html" %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
            <colgroup>
                <col style="width: 60%">
                <col style="width: 25%">
                <col style="width: 15%">
            </colgroup>
            <thead>
                <tr class="table__header">
                    <th class="table__cell table__cell--header">Title</th>
                    <th class="table__cell table__cell--header">Release Date</th>
                    <th class="table__cell table__cell--header"></th>
                </tr>
            </thead>
            <tbody>
                {% for movie in movies_data %}
                    <tr>
                        <td class="table__cell">
                            <p class="table__movieTitle">{{ movie.title }}</p>
                            <p class="table__movieDirector">By {{ movie.director }}</p>
                        </td>
                        <td class="table__cell">{{ movie.year }}</td>
                        <td class="table__cell"><a href="#" class="table__link">View</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p class="table__empty">You haven't added any movies yet. <a href="{{ url_for('pages.add_movie') }}" class="link">Add one!</a></p>
    {% endif %}
{% endblock %}
```

Finally, we also need a way to add new movies even if there is already a movie in there. Let's add a button for that:

```html
{% extends "layout.html" %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
            <colgroup>
                <col style="width: 60%">
                <col style="width: 25%">
                <col style="width: 15%">
            </colgroup>
            <thead>
                <tr class="table__header">
                    <th class="table__cell table__cell--header">Title</th>
                    <th class="table__cell table__cell--header">Release Date</th>
                    <th class="table__cell table__cell--header"></th>
                </tr>
            </thead>
            <tbody>
                {% for movie in movies_data %}
                    <tr>
                        <td class="table__cell">
                            <p class="table__movieTitle">{{ movie.title }}</p>
                            <p class="table__movieDirector">By {{ movie.director }}</p>
                        </td>
                        <td class="table__cell">{{ movie.year }}</td>
                        <td class="table__cell"><a href="#" class="table__link">View</a></td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p class="table__empty">You haven't added any movies yet. <a href="{{ url_for('pages.add_movie') }}" class="link">Add one!</a></p>
    {% endif %}
    
    <a href="{{ url_for('pages.add_movie') }}" class="button button--add">
        <span>+</span>
    </a>

{% endblock %}
```

## Style the table with CSS
Now that we've got all our markup, it's time to get into styling.

Create a CSS file in `movie_library/static/css/movies.css`, and then link it in the `index.html` template:

```html
{% extends "layout.html" %}

{% block head_content %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/movies.css') }}" />
{% endblock %}

{% block main_content %}
    {% if movies_data %}
        <table class="table">
        ...
```

### Styling the floating "add movie" button

The first thing I'll do in our new CSS file is position the "Add movie" button so that it's at the bottom right of the screen, always floating there:

```css
.button--add {
  position: absolute;
  bottom: 4rem;
  right: 2rem;
  display: flex;
  height: 5rem;
  width: 5rem;
  border: var(--border);
  border-radius: 50%;
  color: var(--text-dark);
  text-decoration: none;
  font-weight: 600;
  font-size: 1.75rem;
  align-items: center;
  justify-content: center;
}

@media screen and (min-width: 50em) {
  .button--add {
    right: 3rem;
  }
}

@media screen and (min-width: 80em) {
  .button--add {
    right: 4rem;
  }
}

.button--add:hover {
  color: var(--text);
  background-color: var(--accent-colour);
}
```

Using `position: absolute` makes the button fixed within the screen. Then the `bottom` and `right` properties define how far away from the bottom and right sides of the screen it should be.

In larger screen sizes, I separate it a bit more from the edge so it looks better and not too hidden.

### Styling the movies table
Now let's get to work on the movies table!

First let's limit the maximum width of the table. It doesn't contain a lot of information, so you don't want it to take up too much space horizontally. Otherwise it becomes very difficult to scan:

```css
.table {
  max-width: 50rem;
  width: 100%;
  margin: 0 auto;
  border-spacing: 0;
}
```

::: tip
Setting `border-spacing` to 0 removes the lines between rows and columns, which will help create a cleaner table design. In low-density tables, those lines can make it look busy. The lines do help if you have very dense tables though!
:::

Next let's add some spacing in each cell so the content isn't squished against other cells:

```css
.table__cell {
  padding: 1.25rem 1rem;
}
```

For the header cells, we'll add a bottom border as well as align the text to the left:

```css
.table__cell--header {
  text-align: left;
  padding: 0.5rem 1rem;
  border-bottom: var(--border);
}
```

We can make the title of the movie in the table bold, so that it's easier to notice which part of the table is most important. Similarly for the director, I'll make the text smaller:

```css
.table__movieTitle {
  font-weight: 600;
}

.table__movieDirector {
  font-size: 0.85em;
}
```

Finally let's make the "View" link look a bit more in line with the styling of the app by removing the text decoration. We'll bring it back using the red colour on hover:

```css
.table__link {
  color: inherit;
  text-decoration: none;
}

.table__link:hover {
  text-decoration: underline;
  text-decoration-color: var(--accent-colour);
}
```

When there are no movies and we display a paragraph, let's center it and increase the font size a bit:

```css
.table__empty {
  display: block;
  text-align: center;
  font-size: 1.2rem;
}
```

And that's all the styling we need! A very clean look for our table, which is super readable!

If you want a bit more inspiration for table designs, I really like the Tailwind UI tables which you can see [here](https://tailwindui.com/components/application-ui/lists/tables).