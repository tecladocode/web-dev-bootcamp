# Jinja2: Conditional Statements

**Conditional statements**[^conditional-statements] perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to *true* or *false*. Simply speaking, the `if-else` construct in your code is generally referred to as conditional statements.

> Instead of dealing with `if...else` conditionals in the Flask code, you can directly embed them into the Jinja2 templates. With the default syntax, control structures appear inside `{% ... %}` blocks.

## Basic Comparisons

Define a template named `conditionals_basics.html` in your Flask project's `/templates` folder. In this example, we'll render different lists of products depending on the name of different companies provided by a user-defined variable called `company`. Here, we'll directly embed the conditional statements into the template.

```html{6,12,19,22}
<!-- templates/conditionals_basics.html -->

<h2>Conditionals in Jinja2</h2>
<h3>Basic Comparisons</h3>

{% if company == "Apple" %}
<h4>Available {{ company }} Products</h4>
    <ul>iPhone</ul>
    <ul>iPad</ul>
    <ul>iMac</ul>

{% elif company == "Microsoft" %}
<h4>Available {{ company }} Products</h4>
    <ul>Windows Phone</ul>
    <ul>Surface Pro</ul>
    <ul>Surface Book</ul>

{% else %}
    No {{ company }} product available.

{% endif %}
```

Notice how conditional blocks were introduced to the template via `{% %}` blocks in line 6, 12, 18. The `{% endif %}` block in line 21 marks the end of the conditional block. Now let's create an endpoint named `/conditionals-basics/` in your Flask project's `app.py` file to render the template:

```python{10,11}
# app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/conditionals-basics/")
def render_conditionals_basics():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)
```

In line 10, we've provided the name of the company and passed that to the `render_template` method in the next line. Run the Flask application and go to [http://localhost:5000/conditionals-basics](http://localhost:5000/conditionals-basics) on your browser. You should be able to see the following list:

![conditionals_basics_1](./assets/conditionals_basics_1.png)

Now change the variable `company` in the `app.py` from `Apple` to `Microsoft` and see what happens. Your `app.py` should look like this:

```python{10}
# app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/conditionals-basics/")
def render_conditionals_basics():
    company = "Microsoft"
    return render_template("conditionals_basics.html", company=company)
```

This time going to the [link](http://localhost:5000/conditionals-basics) on your brwoser should show a different list of products.

![conditionals_basics_1](./assets/conditionals_basics_2.png)

If you assign a different name other than `Apple` and `Microsoft` to the variable `company`, you'll see a "No product available" page.

![conditionals_basics_1](./assets/conditionals_basics_3.png)

## Checking Truthy / Falsy Values

You can also use conditional statements to test if a variable is *Truthy*[^truthy-falsy] (or *Falsy*) and take action based on that. For a variable to be *Truthy*, it has to be defined, not empty and not false. Make a new template named `conditionals_truthy.html` and add the following contents to it:

```html{6,7}
<!-- templates/conditionals_truthy.html -->

<h2>Conditionals in Jinja2</h2>
<h3>Checking Truthy/ Falsy Variables</h3>

{% if user %}
{% if user.username %}
    <p>Hi, I'm {{ user.username }}.</p>
{% endif %}
{% endif %}
```

The above template first checks whether the variable `user` is *Truthy* and then it also checks whether attribute `user.username` is also a *Truthy* value. If both of the conditions are true, the template returns the name defined in the `user` class.

Let's define an endpoint named `/conditionals-truthy` in the `app.py` file:

```python{8,19}
# app.py

from flask import Flask, render_template

app = Flask(__name__)


class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User({self.username})"


@app.route("/conditionals-truthy/")
def render_conditionals_truthy():
    user = User("Adam")
    return render_template("conditionals_truthy.html", user=user)
```

In line 8, we've defined a class called `User`. The class takes a single argument `username`. An instance of the class has been created in line 18. Here, the value of the argument `username = "Adam"` is a Truthy.

Run the Flask application and head over to [http://localhost:5000/conditionals-truthy](http://localhost:5000/conditionals-truthy) in your browser. You should see the template gets rendered like this:


![conditionals_basics_1](./assets/conditionals_truthy.png)

Now if you instantiate the class `User` with a *Falsy* value - for example, an empty string `""` - the greeting statement of the template won't be rendered. Here, your `app.py` will look like this:

```python{8,19}
# app.py

from flask import Flask, render_template

app = Flask(__name__)


class User:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User({self.username})"


@app.route("/conditionals-truthy/")
def render_conditionals_truthy():
    user = User("")
    return render_template("conditionals_truthy.html", user=user)
```

This time if you go to the [link](http://localhost:5000/conditionals-truthy), you'll notice that the greeting statement hasn't been rendered.


![conditionals_basics_1](./assets/conditionals_falsy.png)

## Conclusion

In this post, you've learned how to perform basic comparisons in Jinja2 templates using conditional statements. You've also seen how you can leverage *Truthy* and *Falsy* values of variables to control your logic directly from the Jinja2 template.

[^conditional-statements]: [Conditional (computer programming)](https://en.wikipedia.org/wiki/Conditional_(computer_programming)#:~:text=In%20computer%20science%2C%20conditional%20statements,evaluates%20to%20true%20or%20false.)

[^truthy-falsy]: [What is Truthy and Falsy? How is it different from True and False?](https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false)
