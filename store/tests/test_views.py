

from unittest import skip
from django.test import TestCase

from django.contrib.auth.models import User

from store.models import Category, Product

from django.test import Client


@skip("This is a skipped test")
class SkipSample(TestCase):
    def test_banana(self):
        """practising tests
        """
        key=1
        self.assertTrue(key)



class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """ Test allowed host"""
        response = self.c.get('/')
        self.assertEqual(response.status_code,200)
      