
from django.test import TestCase
from ..models import *



class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django',id=5)
        

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data,Category))

    def test_category_model_return(self):
        """
        Test Category model default name
        """
        
        self.assertEqual(str(self.data1),'django')


class TestProductModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django',id=5)
        self.user = User.objects.create(first_name='hassan')
        self.data2 = Product.objects.create(title='GCSE',quantity=50,price=44,created_by=self.user,category_id=5)

    
    def test_product_model_entry(self):
        
        """
        Test Product model data insertion/types/field attributes
         """
        data = self.data2
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data),'GCSb')