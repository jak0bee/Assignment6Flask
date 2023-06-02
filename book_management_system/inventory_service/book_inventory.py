# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

from flask import Flask, abort, request, jsonify
from book_management_system.inventory_service.inventory_mock_database import inventory

app = Flask(__name__)


@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)


@app.route('/inventory/create', methods=['POST'])
def add_book():
    if not request.json or 'book_id' not in request.json:
        abort(404)
    new_book = {
        "book_id": request.json.get('book_id'),
        "quantity": 2
    }
    inventory.append(new_book)
    return jsonify({'book': new_book}), 201


@app.route('/inventory/update', methods=['PUT'])
def update_inventory():
    if not request.json or 'book_id' not in request.json or 'quantity' not in request.json:
        abort(400)
    book_id = request.json['book_id']
    item = [item for item in inventory if item['book_id'] == book_id]
    if not item:
        abort(400)
    if type(request.json['quantity']) is not int:
        abort(400)

    item[0]['quantity'] = request.json['quantity']
    return jsonify(item)


if __name__ == '__main__':
    app.run(port=3002)
