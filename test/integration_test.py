# by Software Engineering Assignments 55: Jakub Suszwedyk: 6310933   and Marcell Dorko: 6326607

import unittest
import requests


class TestIntegration(unittest.TestCase):
    """
    In order for the tests to be correct, the run_services.py script from the main packages has to also be running.
    """
    BASE_URL = 'http://localhost:3000'

    def test_create_get_delete_book(self):
        # creates new book
        response = requests.post(f"{self.BASE_URL}/catalog/create",
                                 json={'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2023})
        self.assertEqual(response.status_code, 201)

        # attempts to retrieve the new book from the catalog
        response = requests.get(f"{self.BASE_URL}/catalog/3")
        self.assertEqual(response.json(),
                         {'book':
                              {'id': 3, 'title': 'Book 3', 'author': 'Author 3', 'publication_year': 2023}})
        self.assertEqual(response.status_code, 200)

        # deletes the book
        response = requests.delete(f"{self.BASE_URL}/catalog/delete", json={'book_id': 3})
        self.assertEqual(response.status_code, 204)

        # attempts to retrieve the deleted book
        response = requests.get(f"{self.BASE_URL}/catalog/3")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
