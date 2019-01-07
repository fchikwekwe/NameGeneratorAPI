import markov
from flask import Flask, request, render_template, jsonify, json

app = Flask(__name__)

SOURCE_TEXT = 'girl.txt'
NAME_LIST = markov.list_names(SOURCE_TEXT)
CLEANED_TEXT = markov.cleanup(SOURCE_TEXT)
TEXT_LIST = markov.tokenize(CLEANED_TEXT)

@app.route('/', methods=['GET', 'POST'])
def parse_json():
    """ takes in POST data from Node app and dumps JSON values to make them
    accessible to rest of Flask app """
    if request.method == 'GET': # only executed with HTTP GET requests
        return "Please send a POST request to use this application."

    params = request.json()

    questionOne = params['questionOne']
    questionTwo = params['questionTwo']
    questionThree = params['questionThree']

    print(json.dumps(questionOne))
    return json.dumps(questionOne)

@app.route('/index')
def index():
    """ demonstrates api; returns a web template"""
    index_name = markov.main(NAME_LIST, TEXT_LIST)
    return render_template('index.html', index_name=index_name)


@app.route('/api')
def return_json():
    """ demonstrates api; returns json result """
    json_name = markov.main(NAME_LIST, TEXT_LIST)
    return jsonify(json_name)
