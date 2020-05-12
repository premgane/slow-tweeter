from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PostingForm(FlaskForm):
    tweet = StringField('tweet', validators=[DataRequired()])
    submit = SubmitField('Submit')
