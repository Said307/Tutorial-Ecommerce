from django.shortcuts import render,get_object_or_404

from .models import Category, Product




def category_list(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category) 
    context = {'products':products,'category':category}
    return render(request,'store/products/category.html',context)

def all_products(request):
    products = Product.objects.filter(is_active=True)
    context = {'products':products,}
    return render(request,'store/home.html',context)


def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug,in_stock=True)
    context = {'product':product}
    return render(request,'store/products/detail.html',context)

