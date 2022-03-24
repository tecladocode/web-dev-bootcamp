from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

from wtforms.validators import DataRequired, NumberRange


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
