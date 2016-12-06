import flask
import random

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

WORDS = open("palabras.txt").read().splitlines()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hola! Probablemente quieres /random'

@app.route('/random')
def random_word():
    """Return a random word."""
    index = random.randint(1, len(WORDS)) - 1
    word = WORDS[index]
    response = "{'palabra': '%s', 'index': %d}" % (word, index)
    return flask.Response(response, mimetype='application/json')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
