
from decimal import Decimal

from tabnanny import verbose
from django.db import models
from django.shortcuts import reverse
from django.conf import settings

from store.models import Product
# Create your models here.



class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="order_user")
    id =
    created =

    paid =



    class Meta:

        ordering = ["-created"]
        verbose_name_plural = "Orders"

        def __str__(self):
            return self.id

        def get_absolute_url(self):
            """URL name"""
            return reverse("orders:order_detail", args=[self.id])

