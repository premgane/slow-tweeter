from app import app
from flask import render_template, flash, redirect
from app.forms import PostingForm

@app.route('/')
@app.route('/index')
def index():
    form = PostingForm()
    return render_template('posting.html', title='Make a post', form=form)