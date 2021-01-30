from flask_sqlalchemy import SQLAlchemy
import os
from app.app import app
from datetime import datetime

user=os.environ['username']
db = os.environ['db']

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:@localhost/{}'.format(user, db)
app.config['SQLALCHEMY_DATABASE_URL'] = 'postgres://yqetdzwcoulinz:@ec2-52-6-75-198.compute-1.amazonaws.com:5432/d8qig3udtsa2l7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class allteam2020(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    teamname = db.Column(db.String(2), nullable=False)
    history = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<history %r>' % self.history
