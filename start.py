import collections
from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from settings import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config[SQLALCHEMY_DATABASE_URI] = 'postgresql://xdfhkkmhunxxim:5b2f2c590b5963a8bd3422bce0283a7730a9b0dea7ee2a7580e15ee291f7e8d6@ec2-34-242-89-204.eu-west-1.compute.amazonaws.com:5432/d1r7qn9gh3f6ug'
db = SQLAlchemy(app)


class Guest(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)

    def __repr__(self):
        return self.username


db.create_all()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/name', methods=['GET' 'POST'])
def add_name():
    try:
        user = Guest(username=request.form['name'])
        db.session.add(user)
        db.session.commit()
        return render_template('greetings.html', user=user)
    except:
        db.session.rollback()
        return render_template('seen.html', user=user)


@app.route('/collection', methods=['GET'])
def collection():
    collection = Guest.query.all() 
    return render_template('collection.html', collection=collection)
