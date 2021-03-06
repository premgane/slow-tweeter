from app import app, db, models
from flask import render_template, flash, redirect, url_for
from app.forms import PostingForm
import time
import tweepy

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostingForm()
    if form.validate_on_submit():
        flash('Tweeting this out: {}'.format(
            form.tweet.data))
        # In the year 2038, we will need to make sure not to use 32-bit ints
        tweet = models.Tweets(id=time.time(), tweet=form.tweet.data)
        db.session.add(tweet)
        db.session.commit()

        auth = tweepy.OAuthHandler(app.config.TWITTER_CONSUMER_KEY, app.config.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(app.config.TWITTER_ACCESS_TOKEN, app.config.TWITTER_ACCESS_SECRET)

        api = tweepy.API(auth)

        api.update_status(form.tweet.data)

        return redirect(url_for('index'))
    return render_template('posting.html', title='Make a post', form=form)