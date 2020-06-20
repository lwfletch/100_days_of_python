import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

courses = [
    {
        'id': 1,
        'title': "Intro to HTML",
        'author': 'Trey Fletcher',
    },
    {
        'id': 2,
        'title': "Intro to Advanced HTML",
        'author': 'Trey Fletcher',
    },
    {
        'id': 3,
        'title': "Intro to CSS",
        'author': 'Trey Fletcher',
    },
    {
        'id': 4,
        'title': "Advanced CSS",
        'author': 'Trey Fletcher',
    },
]

@app.route('/', methods=['GET'])

def home():
    return "<h3>API Works</h3>"

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(courses)

@app.route('/api/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error no ID provided. Please specify an id"

    results = []

    for course in courses:
        if course['id'] == id:
            results.append(course)
    
    return jsonify(results)

app.run()