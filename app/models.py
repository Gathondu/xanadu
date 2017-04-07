from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), index=True)
    last_name = db.Column(db.String(30), index=True)
    nickname = db.Column(db.String(60), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.nickname)
