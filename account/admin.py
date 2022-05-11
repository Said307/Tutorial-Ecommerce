from django.contrib import admin

# Register your models here.


from .models import UserBase

admin.site.register(UserBase)

""" 
@admin.register(UserBase)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk","first_name","email"]
"""
