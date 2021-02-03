from flask_sqlalchemy import SQLAlchemy
import os
from app.app import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class allteam2020(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    teamname = db.Column(db.String(2), nullable=False)
    history = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<history %r>' % self.history
