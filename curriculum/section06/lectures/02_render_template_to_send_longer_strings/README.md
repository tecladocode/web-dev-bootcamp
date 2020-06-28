# Using render_template to Send Longer HTML Strings

In the previous lesson, you've learned about APIs, endpoints and how you can make quick APIs with Flask. Also, you've seen how Flask lets you display HTML decorated texts in your browser.

Writing HTML string directory into your application code is okay as long as the size of the string is minimal. However, if you want display multiple HTML pages or large HTML stings, embedding that directly into your application code may not be the best idea.

In this lesson, we'll see how you can write separate HTML files and use Flask's `render_template()` method to display your static contents.

## Static Content

Static content is any content that can be delivered to an end user without having to be generated, modified, or processed. The server delivers the same file to each user, making static content one of the simplest and most efficient content types to transmit over the Internet. In our case, the HTML files that we want to display in the browser are static contents.

## Rendering

The process of displaying static contents are also known as *rendering*. In this lesson, we'll be strictly rendering static HTML contents. In the next lesson, you'll see how you can render dynamic contents through dynamic templating language[^templating-language] and render_template[^render-template].

## Render HTML String

From the previous lesson, you probably recall that you can render HTML string in the following manner:

```python
# app.py
from flask import Flask


app = Flask(__name__)


@app.route("/fancy")
def hello_world_fancy():
    greetings = """
    <html>
    <body>

    <h1>Greetings!</h1>
    <p>Hello, world!</p>

    </body>
    </html>
    """
    return greetings
```

Running the code gives you this nicely formatted greeting in your browser:


![Hello world with html](https://user-images.githubusercontent.com/30027932/85437519-847cdf80-b5ac-11ea-8e3c-9bcfd558f447.png)

While this is good for simple cases, in the next section you'll see how you can manage and server larger HTML content with Flask.

## Render HTML Page

### Create the Static Files

Let's create a folder named `template` inside your project folder. Create two empty HTML files called `first_page.html` and `second_page.html` in the `template` folder. Your project folder should have the following structure:

```
.
├── app.py
└── templates
    ├── first_page.html
    └── second_page.html
```

Now, go ahead and add the following contents to your static files.

**First page:**

```html
<!-- first_page.html -->

<!DOCTYPE html>
<html>

<body>

    <h1>First Page</h1>
    <p>This is the first page of your static content</p>

</body>

</html>
```

**Second Page:**

```html
<!-- second_page.html -->

<!DOCTYPE html>
<html>

<body>

    <h1>Second Page</h1>
    <p>This is the second page of your static content</p>

</body>

</html>
```

The above static are kept simple for demonstration purpose. In real life, you'll be dealing with much larger and more complex static files.

### Render the Files via render_template

Now you've created the necessary static files, let's see how you can render them in your browser. If you've gone through the previous lesson, the following code snippet should be familiar. Here, we'll be exposing two API endpoints for rendering two HTML static files:

``` python{4,11,16}
# app.py

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/first-page")
def render_first_page():
    return render_template("first_page.html")


@app.route("/second-page")
def render_second_page():
    return render_template("second_page.html")
```

In the above code snippet, we've imported the `render_template` method from Flask and used that to render our static contents. Here, using the `route` decorator, we've created two different endpoints to display the pages. Notice, we didn't mention the full path of the HTML files inside the `render_template()` method; Flask automatically looks for static files in the `template` folder.

Now run the application (refer to the previous lesson[^run-flask] if you don't know how to run Flask applications.) and go to following URL to view the `first_page.html`:

```
http://localhost:5000/first-page
```

To access `second_page.html`, go to:

```
http://localhost:5000/first-page
```

## Conclusion

In this lesson, you've learned the what static contents are, what rendering static files means and how to render static HTML files using Flask's `render_template` method.

[^templating-language]: [Templating Language](https://collectiveidea.com/blog/archives/2018/03/06/what-s-in-a-templating-language-part-1)
[^render-template]: [Flask's render_template](https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates)
[^run-flask]: [Running Flask Applications](https://github.com/tecladocode/python-web-2020/tree/master/curriculum/section06/lectures/01_hello_world_flask#run-the-application)
