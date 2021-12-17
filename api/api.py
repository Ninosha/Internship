import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
from random import choices
from string import ascii_letters, digits

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


api = Api(app)


class Urls(db.Model):
    __tablename__ = "Urls"

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(250))
    short_url = db.Column(db.Integer)

    def __init__(self, original_url):
        self.original_url = original_url
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = digits + ascii_letters
        short_url = ''. join(choices(characters, k=7))
        url = self.query.filter_by(short_url=short_url).first()
        if url:
            return self.generate_short_url()
        return short_url

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id': self.id, 'original_url': self.original_url, 'short_url': self.short_url}


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('original_url',
                        type=str,
                        required = True,
                        help = "Please input url"
    )


    def get(self):
        url = Urls.query.filter_by.first()
        if url:
            return url.json()


api.add_resource(Urls, '/urls/<string:url>')


app.run(port=5000, debug=True)
