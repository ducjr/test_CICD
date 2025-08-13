from django.test import TestCase
from django.urls import reverse
from .models import Greeting


class HelloTests(TestCase):
    def test_root_returns_hello(self):
        Greeting.objects.create(message='Hello, CI/CD!')
        resp = self.client.get(reverse('hello'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Hello, CI/CD!', resp.content)
