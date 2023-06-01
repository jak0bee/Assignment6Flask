import requests
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'}
]


@app.route('/catalog/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@app.route('/catalog/create', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json or not 'author' in request.json:
        abort(400)
    new_book = {
        'id': books[-1]['id'] + 1,  # Assign the next ID to the new book
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify({'book': new_book}), 201



if __name__ == '__main__':
    app.run(port=3001)
