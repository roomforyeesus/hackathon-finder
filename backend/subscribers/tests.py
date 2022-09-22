from django.test import TestCase
import unittest

# Create your tests here.
class TestSubscriberView(TestCase):
    def test_get(self):
        response = self.client.get('/subscribers/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post('/subscribers/', {'email': '', 'name': ''})
