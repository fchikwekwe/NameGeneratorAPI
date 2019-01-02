import markov
from flask import Flask, jsonify

APP = Flask(__name__)

SOURCE_TEXT = 'names.txt'
CLEANED_TEXT = markov.cleanup(SOURCE_TEXT)
TEXT_LIST = markov.tokenize(CLEANED_TEXT)

@APP.route('/', methods=['GET'])

def index():
    """ call methods and send to flask app """
    json_name = markov.main(TEXT_LIST)

    return jsonify(json_name)
