from app import app
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)