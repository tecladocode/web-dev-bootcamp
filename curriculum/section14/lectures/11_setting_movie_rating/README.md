---
title: Setting movie ratings
slug: setting-movie-ratings
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to use Jinja loops and query string parameters to set the movie rating using icons.
draft: true
---



# Setting movie ratings

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/79d93fd986564b0ebebbf65f0f5b5033](https://diff-store.com/diff/79d93fd986564b0ebebbf65f0f5b5033)
:::

At the moment we're showing the movie's rating as a number beside the movie name. We want to show 5 stars instead, with a visual indication as to what the rating of the movie is, out of five.

When we click on one of the stars beside the movie name, we want the app to set the movie's rating to that star rating. So if we click on the middle star, we should set the rating to 3 (out of 5).

Each of the stars therefore needs to trigger something in our Flask app, and that's why each star is a link containing an icon.

In this lecture we will display star icons (coloured appropriately) in the movie details page, instead of just the number. Then we will also code the Flask side of things: what should happen when we click on a star icon.

## Displaying star icons

We want to display 5 stars beside the movie name, all of which will be clickable. Depending on the movie rating, some will be coloured yellow and some will be coloured white. For a rating of 3/5, the first 3 stars will be yellow and the last 2 will be white.

So the first thing to do is to display the five star icons in a row:

```jinja2
{% from "macros/svgs.html" import star, pencil %}

{% for i in range(5) %}
    <a class="rating__link" href="#">
        {{ star("star") }}
    </a>
{% endfor %}
```

We will also need some styling for these. First let's make the `.movie__rating` container `flex`, so that we can lay out its children as a row:

```diff
 .movie__rating {
+  display: flex;
   margin-left: 1rem;
 }
```

Then we will write CSS for the `.rating__link` and the SVG icon. Using `flex` in the container of the icon will let us easily center the icon within the height of the container. Remember to set the icon width and height so that it is actually shown.

::: tip
A word of caution on SVGs: sometimes the SVG code itself contains `fill` and `stroke` colour, and that makes it difficult to modify the colour using CSS. Just remove the `fill` and `stroke` properties from the SVG code so you can set them with CSS (although then you _must_ set them with CSS, as otherwise they'll be transparent).
:::

```css
.rating__link {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: unset;
}

.star {
  width: 1.5em;
  height: 1.5em;
  fill: none;
}

.rating__link:not(:first-of-type) {
  margin-left: 2px;
}
```

Now we've got this, but the icons are not filled even if the rating of the movie is non-zero.

To change the styling of some icons but not others we'll need to give them an additional CSS class, which I'll call `.star--filled`.

### CSS classes in the loop

Since the Jinja loop goes from 0 to 4, what we need to do is:

- Loop at the current loop iteration's index
- If the movie rating is higher than the loop index, then add the `.star--filled` class to the icon
- If it isn't higher, then don't add the class

I'll give you an example with a movie whose rating is 3/5:

- Start the loop from 0 to 4: `{% for i in range(5) %}`
- Draw the first link + star icon.
    - Is `movie.rating > i`?
        - Yes, so give the icon the `.star` and `.star--filled` classes
- Second icon, is `movie.rating > i`?
    - Yes, add `.star` and `.star--filled`
- Third icon, is `.star` and `movie.rating > i`?
    - Yes, add `.star` and `.star--filled`
- Fourth icon, is `movie.rating > i`?
    - No, keep only `.star`
- Fifth icon, is `movie.rating > i`?
    - No, keep only `.star`

As you can see, with this logic we would end up with three icons with `.star` and `.star--filled`, and two icons with only `.star`. If we set the fill colour in `.star--filled`, only the first three icons will have a fill colour, and the movie's rating will be very clear.

Here's how we would write that code:

```jinja2
{% for i in range(5) %}
    <a class="rating__link" href="#">
        {{ star("star " + ("star--filled" if movie.rating > i else "")) }}
    </a>
{% endfor %}
```

And now for the styling for the filled icons:

```css
.star--filled {
  fill: #ffd02a;
}
```

## Handling how to click on an icon link

Now let's work on the Flask side of things. What should happen when one of the icons is clicked?

This is a fairly straightforward endpoint, when you think about it logically.

The link is clicked, and the rating should be passed in the link URL. We'll receive that in Flask, and update the database with the appropriate rating.

```py
@pages.get("/movie/<string:_id>/rate")
def rate_movie(_id):
    rating = int(request.args.get("rating"))
    current_app.db.movie.update_one({"_id": _id}, {"$set": {"rating": rating}})

    return redirect(url_for(".movie", _id=_id))
```

### Passing the movie rating in each icon's link

The tricky bit here is passing the movie rating in each link. In the habit tracker app we already did something like this: use query string parameters.

So what we can do is, in each link, include a `rating` query string parameter equal to the loop's iteration index (plus 1). That will make the first star send a query string parameter with the value of `1`, for example.

Here's how to do that:

```jinja2
{% for i in range(5) %}
    <a class="rating__link" href="{{ url_for('pages.rate_movie', _id=movie._id, rating=i+1) }}">
        {{ star("star " + ("star--filled" if movie.rating > i else "")) }}
    </a>
{% endfor %}
```

Remember that when we use `url_for`, if the arguments we add aren't expected by the endpoint, they'll be passed as query string parameters.

And that's it! With that, we've added the ability to change movie ratings, and we've made them easily visible!