import random

from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

WORDS = open("palabras.txt").read().splitlines()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! I\'m Brian!'

@app.route('/random')
def random_word():
    """Return a random word."""
    return random.choice(WORDS)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
