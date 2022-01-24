---
title: "How to start a new software project"
slug: how-to-start-a-new-software-project
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# How to start a new software project

Planning, running, and keeping a software project alive _really_ doesn't have to be hard. Follow just a couple of systems to stay on top of everything.

In this chapter we'll talk about how software projects are usually managed in software companies, as well as what you can take from their processes personally to better manage your software projects.

::: tip Why spend time managing a software project?
Software projects can become messy over time, as you add features, come up with new ideas, change old parts of the code...

In just a few minutes a day you can completely remove all the accidental complexity that comes from this chaos, and instead focus on what brings the most value to your users.

Plus if you work or want to work at a software company, knowing how projects are managed will be extremely helpful!
:::

We've recorded a video that talks about this topic as well:

<iframe width="560" height="315" src="https://www.youtube.com/embed/UvVuXt2Ak8M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## The traditional process: Waterfall

The traditional software development process is called waterfall, because, like in a waterfall, the steps are followed one after another and there's generally no turning back (it's expensive to, as you'll see).

These are the five stages in a waterfall process:

1. **Analysis**: where users are consulted so developers can find out what they want, and build a set of requirements. These requirements are what developers implement later on in the process.
2. **Planning**: each requirement is planned fully from design to the technical implementation. Often, you'll see documents explaining how certain features will be coded.
3. **Implementation**: everything is coded.
4. **Testing**: the finished app is tested (often by a separate team from the development team).
5. **Evaluation** or **Maintenance**: users use the product and bugs are fixed (forever).

Each step is long, and often the outcome of each stage is a lot of documentation or code.

There are pros and cons to a waterfall process.

### The cons of Waterfall

- From stage to stage, everything has to be extremely well defined and documented. This requires a lot of work in each stage.
- If you move from one stage to another and you find out you're missing things (e.g. missing requirements or missing planning), then fixing those things requires a lot of work.
  - This is especially true if you find, for example, missing requirements when you're in the Evaluation phase. Those missing requirements might affect how other features are implemented, so you have to go through Planning, Implementation, and Testing again for a large part of your app.
- Since every phase takes a lot of time and effort, nobody involved in the project wants to find out that their work was wasted. This, however, does happen often in software projects. For example, the customer might think they want a certain feature, but when they get to the Evaluation phase they realise that actually, that feature isn't so useful or necessary anymore. Happens all the time!
- Different phases are often carried out by different teams. For example, a Testing team might carry out extensive testing of the application in the Testing phase, but a Development team did the implementation. Working like this often leads to "throwing over the fence", or a handover of the project between teams such that the previous team washes their hands off the project before moving onto something else.
  - It happens that, for example, if the Testing team finds bugs, the Development team might feel _angry_ or _slighted_ by this. This is often due to a feeling of being "done" with the project, and now it's someone else's responsibility.

I'm sure there are more cons, but we'll leave it there for now!

### The pros of Waterfall

The main "pro" of waterfall processes also happens to be a "con":

- Every stage needs to be done, finished, and verified, before moving onto the next one. Lots of documentation is often produced at each stage that formalizes everything that happens next.

But this point is precisely why waterfall processes are often used.

If you have a lot of documentation and a very formal set of requirements, this means that those requirements and those plans can be validated thoroughly.

Therefore, waterfall processes are often used in critical systems and applications where you need a high degree of exactitude and verification. For example, medical software, software that runs in airplanes, or security systems.

For most software projects though, waterfall is not the right process to follow. That is because **software is easy to change**, and because of that, we often do change it!

## Agile, and what that means

I'll preface this section by saying that there is a lot of misinformation, many misconceptions, some cargo cult, and a lot of stress placed on Agile. What I'm about to talk about probably has nothing to do with anything you have read about or heard of before.

At its core, being agile is about having a plan but being able to change it, and about continuously trying to improve the way you work (for example, by improving the tools you use, the technologies you depend on, or the people you work with).

### A scenario: adding features after the project is finished

Let's say you're building an application, such as a movie database.

When you start the project, you think you're going to build a simple application that stores upcoming movie releases and lets users search for upcoming movies.

You plan the whole thing, then you design the entire application, and then you code it. Throughout this process, you write documentation explaining every design and implementation decision.

Then you get to testing, and you painstakingly test manually the application. Every corner case, every potential issue a user might encounter.

Then you get to the evaluation phase, and you (or your users) decide that, instead of storing upcoming movie releases, it would be better if the application allowed users to store what movies they have watched so that they and their friends can comment on them.

This might seem outrageous, but it happens _so often_.

Even at Teclado, internally, we develop tools to help us with video production and editing. We change our mind on features and use cases for those applications all the time.

### Having a plan but being able to change it

Having a plan is good, but only involving your users at the beginning of that (the Requirements phase) is not good. Agile suggests that you should involve users throughout the entire software project.

In order to involve users throughout the entire project, two things need to happen:

1. You need to have an open channel of communication with users throughout the entire project development
2. Your users need to be able to use your software while you develop it (otherwise, what do they comment on?)

It is for these two reasons that Agile recommends that you build software in a way that you can always run it (this is called "Working software"). To do this, the application development starts with the smallest feature that users would want to use, and it is developed so that users can benefit from it as soon as possible.

Then, when that's working, you work on the next feature (or maybe fix a bug that you noticed when the user tried your first feature).

This back and forth with the customer and working software is known as "Customer collaboration". It's vital for any successful software project.

The final thing this allows is for the customer, early on in the process, to notice that, you know, this new feature isn't exactly what they needed after all. Maybe they now want to take the project in a different direction!

This ability to change is known as "Responding to change".

Do note that this means that the timeline for an Agile software project can be uncertain. There is always a tradeoff between changing requirements and cost (since paying developers takes money!). However, I've personally found that Agile projects produce better software that customers want, and generally in less time than waterfall projects.

### Continuously improving the way you work

The final cornerstone of Agile is that "Individuals and interactions" are valued more than processes and tools. Agile recommends that any software team collaborates heavily and also spends time trying to improve their ways of working.

When you're working in a high-performing software development team, you'll immediately notice that people mesh together well. Everyone involved in the development collaborates heavily, and ideas cross-pollinate between members--even if they are in different disciplines.

And that is another thing: no more "throwing over the fence". The Agile team should be composed of motivated individuals with the appropriate environment, support, and trust from the business to do their best work. Generally you'll see Agile teams include designers, test engineers, software engineers, customer representatives, database administrators, and really anyone else that can help develop the project.

## A formalization of Agile

The idea of Agile (with an uppercase "A") was originally conceived in 2001 by a group of software developers who didn't know everything but tried to come up with some principles that can guide a software team in making better software and getting better at making better software, every day.

They produced a (slightly sectarian-looking) _manifesto_ with their recommendations: [https://agilemanifesto.org/](https://agilemanifesto.org/).

I happen to agree with what they decided back then:

- Individuals and interactions are more valuable than processes and tools.
- Working software is more valuable than comprehensive documentation.
- Customer collaboration is more valuable than contract negotiation.
- Responding to change is more valuable than following a plan.

As you progress in your software career, you may find that some people follow very specific practices (like a meeting every day to tell your manager what you've done). If those practices help produce better working software, better customer collaboration, better interactions between team members, or allow you to respond to change more easily, then they're probably good practices.

If not though, you shouldn't be afraid to suggest changing them.

There's much more to learn about agile working, and especially to absorb about what feels right and what doesn't. Only experience will give you that!

## Conclusion

In the next few chapters we'll talk about how you might develop this Microblog project following an Agile way of working so you gain first-hand experience!
