from datetime import datetime
from ecommerce import db

db.Model.metadata.reflect(db.engine)


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    userid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    address1 = db.Column(db.String(20), unique=False, nullable=False)
    address2 = db.Column(db.String(20), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    zipcode = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}'), '{self.password}', " \
               f"'{self.address1}', '{self.address2}', '{self.city}', '{self.state}', '{self.country}'," \
               f"'{self.zipcode}','{self.email}','{self.phone}')"
