---
title: "HTML forms: sending form data"
slug: html-forms-sending-form-data
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# HTML forms: sending form data

Let's continue the Microblog project by working on the form users will submit to create new entries.

HTML forms have 3 main parts to them:

- The `<form>` element itself, which describes how the form behaves in terms of sending data.
- A button used to submit the form, and send data as described in the `<form>` element.
- Form inputs, each of which is comprised of a label and a field.

Let's begin by talking about the `<form>` element itself.

## The form element

There are two ways of submitting data in forms: using a `GET` request (the default), or using a `POST` request. This is called the **method**.

In addition to the method, we can specify an **action**, which is the URL that will receive the form data.

This form uses `GET`, and the form data is sent to `/entry`:

```html
<form action="/entry"></form>
```

If we don't specify an `action` attribute, then data is sent to the _current URL_:

```html
<form></form>
```

We can manually specify the method (with or without an action):

```html
<form method="GET" action="/entry"></form>
```

And we can use `POST` instead of `GET`:

```html
<form method="POST" action="/entry"></form>
```

## Sending data with a form

But what are the differences between `GET` and `POST`? To understand this, let's add a text field and a submit button to our form:

```html
<form>
    <label for="sample-field">Sample:</label>
    <input type="text" name="sample" id="sample-field" />
    <button type="submit">Submit</button>
</form>
```

If we open an HTML file containing this with our browser, we'll see something like this:

IMAGE

Let's type something in our field, and press Submit:

IMAGE

Now notice that the page seemingly refreshes. The form is emptied. That's because the form sent the data to the URL defined in the `action` attribute. But since we didn't add an `action` attribute, the default is the _current URL_.

However, notice that the URL changed slightly. We ended up with `?sample=Bob` at the end (if you typed "Bob" in the field).

That is the form data that the form sent to the current URL.

So the form sent the data to the current URL, which means that it made another request to our HTML file. Our HTML file doesn't _use_ the form data for anything (we'll learn how to do that later), so all that happened is the browser loaded the HTML contents and painted them again.

### GET requests and query string parameters

Whenever we send form data using `GET`, the data will be appended to the URL as query string parameters.

Query string parameters are key-value pairs appended at the end of a URL. They are a standard way of sending non-sensitive data in web requests.

If you have more than one, they'll be separated by ampersands:

```
?sample=Bob&last_name=Smith
```

### POST requests

If we change the form's `method` to `"POST"`, reload the page, and submit again, you'll see no query string parameters.

When we send data with `POST`, data is included in the **body**, a different part of the request, instead of being part of the URL.

Data in the body is a bit more secure because it's not visible in the URL. For sensitive information, we should use `POST`.

Also, there are limits to the size of URLs which means that for very long forms, `GET` might not be viable.

## Conclusion

We've learned how to send data using HTML forms. In a later section, after we learn about back-end development with Flask, we'll learn about how to receive and use form data!