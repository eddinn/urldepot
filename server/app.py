import uuid, os

from flask import Flask, json, jsonify, request
from flask_cors import CORS

#URLS = [
#    {
#        'id': uuid.uuid4().hex,
#        'url': 'https://github.com/eddinn/',
#        'category': 'Github',
#    },
#    {
#        'id': uuid.uuid4().hex,
#        'url': 'https://eddinn.net/',
#        'category': 'Blog'
#    }
#]

URLS = []

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

def sync_to_disk():
    with open("urls.json", "a+") as write_file:
        json.dump(URLS, write_file)

def open_file():
    with open("urls.json", "r") as read_file:
        URLS = json.load(read_file)

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
            'url': post_data.get('url'),
            'category': post_data.get('category')
        })
        sync_to_disk
        response_object['message'] = 'Url added!'
    else:
        open_file
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
            'url': post_data.get('url'),
            'category': post_data.get('category'),
        })
        sync_to_disk
        response_object['message'] = 'Url updated!'
    if request.method == 'DELETE':
        remove_url(url_id)
        sync_to_disk
        response_object['message'] = 'Url removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
