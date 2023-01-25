---
title: What do deployment services do for us?
slug: what-do-deployment-services-do
tags:
  - Concept
  - Published
categories:
  - Presentation
section\_number: 8
excerpt: "Learn about what deployment services like Render.com do for us."
draft: false
---

# What do deployment services do for us?

When we run our app, people and programs can make requests to the address the app is running on. When we run our app with `flask run`, this starts a development server which is in charge of receiving those requests and sending them over to the Flask app. The app then runs the Python function and calculates the response.

For security reasons, when we run our app locally, people outside our network can't make requests to it. So if we want our app to be publicly available, we must deploy it somewhere that doesn't have this restriction.

Deployment services companies like Render.com or Heroku, run our applications in publicly accessible services and they give us a URL that we can use to make requests to the application.

These companies make it really easy to deploy our apps by taking care of provisioning hardware, setting it up, installing dependencies, etc. This kind of business is known as a PaaS: "Platform as a service."

If you don't mind doing some more work yourself, for example by setting up each individual server, then you can save money by renting servers directly. The benefit of this is you can run multiple applications in a single server and you get more flexibility. This can save money, but takes a lot more work. Plus, PaaS applications can do things like restart our services if they crash, they can handle backups and deployments, and much more. Overall, I think using a PaaS makes a lot of sense, especially for smaller applications.

Render.com has a generous free plan which means we can use their services for free. There are some limitations however. We only get 1500 hours per month, and builds are a bit slower than on paid plans (so when you deploy, it takes a few minutes for your application to run).

Let's get started in the next lecture!