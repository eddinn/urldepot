import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

URLS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_url(url_id):
    for url in URLS:
        if url['id'] == url_id:
            URLS.remove(url)
            return True
    return False

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/urls', methods=['GET', 'POST'])
def urls():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        URLS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Url added!'
    else:
        response_object['urls'] = URLS
    return jsonify(response_object)

@app.route('/urls/<url_id>', methods=['PUT', 'DELETE'])
def single_url(url_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_url(url_id)
        URLS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Url updated!'
    if request.method == 'DELETE':
        remove_url(url_id)
        response_object['message'] = 'Url removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
