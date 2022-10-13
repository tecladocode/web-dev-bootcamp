---
title: How websites work
slug: how-websites-work
tags:
  - How to
  - Published
categories:
  - Video
section_number: 3
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# How websites work

## A lightning tour of the Internet

Before we start creating websites of our own, it pays to have a rough idea of what goes on in the background when we type a URL in the address bar of our web browsers. It actually takes a surprising amount of work!

### Step 1: Finding the IP address of the domain

We're used to accessing websites using addresses like `www.google.com` and `www.facebook.com`, but our browsers don't make use of these domain names directly. Instead they use IP addresses, which are used to identify Internet connected devices.

When we type the URL for a given site, our browser has to figure out which IP address corresponds to the site we're trying to access. This process is called *domain name resolution*.

Your browser does this through the use of a DNS (or **D**omain **N**ame **S**ystem) server, which checks an index of URLs and corresponding IP addresses. This index is a little like a phone book for computers.

For sites you've visited before, IP addresses can often be found in one of several local caches, starting with the one maintained by your browser. Your operating system and router also maintain caches like this to help speed up the process of name resolution.

If a matching record isn't found in one of these caches, it's up to your Internet service provider to tell your browser the IP address of the site you're hoping to access.

::: tip IP addresses
IP stands for **I**nternet **P**rotocol, and there are two IP versions in common use today: IPv4 and IPv6. IPv6 was created to deal with the rapidly depleting[^ipv6] number of available IPv4 addresses as Internet access became more widespread in the 1990s.
:::

### Step 2: Connecting to the server

Assuming a matching IP address is found, your browser attempts to connect to the web server[^server] for the site you're trying to access.

This is a multi-stage process, but we don't have to worry too much about what happens during this step. Its purpose is to ensure that a reliable connection can be established between the two devices.

### Step 3: Sending a request to the server

If a reliable connection is established, we can send an HTTP (**H**yper**t**ext **T**ransfer **P**rotocol) request to the server. This is where we tell the server what we actually want from it.

When accessing a website, this is generally going to be a `GET` request, where we ask for some content from the site. This can be anything from plain text documents to images and videos.

The request also includes lots of useful meta-information, such as language preferences.

In addition to the request, your browser will also send any relevant HTTP cookies to the site at this stage. These cookies are small pieces of data stored by your browser, and are frequently used to preserve information between page visits. Common use cases are things like keeping track of items in a user's shopping cart, or keeping users logged across several page loads.

::: tip Request types
A `GET` request isn't the only type of request we can make, and we'll be covering some other request types throughout the course, such as `POST` requests.
:::

### Step 4: Sending a response

After our browser sends the request for us, it's up to the site's server to handle the request and give us what we asked for in the form of an HTTP response. The HTTP response contains lots of information such as the time the response was sent, and information about the content being returned.

The server may not always be able to fulfill our request, and the response contains a line to let us know the status of the request. This line includes the HTTP version being used, a status code for the response, and some explanatory phrase for the status code.

These status codes are how the server communicates whether anything went wrong with the initial request, or if anything else noteworthy happened. You're probably familiar with the `404` status code, which indicates that a resource could not be found. It usually means that we're trying to access a page which doesn't exist.

Another important status code is `200`, which means that the request was successful, and that there were no issues.

### Step 5: Loading the page

Assuming the server was able to fulfill the request to view the desired page, the browser is going to be served a document &mdash; generally written in HTML5 &mdash; as part of the response.

This document describes the structure and meaning of the page's content, and will contain links to other resources which also get fetched by the browser. This includes stylesheets, which describe the appearance of the page's content, as well as images, video files, fonts, and potentially JavaScript files.

The browser has to send additional requests to the server for all of these resources, just like it did for the HTML document itself.

While these additional resources download, the browser begins constructing a model of the site's structure, and starts painting content to the browser window. Once this painting is complete, and all of the site resources have finished downloading, we're left with a complete web page.

## This course

In this course we're going to be predominantly focusing on steps 3 and 4. We're going to be writing client side code to interact with servers through a web browser, and we're going to be writing server side code to handle those requests.

Throughout the next couple of sections we're going to be taking a closer look at the technologies involved in actually displaying a web page to the user, and then we're going to look into writing server-side code to handle user requests with Python and Flask.

<BottomCallout></BottomCallout>

[^ipv6]: [IPv6](https://www.networkworld.com/article/3254575/what-is-ipv6-and-why-aren-t-we-there-yet.html)
[^server]: [What is a server?](https://www.techopedia.com/definition/2282/server)
