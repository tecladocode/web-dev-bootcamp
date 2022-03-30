---
title: Set the last watched date
slug: setting-last-watched-date
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: "Learn how to easily set the last watched date for a movie, using today's date as a value."
draft: true
---


# Setting the last watched date

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/44ccd7a46e9848ebae94d350f32aec48](https://diff-store.com/diff/44ccd7a46e9848ebae94d350f32aec48)
:::

At the moment we're showing "Not watched yet" on every movie. If the have a date in the database for when the movie was last watched, we're using it, formatted with `%d %b %Y`.

In this lecture we will make both of those pieces of data clickable, and we will update the movie's last watched date using today's date as a value.

First, let's create an endpoint that, when clicked, will update the movie's last watched date.

## Create the Flask endpoint to update a movie watched date

Using what we learned in the last lecture, we can update the movie watched date with `$set` in MongoDB. We'll then pass in a Python `datetime` object (supported natively by `pymongo`), and that's it!

```py
@pages.get("/movie/<string:_id>/watch")
def watch_today(_id):
    current_app.db.movie.update_one(
        {"_id": _id}, {"$set": {"last_watched": datetime.datetime.today()}}
    )

    return redirect(url_for(".movie", _id=_id))
```

## Use the date update link in the template

All we have to do in our template is add this link in, remembering to pass the movie ID:

```diff
 <div class="movie__watched">
     {% if movie.last_watched %}
         <p>
-            Last watched: <a href="#" class="watched__link">
+            Last watched: <a href="{{ url_for('pages.watch_today', _id=movie._id) }}" class="watched__link">
                 <time datetime="{{ movie.last_watched }}">{{movie.last_watched.strftime("%d %b %Y")}}</time>
             </a>
         </p>
     {% else %}
-        <p><a href="#" class="watched__link">Not watched yet</a></p>
+        <p><a href="{{ url_for('pages.watch_today', _id=movie._id) }}" class="watched__link">Not watched yet</a></p>
     {% endif %}
     <a class="movie__edit" href="#">Edit {{ pencil("pencil") }}</a>
 </div>
```

That's it! Now when we click this link, we'll trigger the Flask route which updates the date, and refreshes the page. You should be able to see today's date immediately in place of "Not watched yet".