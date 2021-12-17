from .extensions import db
from string import ascii_letters, digits
from random import choices
class Url(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    original_url = db.Column(db.String(100))
    short_url = db.Column(db.String(10), unique=True)
    count = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()
    def generate_short_url(self):
        characters = digits + ascii_letters
        short_url = ''. join(choices(characters, k=7))
        url = self.query.filter_by(short_url=short_url).first()
        if url:
            return self.generate_short_url()
        return short_url
