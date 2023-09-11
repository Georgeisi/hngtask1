
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Person

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person

class PersonAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_person(self):
        data = {"name": "John Doe", "age": 30}
        response = self.client.post(reverse("person-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, "John Doe")
    
    def test_get_person(self):
        person = Person.objects.create(name="Jane Smith", age=25)
        response = self.client.get(reverse("person-detail", kwargs={"pk": person.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Jane Smith")

    def test_update_person(self):
        person = Person.objects.create(name="Alice Johnson", age=35)
        data = {"name": "Updated Name", "age": 40}
        response = self.client.put(reverse("person-detail", kwargs={"pk": person.pk}), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get(pk=person.pk).name, "Updated Name")

    def test_delete_person(self):
        person = Person.objects.create(name="Bob Brown", age=45)
        response = self.client.delete(reverse("person-detail", kwargs={"pk": person.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)


