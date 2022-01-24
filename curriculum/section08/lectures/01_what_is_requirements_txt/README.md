---
title: What is requirements.txt?
slug: what-is-requirements-txt
tags:
  - Published
  - Concept
categories:
  - Video
section_number: 8
excerpt: "Learn how to store any dependencies your project needs so that others can easily run it."
draft: false
---

# What is requirements.txt?

For this application we only have two dependencies, so let's create the `requirements.txt` file in the root of the project:

```
flask
pymongo[srv]
```

If you had specific dependencies for development (e.g. a formatter or something ot run your tests), you'd normally place those requirements in another file. You can call that `requirements-dev.txt`.