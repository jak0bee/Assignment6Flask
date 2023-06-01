from flask import Flask, abort, request, jsonify

app = Flask(__name__)

inventory = [
    {"book_id": 1, "quantity": 2},
    {"book_id": 2, "quantity": 3}
]


@app.route('/inventory/add', methods=['PUT'])
def add_book():
    if not request.json or 'book_id' not in request.json:
        abort(404)
    new_book = {
        "book_id": request.json.get['book_id'],
        "quantity": 2
    }
    inventory.append(new_book)
    return jsonify({'book': new_book}), 201
