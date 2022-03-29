from django.shortcuts import render

from .models import *



def all_products(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {'products':products,'categories':categories}
    return render(request,'store/home.html',context)


