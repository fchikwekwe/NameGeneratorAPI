import markov
from flask import Flask, render_template, jsonify

APP = Flask(__name__)

SOURCE_TEXT = 'girl.txt'
NAME_LIST = markov.list_names(SOURCE_TEXT)
CLEANED_TEXT = markov.cleanup(SOURCE_TEXT)
TEXT_LIST = markov.tokenize(CLEANED_TEXT)

@APP.route('/')

def index():
    """ returns a web template"""
    index_name = markov.main(NAME_LIST, TEXT_LIST)

    return render_template('index.html', index_name=index_name)


@APP.route('/api')

def return_json():
    """ returns json result """
    json_name = markov.main(NAME_LIST, TEXT_LIST)

    return jsonify(json_name)
