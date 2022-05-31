from .extensions import db


class Mehedi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


      git config --global user.email "aminulislam0527@gmail.com"
       git config --global user.name "ai-mehedi"