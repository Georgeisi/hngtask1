import unittest
from django.test import Client
from django.urls import reverse
from rest_framework import status

class TestPersonAPI(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_person(self):
        # Define the data for creating a person
        data = {"name": "John Doe", "age": 30}
        response = self.client.post(reverse("person-list"), data, content_type="application/json")
        
        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

if __name__ == "__main__":
    unittest.main()