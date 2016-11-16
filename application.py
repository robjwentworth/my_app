import flask
import os
import sys
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask import Flask, request, render_template
import cPickle as pickle

# Default config vals
THEME = 'default' if os.environ.get('THEME') is None else os.environ.get('THEME')
FLASK_DEBUG = 'false' if os.environ.get('FLASK_DEBUG') is None else os.environ.get('FLASK_DEBUG')

application = flask.Flask(__name__)

# Load config values specified above
application.config.from_object(__name__)

# Load configuration vals from a file
application.config.from_envvar('APP_CONFIG', silent=True)

# Only enable Flask debugging if an env var is set to true
application.debug = application.config['FLASK_DEBUG'] in ['true', 'True', '1']

with open('data/vectorizer.pkl') as f:
    vectorizer = pickle.load(f)
with open('data/model.pkl') as g:
    model = pickle.load(g)


# home page
@application.route('/')
def index():
    return flask.render_template('index.html', flask_debug=application.debug)

##@application.route('/submit')
##def submit():
##    return render_template('submit.html')

@application.route('/predict', methods=['POST'] )
def predict():

    text = str(request.form['user_inputs'])
    #X = vectorizer.transform(unicode(text, errors ='ignore'))
    X = vectorizer.transform([text])
    p = model.predict(X)
    return flask.render_template('predict.html').format(p[0])

if __name__ == '__main__':
##    with open('data/vectorizer.pkl') as f:
##        vectorizer = pickle.load(f)
##    with open('data/model.pkl') as g:
##        model = pickle.load(g)
    application.run(host='0.0.0.0')
