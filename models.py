from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(100))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
