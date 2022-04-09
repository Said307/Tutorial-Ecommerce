from itertools import product
from unicodedata import category
from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}  # slug get populated automatically


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "slug",
        "price",
        "in_stock",
        "created",
        "updated",
    ]
    prepopulated_fields = {"slug": ("title",)}  # slug get populated automatically
    list_filter = ["in_stock", "is_active"]
    list_editable = ["price", "in_stock"]
