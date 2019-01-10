import markov
from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_json():
    """ takes in POST data as JSON from Node app and converts values to make
    them accessible to rest of Flask app """
    if request.method == 'GET': # only executed with HTTP GET requests
        return """Please send a POST request to use this application.
                For additional information on use of this API, documentation can be
                found at: https://github.com/fchikwekwe/name-ly-API.
                """

    params = request.get_json()

    # get the user's answers and add file extension
    name_number = params['nameNumber']
    gender = params['gender'] + '.txt'
    cultural = params['cultural'] + '.txt'
    literary = params['literary'] + '.txt'

    markov_name = markov.main(name_number, gender, cultural, literary, 'corpus.txt')
    return jsonify(name=markov_name)

@app.route('/index')
def index():
    """ Demonstration of api; returns a web template"""
    index_name = markov.main(10, 'feminine.txt', 'fantasy.txt', 'modern.txt', 'corpus.txt')
    return render_template('index.html', index_name=index_name)


@app.route('/api')
def return_json():
    """ Demonstration of api; returns json result """
    json_name = markov.main(10, 'masculine.txt', 'fantasy.txt', 'modern.txt', 'corpus.txt')
    return jsonify(json_name)
