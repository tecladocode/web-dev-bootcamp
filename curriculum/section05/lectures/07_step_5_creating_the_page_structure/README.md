# Step 5: Creating the Page Structure

When coming up with a rough HTML structure for a page, there are two main things I think of:

- Layout: grid vs. columns vs. rows
- Nesting of elements
  - Which ones are block (full width) vs. inline

## Layouts

To understand what we mean by "layouts", let me show you a fictitious website:


Here you can see that we've got, in the middle of the page, something that looks like a grid.

That one's pretty clear-cut, but what about the header and footer?

Well, there's really two main ways to think about the site as a whole:

- A 3-column grid, where the header and footer span 3 columns;
- A single column with 3 elements, where the middle element is a 3-column grid.

### The 3-column grid

We can place all of the site's content into a grid of 3 columns and 4 rows.

Then we could make the header and footer elements span the 3 columns so that they are full-width.

IMAGE

This way we have less nesting: all the main elements are direct children of the grid, like so:

```html
<main class="grid-3-col">
  <header class="span-3-col"></header>
  <div class="content-item"></div>
  <div class="content-item"></div>
  <div class="content-item"></div>
  <div class="content-item"></div>
  <div class="content-item"></div>
  <div class="content-item"></div>
  <footer class="span-3-col"></footer>
</main>
```

However, by doing this we lose a bit of meaning, and we need to manually specify which elements should span 3 columns.

### The single column

Instead, I prefer the single column approach, where elements occupy the full width of the page by default, and we can then have a grid sub-element to take care of the grid layout:

IMAGE

Although here we have more elements and more nesting, I believe it's clearer to work with because the layouts are only defined at the point at which they are used:

```html
<main>
  <header></header>
  <div class="grid-3-col">
    <div class="content-item"></div>
    <div class="content-item"></div>
    <div class="content-item"></div>
    <div class="content-item"></div>
    <div class="content-item"></div>
    <div class="content-item"></div>
  </div>
  <footer></footer>
</main>
```

These decisions of which layout to go for and how to structure the site are one of the main things you need to learn about how to code effectively with HTML. We'll help with that, but also experience will tell you whether you prefer one over the other!

## Nesting of elements

The nesting of HTML elements is mostly decided by the meaning of the structure you're coding. That is why we say that HTML is a _semantic_ language: the things you code are shown to users, and depending on how you structure your site, it can suggest one meaning or another.

For example, using HTML and CSS you could make these two _look identical_:

```html

```

and

```html

```

But just by looking at the HTML, clearly they don't mean the same.

For many users, the meaning of HTML code can often go unnoticed. It is when we start using screen readers and other assistive technology that well-constructed HTML can provide an excellent experience for users, and badly crafted HTML can cause extreme confusion.

Throughout the course we'll explain why we choose the type of elements we choose, and how we use them in conjunction with other elements. That way, you'll gain first-hand experience on writing good semantic HTML.
