from flask_sqlalchemy import SQLAlchemy
from app.app import app
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://manattan:@localhost/npb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class uniformNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(2), nullable=False)
    history = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<history %r>' % self.history
