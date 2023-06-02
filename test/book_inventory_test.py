# by Software Engineering Assignments 55: Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

import unittest
from book_management_system.inventory_service.book_inventory import app, inventory


class TestBookInventory(unittest.TestCase):
    """
    In order for the tests to be correct, the run_services.py script from the main packages has to also be running.
    """

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_inventory(self):
        response = self.app.get('/inventory')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, inventory)

    def test_add_book(self):
        response = self.app.post('/inventory/create', json={'book_id': 3})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'book': {'book_id': 3, 'quantity': 2}})

    def test_add_book_no_id(self):
        response = self.app.post('/inventory/create', json={})
        self.assertEqual(response.status_code, 404)

    def test_update_inventory(self):
        response = self.app.put('/inventory/update', json={'book_id': 1, 'quantity': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'book_id': 1, 'quantity': 5}])

    def test_update_inventory_wrong_id(self):
        response = self.app.put('/inventory/update', json={'book_id': 4, 'quantity': 5})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
