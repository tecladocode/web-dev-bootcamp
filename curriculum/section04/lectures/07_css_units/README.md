# Basic CSS Units

So far we've mostly been using pixels to specify sizes, but in practice, pixels are not a great option for most use cases.

We actually have a wealth of different unit types in CSS, from pixels and percentages, to centimetres and inches. The latter generally being used for styling print documents.

In this lecture we'll cover a few of the most important unit types for CSS.

## Pixels (`px`)

In terms of hardware, a pixel is a single light-emitting unit capable of displaying full colour independent of its neighbours. You screen is made up of millions of such units, and we can see them with the naked eye if we look closely enough.

A pixel in CSS doesn't quite correspond to these device pixels which make up your screen. Instead, there's a degree of scaling involved to ensure that devices with a high pixel density display objects at an appropriate size.

Take an iPhone 11 Pro, for example. An iPhone 11 Pro has a whopping device resoluton of `2436 x 1125`, but in CSS pixels, the device is only `812 x 375`: a third of the device values.

This isn't something we usually have to worry about, but we should keep this concept in mind for when we start talking about responsive design.

## `em` and `rem`

`em` and `rem` are units you've likely never encountered before, but you're going to be getting very familiar with them when working with CSS. They're the most common unit types I personally use.

The term "em" comes from typography, and historically it was the width of an uppercase "M" character. However, this was really more of an accident, as "M" character was traditionally the same width as the the point size of the font. This is generally no longer the case.

In modern typography, an em is defined as being the same as the point size of the font, and the same is true in CSS. This also translates to pixels, so if we have a font size of `16px`, then `1em` is `16px`.

When working with `em` units, the font size of the element where the unit is being used. For example, if we have an element with a font size of `10px`, then `1em` is considered to be `10px` when used to size components of that element.

`rem` stands for *root* `em`, and is generally a far more useful unit. `rem` uses the global font size to determine its size, which means that `rem` units are consistent across our entire site.

`rem` is forms the cornerstone of modern responsive design, as we'll see shortly.

## 