# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607
import requests
from flask import Flask, json, jsonify, abort, request

app = Flask(__name__)

BOOK_INVENTORY_SERVICE = "http://localhost:3002"

orders = [
    {"book_id": 2, "quantity": 3, 'date': "31.05.2020"},
    {"book_id": 1, "quantity": 4, 'date': "28.06.1996"}
]


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
        response.raise_for_status()  # Raise an exception if the response was not successful
        inventory = response.json()
        current_quantity = 0
        for item in inventory:
            if item['book_id'] == book_id:
                current_quantity = item['quantity']
                break

        updated_quantity = current_quantity + new_order['quantity']
        requests.put(f"{BOOK_INVENTORY_SERVICE}/inventory/update",
                     json={'book_id': new_order['book_id'], 'quantity': updated_quantity})

    except requests.exceptions.RequestException as e:
        abort(500)
    orders.append(new_order)
    return jsonify(new_order)


if __name__ == '__main__':
    app.run(port=3003)
