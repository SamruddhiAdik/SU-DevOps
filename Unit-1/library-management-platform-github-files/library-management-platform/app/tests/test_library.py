"""Basic automated tests for the starter API."""
import os
import tempfile
import unittest
from app.main import create_app
from app.database import db

class LibraryApiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.NamedTemporaryFile(delete=False)
        self.temp.close()
        db.DB_PATH = self.temp.name
        self.client = create_app().test_client()

    def tearDown(self):
        try:
            os.unlink(self.temp.name)
        except FileNotFoundError:
            pass

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "ok")

    def test_add_and_list_book(self):
        response = self.client.post("/books", json={
            "title": "Test Book", "author": "A. Writer", "isbn": "TEST-001"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.client.get("/books").json[0]["title"], "Test Book")

    def test_missing_required_fields(self):
        response = self.client.post("/books", json={"title": "Incomplete"})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
