from flask import (
    Blueprint,
    redirect,
    render_template,
    session,
    request,
)
from movie_library.forms import MovieForm


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )


@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if request.method == "POST":
        pass

    return render_template(
        "new_movie.html", title="Movies Watchlist - Add Movie", form=form
    )


@pages.get("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"

    return redirect(request.args.get("current_page"))
