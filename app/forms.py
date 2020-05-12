from wtforms import StringField, SubmitField


class PostingForm(FlaskForm):
    username = StringField('Tweet', validators=[DataRequired()])
    submit = SubmitField('Sign In')