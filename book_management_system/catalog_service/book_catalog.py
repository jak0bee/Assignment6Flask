# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

from flask import Flask, jsonify, abort, request
import requests
from book_management_system.catalog_service.catalog_mock_database import books

app = Flask(__name__)

INVENTORY_SERVICE = "http://localhost:3002"


@app.route('/catalog/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if not book:
        abort(404)
    return jsonify({'book': book[0]}), 200


@app.route('/catalog/create', methods=['POST'])
def create_book():
    if not request.json or 'title' not in request.json or 'author' not in request.json \
            or 'publication_year' not in request.json:
        abort(400)
    if type(request.json['publication_year']) is not int:
        abort(400)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'publication_year': request.json['publication_year']
    }
    try:
        requests.post(f"{INVENTORY_SERVICE}/inventory/create", json={'book_id': new_book['id']})
    except requests.exceptions.RequestException:
        abort(500)
    books.append(new_book)
    return jsonify({'book': new_book}), 201


@app.route('/catalog/delete', methods=['DELETE'])
def delete_book():
    if not request.json or 'book_id' not in request.json or type(request.json['book_id']) is not int:
        abort(404)

    book_id = request.json['book_id']
    book = [book for book in books if book['id'] == book_id]
    if not book:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True}), 204


@app.route('/catalog/update', methods=['PUT'])
def update_book():
    if not request.json or 'book_id' not in request.json or type(request.json['book_id']) is not int:
        abort(404)
    book_id = request.json['book_id']
    book = [book for book in books if book['id'] == book_id]
    if not book:
        abort(400)

    if 'title' in request.json:
        book[0]['title'] = request.json.get('title')

    if 'author' in request.json:
        book[0]['author'] = request.json.get('author')

    if 'publication_year' in request.json and type(request.json['publication_year']) is int:
        book[0]['publication_year'] = request.json.get('publication_year')

    return jsonify({'book': book[0]})


if __name__ == '__main__':
    app.run(port=3001)
