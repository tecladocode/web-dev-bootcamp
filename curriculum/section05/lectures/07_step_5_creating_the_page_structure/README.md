# Step 5: Creating the Page Structure

When coming up with a rough HTML structure for a page, the main thing to think about is the meaning of the elements we're using, and how we're nesting them.

## Layout

To understand what we mean by "layout", let me show you a fictitious website:

IMAGE

Here you can see that we've got, in the middle of the page, something that looks like a grid.

That one's pretty clear-cut, but what about the header and footer?

Some people might want to consider the whole page as a grid with 3 columns. With this model, the header and footer span 3 columns (making them full width). The elements in the middle each span one column.

Other people might think of the page as having three elements: header, a grid of content items, and footer.

Coming up with the correct layout depends on what each element means. When two elements are contained by the same parent (i.e. the elements are _siblings_), they should have similar meaning. It's uncommon to have disjointed sibling elements.

For this reason, one of these layouts is correct, and the other is not. Let's take a look!

### The 3-column grid

If we think of the whole page as a single grid, we can place all of the site's content into a grid of 3 columns and 4 rows.

Then we could make the header and footer elements span the 3 columns so that they are full-width.

IMAGE

This way we have less nesting: all the main elements are direct children of the grid, like so:

```html
<body class="grid-3-col">
  <header class="span-3-col"></header>
  <article class="content-item"></article>
  <article class="content-item"></article>
  <article class="content-item"></article>
  <article class="content-item"></article>
  <article class="content-item"></article>
  <article class="content-item"></article>
  <footer class="span-3-col"></footer>
</body>
```

However, by doing this we lose meaning. The header, footer, and content items are all siblings. This suggests they should have similar meaning, but in reality they do not.

### The single column

Instead, we should make sure sibling elements are related.

By using a single column approach, we can have a separate header, footer, and grid. These three elements related in that they are entire sections of a page on their own.

Then, the grid element contains the articles, or content items, all of which are related as well.

IMAGE

Although here we have more elements and more nesting, I believe it's clearer to work with:

```html
<body>
  <header></header>
  <main class="grid-3-col">
    <article class="content-item"></article>
    <article class="content-item"></article>
    <article class="content-item"></article>
    <article class="content-item"></article>
    <article class="content-item"></article>
    <article class="content-item"></article>
  </main>
  <footer></footer>
</body>
```

These decisions of which layout to go for and how to structure the site are one of the main things you need to learn about how to code effectively with HTML. We'll help with that, but also experience will tell you whether you prefer one over the other!

## The Microblog page structure

For our Microblog project, we need to look at the layout and structure of the page before we jump into coding as well.

Fortunately, the Microblog is simpler. We don't have to make decisions regarding grids, as everything can be divided into rows and columns:

IMAGE SHOWING MICROBLOG COLUMNS

We have:

- One column that contains all elements. Inside it:
  - A header
  - A central content area with a form and previous entries
  - A footer

The entire page is laid out as a column, and the central content area is a column too, with the form at the top and entries stacked one on top of another. Since these are closely related (the form creates new entries), they're OK to be siblings.

However, to differentiate them as two distinct sections of the main content, the form and the articles will each be enclosed in a `section` tag.

So this is more or less what I'm envisioning the structure of the page will look like:

IMAGE

## Conclusion

Now that we've learned how to begin identifying the layout and nesting of elements in an HTML page, let's get to actually coding this page in our code editor!