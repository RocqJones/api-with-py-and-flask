import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# create a book
books = [
    {
        'id' : 0,
        'title' : 'Rich Dad Poor Dad',
        'author': 'Robert Kiyosaki',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '2005'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>'''

# rouute all to return all available entries in a catalog 'http://127.0.0.1:5000/api/v1/resources/books/all'
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# Finding Specific Resources
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    """
        Check if an ID was provided as part of the URL.
        If ID is provided, assign it to a variable.
        If no ID is provided, display an error in the browser.
    """
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No 'id' provided. please specify an 'id'!!!"

    # create an empty list for our results
    results = []

    """
        Loop through the data and match results that fit the requested ID.
        IDs are unique, but other fields might return many results
    """
    for book in books:
        if book['id'] == id:
            results.append(book)

    # convert the results into json format
    return jsonify(results) 

app.run()