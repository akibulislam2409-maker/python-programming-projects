import unittest

class TestLibrarySystem(unittest.TestCase):

    def test_add_book(self):
        books = []
        books.append({
            "id": 1,
            "title": "Test Book",
            "author": "Author",
            "genre": "Fiction",
            "year": 2020,
            "copies": 2
        })
        self.assertEqual(len(books), 1)

    def test_search_books(self):
        books = [{"id":1,"title":"Python","author":"John"}]
        keyword = "python"
        results = [b for b in books if keyword in b["title"].lower()]
        self.assertEqual(len(results), 1)

    def test_remove_book(self):
        books = [{"id":1,"title":"Test"}]
        books = [b for b in books if b["id"] != 1]
        self.assertEqual(len(books), 0)

    def test_invalid_login(self):
        USERS = {"admin": "123"}
        self.assertFalse("wrong" == USERS.get("admin"))

    def test_valid_login(self):
        USERS = {"admin": "123"}
        self.assertTrue("123" == USERS.get("admin"))

if __name__ == "__main__":
    unittest.main()
