# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

from flask import Flask, jsonify, abort, request
import requests
from book_management_system.order_service.order_mock_database import orders

app = Flask(__name__)

BOOK_INVENTORY_SERVICE = "http://localhost:3002"


@app.route('/orders/get', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/orders/create', methods=['POST'])
def add_order():
    if not request.json or 'book_id' not in request.json or 'quantity' not in request.json or 'date' not in request.json:
        abort(404)
    book_id = request.json['book_id']
    quantity = request.json['quantity']
    date = request.json['date']
    if type(book_id) is not int or type(quantity) is not int:
        abort(400)
    new_order = {
        'book_id': book_id,
        'quantity': quantity,
        'date': date
    }
    try:
        response = requests.get(f"{BOOK_INVENTORY_SERVICE}/inventory")
        response.raise_for_status()  # exception if the response was not successful
        inventory = response.json()
        current_quantity = 0
        for item in inventory:
            if item['book_id'] == book_id:
                current_quantity = item['quantity']
                break

        updated_quantity = current_quantity + new_order['quantity']
        requests.put(f"{BOOK_INVENTORY_SERVICE}/inventory/update",
                     json={'book_id': new_order['book_id'], 'quantity': updated_quantity})

    except requests.exceptions.RequestException:
        abort(500)
    orders.append(new_order)
    return jsonify(new_order), 201


if __name__ == '__main__':
    app.run(port=3003)
