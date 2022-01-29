from flask import Flask, render_template, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jbduzvmgcsebtb:27f5e32b0cebfa3ca9171208a59eda40e00cd70a99d810eccf30c61a66b526ba@ec2-54-73-152-36.eu-west-1.compute.amazonaws.com:5432/dasvmqpo1ebrjj'
db = SQLAlchemy(app)

#postgresql://pguser:pgpassword@localhost:5433/app_db
class Guest(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)

    def __repr__(self):
        return self.username


db.create_all()

text = None 



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/name', methods=['GET', 'POST'])
def add_name():
    try:
        user = Guest(username=request.form['name'])
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return render_template('greetings.html', user=user)
    except:
        db.session.rollback()
        return render_template('seen.html', user=user)



@app.route('/collection', methods=['GET'])
def collection():
    return render_template('collection.html', collection=Guest.query.all())
