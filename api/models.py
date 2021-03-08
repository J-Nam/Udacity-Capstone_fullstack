import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

database_path = os.environ.get('DATABASE_URL')
if not database_path:
    database_path = "postgres://postgres:postgres@localhost:5432/capstone"

database_test_path = "postgres://postgres:postgres@localhost:5432/capstone_test"

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()

def setup_test_db(app, database_path=database_test_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Institution(db.Model):
    __tablename__ = 'institutions'
    email = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime())
    session = db.relationship('Session', backref='institution', lazy=True, cascade='all, delete')

    def __init__(self, name, location, email, created_at):
        self.name = name
        self.location = location
        self.email = email
        self.created_at = created_at

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'email': self.email,
            'name': self.name,
            'location': self.location,
            'created_at': self.created_at,
        }

class Musician(db.Model):
    __tablename__ = 'musicians'
    email = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    genre = db.Column(db.String(), nullable=False)
    instrument = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime())

    def __init__(self, name, genre, instrument, email, created_at):
        self.name = name
        self.genre = genre
        self.instrument = instrument
        self.email = email
        self.created_at = created_at

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'email': self.email,
            'name': self.name,
            'genre': self.genre,
            'instrument': self.instrument,
            'created_at': self.created_at
        }


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    institution_email = db.Column(db.String(), db.ForeignKey('institutions.email'), nullable=False)
    is_open = db.Column(db.Boolean(), default=True)
    location = db.Column(db.String(), nullable=False)
    schedule = db.Column(db.DateTime(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    imgURL = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime())

    def __init__(self, institution_email, location, schedule, title, description, imgURL, created_at):
        self.institution_email = institution_email
        self.location = location
        self.schedule = schedule
        self.title = title
        self.description = description
        self.imgURL = imgURL
        self.created_at = created_at

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'institution_email': self.institution_email,
            'is_open': self.is_open,
            'location': self.location,
            'schedule': self.schedule,
            'title': self.title,
            'description': self.description,
            'imgURL': self.imgURL,
            'created_at': self.created_at
        }

# flask db migrate
# flask upgrade/downgrade

# seed db
session = Session(
    institution_email='inst@email.com',
    title='session title',
    description='something about session...',
    location='Montreal, QC, CA',
    schedule='2022-02-25 18:00:00',
    imgURL='',
    created_at='2022-02-01 18:00:00'
)

institution = Institution(
    name='institution name',
    location='Montreal, QC, CA',
    email='inst@email.com',
    created_at='2022-02-25 18:00:00'
)

musician = Musician(
    name='musician name',
    genre='Classical',
    instrument='Piano',
    email='musician@email.com',
    created_at='2022-02-25 18:00:00'
)
