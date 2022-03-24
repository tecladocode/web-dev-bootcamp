from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
)

from wtforms.validators import (
    DataRequired,
    NumberRange,
)


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    director = StringField("Director", validators=[DataRequired()])

    year = IntegerField(
        "Year",
        validators=[
            DataRequired(),
            NumberRange(min=1878, message="Please enter a year in the format YYYY."),
        ],
    )

    submit = SubmitField("Add Movie")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("Cast")
    series = StringListField("Series")
    tags = StringListField("Tags")
    description = TextAreaField("Description")
    video_link = URLField("Video link")

    submit = SubmitField("Submit")
