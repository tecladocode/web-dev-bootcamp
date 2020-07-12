# Jinja2: Expressions & Data Structures

By now you already know how to use Jinja2 and Flask's `render_template` method to interpolate placeholder values in HTML files and send them to the browser. Jinja2 also lets you evaluate Python expressions and data structures while filling in the placeholders with values that are more complex than simple variables.

In this lesson, you'll see how you can evaluate different Python expressions, incorporate a few data structures in Jinja2 and render them using the `render_template` method.

## What is an Expression?

In Python, an expression[^expression] represents something; like a number, a string, or an instance of a class. To be an expression, a Python instruction has to evaluate down to a single value.

> An expression is an instruction that combines values and operators and always evaluates down to a single value.

For example, `>>> foo = 2 + 2` is an expression that evaluates to a single value `4`. In contrast, a Python instruction that doesn't evaluate down to a single value is generally known as a statement, i.e. an `if-else` statement.

## Expressions in Jinja2

### Basic Operations

* Float/integer addition, subtraction
* String concatenation

### Function Evaluation

## Data Structures in Jinja2

### Built in Data Structures

* Lists
* Dicts
* Sets

### Custom Data Structures

* Custom classes

## Conclusion


[^expressions]: [What is an expression in Python?](https://stackoverflow.com/a/30114220/8963300)
