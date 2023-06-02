# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

import unittest
from unittest.mock import patch
from book_management_system.order_service.book_order import app, orders


class TestBookOrder(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_orders(self):
        response = self.app.get('/orders/get')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, orders)

    @patch('requests.get')
    @patch('requests.put')
    def test_add_order(self, mock_put, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'book_id': 1, 'quantity': 10}]
        mock_put.return_value.status_code = 200

        response = self.app.post('/orders/create', json={'book_id': 1, 'quantity': 2, 'date': '28.02.2023'})
        self.assertEqual(response.status_code, 201)

    @patch('requests.get')
    @patch('requests.put')
    def test_add_order_no_id(self, mock_put, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'book_id': 1, 'quantity': 10}]
        mock_put.return_value.status_code = 200

        response = self.app.post('/orders/create', json={'quantity': 2})
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
