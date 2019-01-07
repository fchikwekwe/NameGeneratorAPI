import markov
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

SOURCE_TEXT = 'girl.txt'
NAME_LIST = markov.list_names(SOURCE_TEXT)
CLEANED_TEXT = markov.cleanup(SOURCE_TEXT)
TEXT_LIST = markov.tokenize(CLEANED_TEXT)

@app.route('/', methods=['GET', 'POST'])
def json():
    """ takes in POST data from Node app and dumps JSON values to make them
    accessible to rest of Flask app """
    params = {
        'questionOne': request.get_json.get('questionOne'),
        'questionTwo': request.get_json.get('questionTwo'),
        'questionThree': request.get_json.get('questionThree')
    }
    print(json.dumps(params))
    return json.dumps(params)

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
