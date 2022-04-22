
from django.contrib.auth.models import User
from django.test import TestCase,Client
from django.urls import reverse
from django.http import HttpRequest
from store.models import Category,Product
 



class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners',quantity='10', created_by_id=1,
                               slug='django-beginners', price='10.00', image='django')
        Product.objects.create(category_id=1, title='django intermediate',quantity='20', created_by_id=1,
                               slug='django-beginners', price='10.00', image='django')
        Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                               slug='django-beginners', price='10.00', quantity='30', image='django')
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)
        
    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 3, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 6})
         

    
    def test_basket_update(self):
        """ 
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 1, "productqty": 50, "action": "post"}, xhr=True)
      
        self.assertEqual(response.json(),{"qty": 52, "subtotal": "520.00"})
         

  
    def test_basket_delete(self):
         
       # Test adding items to the basket

        response = self.client.post(
            reverse('basket:basket_delete'), {"productid":1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(),{"qty": 2, "subtotal": "20.00"})
 