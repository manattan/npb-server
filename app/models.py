from flask_sqlalchemy import SQLAlchemy
from app.app import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://manattan:@localhost/npb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Maint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    teamname = db.Column(db.String(2), nullable=False, unique=True)
    history = db.Column(db.String(100), nullable=False)

    childs = db.relationship('Team')

    def __repr__(self):
        return '<history %r>' % self.history

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_alpha = db.Column(db.String(2))
    name = db.Column(db.String(20))
    def __repr__(self):
        return '<name %r>' % self.name
