---
title: Hiding our MongoDB details from GitHub
slug: hiding-our-mongodb-details-from-github
tags:
  - Project
  - Published
categories:
  - Video
section_number: 8
excerpt: "Learn how to share your sensitive data with Heroku, without storing it in your GitHub repository."
draft: false
---

- [Hiding our MongoDB details from GitHub](#hiding-our-mongodb-details-from-github)
  - [In this video... (TL;DR)](#in-this-video-tldr)
  - [Code written in this lecture](#code-written-in-this-lecture)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
    - [Step 3](#step-3)
    - [Step 4](#step-4)
    - [Step 5](#step-5)

# Hiding our MongoDB details from GitHub

## In this video... (TL;DR)

Let's look at the steps we need to take to hide our MongoDB details from our GitHub repo.

We will use environment variables to do so.

By defining the environment variables in Heroku _and in our local computers_, we can take them off our code. That way, the sensitive data is in Heroku and our computers, but not in our code.

Therefore, when we share our code in GitHub, the data won't be there.

::: warning
If you have already put your MongoDB details in your repository, then that data will still be there even if you change the files.

What you should do is re-generate your MongoDB username and password if you ever want to make your repository public.
:::

## Code written in this lecture

### Step 1

Create a `.env` file in our project and place this in it:

```
MONGODB_URI=mongodb+srv://<user>:<password>@<mongodb-server>/microblog
```

### Step 2

- Install `python-dotenv` and add it to `requirements.txt`

Then load the environment variables in `app.py` (before the `create_app()` function)

```diff
+from dotenv import load_dotenv

+load_dotenv()
```

### Step 3

Instead of the MongoDB URI we've got as a string, use the environment variable by reading it from `os.environ.get()`:

```diff
+import os

 def create_app():
     app = Flask(__name__)
-    client = MongoClient("mongodb+srv://<user>:<password>@<mongodb-server>/microblog")
+    client = MongoClient(os.environ.get("MONGODB_URI"))
     app.db = client.microblog
```

### Step 4

We *do not* add this `.env` file to GitHub since it contains our private MongoDB details. Instead, we'll create a `.env.example` file and add that.

That file should contain just *what* should be added, but no actual values:

```diff
MONGODB_URI=
```

### Step 5

Since we haven't added `.env` to Heroku, Heroku won't know what our MongoDB URI is.

Therefore we must tell it.

Instead of using the `.env` file in Heroku, we'll just give Heroku the value of our environment variable. Heroku can store it internally and use it, even without the `.env` file.