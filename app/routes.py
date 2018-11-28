from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nico'}
    posts = [
        {
            'author': {'username': 'Ashley'},
            'body': 'Beautiful day in Denver!'
        },
        {
            'author': {'username': 'Mom'},
            'body': 'The Avengers movie was so Horrible!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
