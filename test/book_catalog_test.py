# done by Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

import unittest
from unittest.mock import patch

from book_management_system.catalog_service.book_catalog import app, books


class TestBookCatalog(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_book(self):
        response = self.app.get('/catalog/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'book': books[0]})

    def test_get_book_not_found(self):
        response = self.app.get('/catalog/100')
        self.assertEqual(response.status_code, 404)

    @patch('requests.post')
    def test_create_book(self, mock_post):
        mock_post.return_value.status_code = 201
        response = self.app.post('/catalog/create',
                                 json={'id': 3, 'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2023})
        self.assertEqual(response.status_code, 201)

    @patch('requests.post')
    def test_create_book_missing_fields(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {'book_id': 3}
        response = self.app.post('/catalog/create', json={'author': 'Author 3', 'publication_year': 2023})
        self.assertEqual(response.status_code, 400)

    def test_delete_book(self):
        response = self.app.delete('/catalog/delete', json={'book_id': 3})
        self.assertEqual(response.json, {'result': True})
        self.assertEqual(response.status_code, 200)

    def test_delete_book_wrong_id(self):
        response = self.app.delete('/catalog/delete', json={'book_id': 4})
        self.assertEqual(response.status_code, 404)

    def test_update_book(self):
        response = self.app.put('catalog/update',
                                json={'book_id': 1, 'title': 'Changed Title', 'author': 'Changed Author',
                                      'publication_year': 1925})
        updatedBook = None
        for book in books:
            if book['id'] == 1:
                updatedBook = book
        self.assertEqual(updatedBook,
                         {'id': 1, 'title': 'Changed Title', 'author': 'Changed Author', 'publication_year': 1925})
        self.assertEqual(response.status_code, 200)

    def test_update_book_wrong_id(self):
        response = self.app.put('catalog/update',
                                json={'book_id': 4, 'title': 'Changed Title', 'author': 'Changed Author',
                                      'publication_year': 1925})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
