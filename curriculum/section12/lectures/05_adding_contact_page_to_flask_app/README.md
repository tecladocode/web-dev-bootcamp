---
title: Adding a contact page to our Flask app
slug: portfolio-add-contact-page
tags:
    - Project
    - Written
categories:
    - Video
section_number: 12
excerpt: 'In this lecture we''ll add a ''contact'' page to our Portfolio project, without e-mail sending functionality.'
draft: true
---


# Adding a contact page to our Flask app

::: tip
List of all code changes made in this lecture: [https://diff-store.com/diff/401766ee7dce439585678a83f6a7e314](https://diff-store.com/diff/401766ee7dce439585678a83f6a7e314)
:::

Let's continue our Portfolio project by working on the contact page. Here, we'll display our contact information. Optionally you could add a contact form here, although that feels a bit too formal and businesslike, rather than belonging to a personal portfolio page.

That's why in our contact page we'll just put links to the three ways to get in touch: e-mail, GitHub, and Twitter.

```html
{% extends 'base.html' %}
{% block content %}
    <main class="main main--contact">
        <dl>
            <div class="contact">
                <dt>Email:</dt>
                <dd class="contact__details">
                    <a class="contact__link" href="mailto:jose@tecladocode.com">
                        jose [at] tecladocode.com
                    </a>
                </dd>
            </div>
            <div class="contact">
                <dt>GitHub:</dt>
                <dd class="contact__details">
                    <a class="contact__link" href="https://github.com/tecladocode">
                        @tecladocode
                    </a>
                </dd>
            </div>
            <div class="contact">
                <dt>Twitter:</dt>
                <dd class="contact__details">
                    <a class="contact__link" href="https://twitter.com/tecladocode">
                        @tecladocode
                    </a>
                </dd>
            </div>
        </dl>
    </main>
{% endblock %}
```

Here we use `dl`[^dl], `dt`[^dt], and `dd`[^dd] elements to construct a list of terms and their descriptions.

We will then style them using this CSS:

```css
.contact {
  display: flex;
  justify-content: center;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  text-align: center;
}

.contact__details {
  /* 1ch is equivalent to the width of the 0 character at the current
       font size. This allows to create a roughly one letter gap bewteen
       the contact label and the associated contact detail */

  margin-left: 1ch;
}

.contact__link {
  color: #000;
  text-decoration: none;

  /* We can modify the text decoration colour and thickness to
       create a custom underline, but the text-decoration-thickness
       property isn't currently supported on Chrome.
       
       Using box-shadow to simulate the underline gives us a
       cross-browser solution. */

  box-shadow: 0 3px 0 0 #4cafda;
}

.contact__link:hover {
  color: #4cafda;
}
```

For each element, we use Flexbox to place the `dt` and `dd` side by side. Then we set a margin of 1 character's width, and style the links with a thicker bottom border. On hover, we change the color of the link text.

[^dl]: [The `dl` element (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
[^dt]: [The `dt` element (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
[^dd]: [The `dd` element (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)