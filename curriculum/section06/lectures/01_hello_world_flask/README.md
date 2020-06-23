# "Hello, world!" with Flask

## Why Flask?

Flask[^flask] is known as a lightweight WSGI[^wsgi] application framework. A framework *is a code library that makes a developer's life easier while building reliable, scalable, and maintainable web applications* by providing reusable code or extensions for common operations. Flask lets you quickly get started with building web applications in pure python. In the following sections, you'll be installing Flask on your local development machine and start making a simple `hello-world` application. Let's jump right in!

## Installing Flask

Assuming you've got Python 3 installed on your local development machine, let's create a virtual environment and install Flask in it. For this demonstration, we'll be using `Python 3.8`. Run the following commands on your terminal based on your operating system:

### Linux / MacOS:

* Create the virtual environment

    ```bash
    python3 -m venv venv
    ```

* Activate the virtual environment

    ```bash
    . venv/bin/activate
    ```

* Install Flask via pip

    ```bash
    pip install Flask
    ```

### Windows

* Create the virtual environment

    ```bash
    py -3 -m venv venv
    ```

* Activate the virtual environment

    ```bash
    venv\Scripts\activate
    ```

* Install Flask via pip

    ```bash
    pip install Flask
    ```

If you're having trouble with your installation, checkout this detailed installation guide [here][^flask-install].

## Making a "Hello, World!" Flask Application

If you go to the Flask website, you are welcomed with a very simple example application that has just five lines of code. We'll be building the same application here just to get a hang of how the entire process works.

### Prepare Your Application Directory

We'll create a folder called `app` and put all our application code inside that. Go to your development directory(where you want to place your code) and run the following command to create the `app` folder:

```bash
mkdir app
```

### Write Your First "Hello, World!" Application

Now go to the `app` folder that you've just created and create a new python file called `hello.py`. Add the following lines to the `hello.py` file.

```python
# hello.py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
```

Let's see what did the above code do:

* First we imported the Flask class.

* Then we've create an instance of the class and assigned that to `app` variable. This instance of the class will be our WSGI application.

* We then use the `route()` decorator to tell Flask what URL should trigger our function.

* The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.

### Run the Application

To run the application, you can either use the `flask` command or python’s `-m` switch with `Flask`. Before you can do that you need to tell your terminal the application to work with by exporting the `FLASK_APP` environment variable. Also, during development, you should turn on the debugging mode by setting the `FLASK_ENV` environment variable to `development`. Run the following commands if you're on **Linux/MacOS**:

```bash
export FLASK_APP=hello.py
export FLASK_ENV=development
flask run
```


Now, if you're on **Windows** then export `FLASK_APP` and `FLASK_ENV` variables on command prompt like this:

```
C:\path\to\app>set FLASK_APP=hello.py
C:\path\to\app>set FLASK_ENV=development
```

Then run:

```
python -m flask run
```

Now using your browser, head over to http://127.0.0.1:5000/, and you should see your `hello world` greeting.

![Screenshot from 2020-06-23 14-49-09](https://user-images.githubusercontent.com/30027932/85382453-cda74200-b560-11ea-810e-a357545531ee.png)


Here, you've created your first API. An Application Programming Interface (API) allows two systems to communicate with one another. By running the Flask application, you've created a server that serves your `hello world` code. Your browser is the client that accesses the server via an API endpoint. The final part of the link `http://127.0.0.1:5000/` that you've used to interact with the API is called an endpoint. In this case, hitting the URL instructs the server to execute your `hello_world()` function. The `route()` decorator basically takes care of the back and forth communication between the server and the client.

## Serving an HTML String

Let's make our `hello-world` app a bit more exciting. Here, you'll create a new endpoint and display the *hello world* greeting in a fancy `html` format. Head over to your `hello.py` file and modify it like the following:

```python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


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

Notice, how we've introduced another function called `hello_world_fancy()` and decorated it like the previously defined `hello_world()` function. This time the `route()` decorator defines a new endpoint named `/fancy`. Flask will automatically append this endpoint to your host URL `http://localhost:5000`. So, the final URL will be http://localhost:5000/fancy. If you've stopped your server, then run the application again by following the previously mentioned instructions. Then head over to http://localhost:5000/fancy on your browser and you'll be greeted by a fancier *hello world* page.

![Screenshot from 2020-06-23 16-30-52](https://user-images.githubusercontent.com/30027932/85393520-f7676580-b56e-11ea-93ed-fc6621116e04.png)

## Conclusion

In this lesson, you've learned how to build and serve simple APIs with Flask framework. You've also learned how endpoints work and how to access the server from a client. The later section teaches you about adding new routes to your app and displaying a simple html string on your browser.

* [^flask]: [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [^wsgi]: [Getting Started with WSGI](https://wsgi.readthedocs.io/en/latest/what.html)
* [^flask-install]: [Installing Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
