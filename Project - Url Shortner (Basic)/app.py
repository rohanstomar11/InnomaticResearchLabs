from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters =  ''.join(random.SystemRandom().choice(
        string.ascii_letters + \
        string.digits) for _ in range(10))
        short_url = urls2.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

@app.before_first_request
def create_tables():
    db.create_all()

class urls2(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short


@app.route('/')
def home_get():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    original_url = request.form.get('original')
    short_url = urls2.query.filter_by(long=original_url).first()
    if short_url:
        url = "http://127.0.0.1:5000/"+short_url.short
        return render_template('index.html', shortUrl = url)
    else:
        short_url = shorten_url()
        print(short_url)
        new_url = urls2(original_url, short_url)
        db.session.add(new_url)
        db.session.commit()            
        url = "127.0.0.1:5000/"+short_url
        return render_template('index.html', shortUrl = url)

@app.route('/history')
def history_get():
    return render_template('history.html', values=urls2.query.all())

@app.route('/<url>')
def fun(url):
    original = urls2.query.filter_by(short=url).first()
    if original:
        return redirect(original.long)
    else:
        return f'<h1>Url doesnt exist</h1>'

if __name__ == "__main__":
    app.run(debug=True)