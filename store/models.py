#from curses.ascii import FF
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)

    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def get_absolute_url(self):
        """ URL name """
        return reverse('store:category_list',args=[self.slug])
 
    def __str__(self):
        return self.name
        



class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator',on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    author = models.CharField(max_length=255,default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)   
    
    
 
    def __str__(self):
        return self.title
        