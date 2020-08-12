# Non-inherited Properties

As we discussed in the last lecture, not all properties are inherited by default. In this lecture I want to go over some of the more common non-inherited properties.

## Layout properties

A broad categoty of non-inherited properies can be thought of as "layout properties": properties which change the size of the element in some way, or how it interacts with the elements around it.

These properties include things like `margin`, `padding`, `height`, `width`, `box-sizing`, `position`, and `display`.

The reason these properties don't inherit by default is simply that it doesn't make a lot of sense. For example, if we want to put some space underneath an element, it doesn't really make much sense to add this much space to every single child element as well.

Similarly, if we set the `height` of element explicitly, we'll  clearly run into a lot of trouble if every child element also became this size.

`display` is another case where we could run into major problems. `<p>` elements have a display style of `block`, which means they fill the width of their container. We often put things like `<span>` and `<a>` elements inside `<p>` elements, and usually we want them to fit into the normal flow of the text content. We generally don't want these elements forced onto their own lines.

If these properties were inherited, we'd inevitably end up writing far more code just to correct the issues being caused by inheritance!
