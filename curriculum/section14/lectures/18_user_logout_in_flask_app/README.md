---
title: Add user logouts
slug: handle-user-logout-portfolio-project
tags:
    - Written
    - Project
categories:
    - Video
section_number: 14
excerpt: Learn how to add a logout endpoint and what to do when users log out.
draft: true
---

- [ ] Create per-file diff between `end` and `start` (use "Compare Folders")


# Add user logouts to the portfolio project

Handling user logouts is very straightforward: clear the session, and the user will be logged out!

The `session` variable has a `.clear()` method you can call which will do this for you!

In `routes.py`:

```py
@pages.route("/logout")
def logout():
    session.clear()

    return redirect(url_for(".login"))
```

An alternative, if you wanted to keep some data in the `session` but remove other data, could be to do this:

```py
del session["user_id"]
del session["email"]
```

With that, we can include a link in the nav bar to the logout endpoint:

```diff
 <a
-    href="#"
+    href="{{ url_for('pages.logout') }}"
     class="nav__link"
 >
     <span class="nav__item">Log out</span>
 </a>
```