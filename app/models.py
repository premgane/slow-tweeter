from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(160), unique=True)

    def __repr__(self):
        return '<Tweet {}>'.format(self.tweet)