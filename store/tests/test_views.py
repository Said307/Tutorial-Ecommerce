from unittest import skip

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from store.models import Category, Product
from django.urls import reverse
from django.http import HttpRequest

from store.views import products_all


@skip("This is a skipped test")
class SkipSample(TestCase):
    def test_banana(self):
        """practising tests"""
        key = 1
        self.assertTrue(key)


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username="sadiq")
        Category.objects.create(name="GCSE", slug="GCSE")
        Product.objects.create(
            category_id=1,
            quantity=55,
            price=60,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            image="django",
        )

    def test_url_allowed_hosts(self):
        """Test allowed host"""
        response = self.c.get("/", HTTP_HOST="unwanted.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get("/", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse("store:category_list", args=["GCSE"]))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test product response status
        """
        response = self.c.get(
            reverse("store:product_detail", args=["django-beginners"])
        )
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Test homepage content,
        """
        request = HttpRequest()
        response = products_all(request)
        html = response.content.decode("utf-8")
        self.assertIn("Bookstore", html)

    def test_view_function(self):
        """
        Test all_products view
        """
        request = self.factory.get("/item/django-beginners")
        response = products_all(request)
        html = response.content.decode("utf-8")
        self.assertIn("django beginners", html)
        self.assertTrue(response.status_code, 200)
