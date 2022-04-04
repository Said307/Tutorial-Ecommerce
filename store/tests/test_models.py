
from django.test import TestCase
from ..models import *



class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django',slug='django')
        

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

