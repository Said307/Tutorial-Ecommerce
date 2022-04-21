
from django.contrib.auth.models import User
from django.test import TestCase,Client
from django.urls import reverse
from django.http import HttpRequest
from store.models import Category,Product
 



class TestBasketView(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='django',slug='django')
        Product.objects.create(
            category_id=1,
            quantity=55,
            price=60,
            title="django beginners",
            created_by_id=1,
            slug="django-beginners",
            image="django",
        )

        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)

    def test_basket_home_url(self):

        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code,200)

    def test_basket_add_request(self):
        """
        Testing adding items to the basket """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(),{'qty':4})

        