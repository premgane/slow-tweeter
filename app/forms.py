from wtforms import StringField, SubmitField


class PostingForm(FlaskForm):
    tweet = StringField('tweet', validators=[DataRequired()])
    submit = SubmitField('Submit')