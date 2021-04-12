from . import db


class User(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    street = db.Column(db.String(128))
    city = db.Column(db.String(64))
    zipcode = db.Column(db.Integer())


