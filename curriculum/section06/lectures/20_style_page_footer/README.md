---
title: "How to style the page footer"
slug: how-to-style-the-page-footer
tags:
  - How to
  - Published
categories:
  - Video
section_number: 6
excerpt: An excerpt of the lecture's content goes here.
draft: false
---

# How to style the page footer

## Starting code

```css
html {
    font-family: Lato;
}

.navbar {
    max-width: 640px;
    margin: 50px auto;
    padding: 0 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    font-size: 24px;
}

.navbar__brand {
    display: flex;
    align-items: center;
}

.navbar__logo {
    margin-right: 30px;
}

.navbar__navigation {
    display: flex;
    flex-direction: row;
    align-items: center;
    list-style: none;
    color: #5C6B70;
}

.navbar__navigation-item {
    margin-left: 50px;
}

.navbar__link {
    text-decoration: none;
    color: inherit;
}

.main {
    max-width: 450px;
    margin: 0 auto;
    padding: 0 20px;
}

.form {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.form__input {
    width: 100%;
}

.form__label {
    display: block;
    margin-bottom: 10px;
}

.form__textarea {
    width: inherit;
    font-size: 18px;
    padding: 12px 20px;
    box-sizing: border-box;
    border: none;
    background-color: #F3F6F6;
    margin-bottom: 10px;
}

.form__submit {
    background-color: #3CD0FF;
    border: none;
    font-size: 18px;
    font-weight: bold;
    padding: 5px 30px;
    border-radius: 20px;
    color: white;
		cursor: pointer;
}

.form__submit:hover {
    background-color: #18B1E1;
}

.entry {
    margin-top: 50px;
}

.entry__title {
    display: inline;
    font-size: 16px;
}

.entry__date {
    color: #5C6B70;
}

.entry__content {
    font-size: 14px;
    line-height: 150%;
}
```

## Code written in this lecture

```css
.footer {
    background-color: #323F43;
    padding: 40px 0;
    margin: 50px 0 0 0;
    border-top: 4px solid black;
    color: white;
    font-size: 12px;
}

.footer__content {
    max-width: 640px;
    margin: 0 auto;
		padding: 0 20px;
    display: flex;
    flex-direction: row;
}

.footer .left {
    flex-grow: 2;
    display: flex;
    flex-direction: column;
}

.footer .right {
    flex-grow: 1;
    display: flex;
    flex-direction: row;
}

.footer__column {
    display: flex;
    flex-direction: column;
    margin-left: 50px;
}

.footer__item {
    margin-bottom: 5px;
}
```

## Final code

```css
html {
    font-family: Lato;
}

.navbar {
    max-width: 640px;
    margin: 50px auto;
    padding: 0 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    font-size: 24px;
}

.navbar__brand {
    display: flex;
    align-items: center;
}

.navbar__logo {
    margin-right: 30px;
}

.navbar__navigation {
    display: flex;
    flex-direction: row;
    align-items: center;
    list-style: none;
    color: #5C6B70;
}

.navbar__navigation-item {
    margin-left: 50px;
}

.navbar__link {
    text-decoration: none;
    color: inherit;
}

.main {
    max-width: 450px;
    margin: 0 auto;
    padding: 0 20px;
}

.form {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.form__input {
    width: 100%;
}

.form__label {
    display: block;
    margin-bottom: 10px;
}

.form__textarea {
    width: inherit;
    font-size: 18px;
    padding: 12px 20px;
    box-sizing: border-box;
    border: none;
    background-color: #F3F6F6;
    margin-bottom: 10px;
}

.form__submit {
    background-color: #3CD0FF;
    border: none;
    font-size: 18px;
    font-weight: bold;
    padding: 5px 30px;
    border-radius: 20px;
    color: white;
		cursor: pointer;
}

.form__submit:hover {
    background-color: #18B1E1;
}

.entry {
    margin-top: 50px;
}

.entry__title {
    display: inline;
    font-size: 16px;
}

.entry__date {
    color: #5C6B70;
}

.entry__content {
    font-size: 14px;
    line-height: 150%;
}

.footer {
    background-color: #323F43;
    padding: 40px 0;
    margin: 50px 0 0 0;
    border-top: 4px solid black;
    color: white;
    font-size: 12px;
}

.footer__content {
    max-width: 640px;
    margin: 0 auto;
		padding: 0 20px;
    display: flex;
    flex-direction: row;
}

.footer .left {
    flex-grow: 2;
    display: flex;
    flex-direction: column;
}

.footer .right {
    flex-grow: 1;
    display: flex;
    flex-direction: row;
}

.footer__column {
    display: flex;
    flex-direction: column;
    margin-left: 50px;
}

.footer__item {
    margin-bottom: 5px;
}
```