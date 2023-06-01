from flask import Flask, abort, json, request

app = Flask(__name__)

inventory = [
    {"book_id": 1, "quantity": 2},
    {"book_id": 2, "quantity": 3}
]

