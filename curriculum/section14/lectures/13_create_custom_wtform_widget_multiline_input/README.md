---
title: Create a custom WTForm Widget
slug: create-custom-wtform-widget
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Create a custom WTForm Widget to support multiline values in a textarea.
draft: true
---


# Create a custom WTForm widget

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/95d7b638140145b5a9f1307f621da941](https://diff-store.com/diff/95d7b638140145b5a9f1307f621da941)
:::

We're now going to begin working on movie editing. To do this, we'll be creating a longer form where users can change all of the form data.

There are many ways to allow users to change list-style data (the genre, cast, and series info). These range from super simple to extremely complicated.

In the simple end of the scale, we can have a normal input field that sends data to Flask. We could ask users to type CSV data, and then in Flask we would separate the inputs on the comma.

For example, users could type `Keanu Reeves,Carrie-Anne Moss` and we would turn it into two strings, and put that into a list and store it in the database.

In the complex side of the scale, we can have an individual input field for each actor, and then use buttons to add more actors or delete them.

The more complex your user interface becomes, and the more user interactions you want to support, the more likely you are to need JavaScript. That's because browsers run JavaScript code, so if you want to change the number of input fields without refreshing the page, then simply JavaScript is the only way to do it.

I don't want to bring in JavaScript at this point in the course, but I also don't want to use a solution as ugly as asking users to type CSV into a long input field.

## Using a multi-line text area for list-style inputs

My solution is to use a text area, and ask users to type one value per line. That could be one actor, one genre, or another movie in this series.

Now we have again a choice: to do all the processing of the textarea values in the Flask endpoint, or to do it in the `WTForm` form itself.

If we only had one field that had to accept this type of data, I would do it in the endpoint. But since we have three fields, I think it's going to be more effective to do it using `WTForm`.

WTForms already has a `TextAreaField` that we can use for displaying a textarea and getting the text written in it, but it doesn't handle splitting the written text into multiple lines and giving us back a list of strings.

Let's start with that. We'll write a Python class that extends `TextAreaField` and modifies one of its methods:

```py
from wtforms import TextAreaField  # among others


class StringListField(TextAreaField):
    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []
```

With this, when we use `StringListField` in a WTForm, and the form is submitted, it will split the text inside the textarea and set the field's `data` property to the list of strings.

We also need another method: one to go the other way round, from a list of strings into the textarea's content.

Why do we need this method?

Let's say the form is submitted but validation fails. We will re-display the form with the form data that the user already wrote. But by the time we do that, this class will already have set `self.data` to the list of strings, and it won't be able to turn it back into text to put in the HTML field.

We can add a `_value()` method to the class that takes care of formatting `self.data` into a single string that can be placed inside the textarea:

```py
class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []
```

That's it for our custom field! Those two methods do everything we need.

## Create an extended movie form

Now let's create our movie editing form, similarly to how we created the `MovieForm`:

```py
from wtforms import URLField  # among others


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")
```

::: tip
By extending `MovieForm`, we get to re-use all the previously defined fields and their validation rules. By re-defining the `SubmitField` with the same name, we can easily change its label.
:::

That's it for this lecture! In the next few lectures we'll handle rendering this form and validating it.
