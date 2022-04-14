from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Category, Product


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.active_products.filter(category=category)
    context = {"products": products, "category": category}
    return render(request, "store/products/category.html", context)


def products_all(request):
    products = Product.active_products.all()
    q = request.GET.get("q")
    if q:
        products = Product.active_products.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
    context = {"products": products}
    return render(request, "store/home.html", context)


def product_detail(request, product_slug):
    product = Product.active_products.get(slug=product_slug, in_stock=True)
    # product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {"product": product}
    return render(request, "store/products/product_detail.html", context)


dict = {
    "dddd": "ddsds",
    "dddd": "ddsds",
    "dddd": "ddsds",
    "dddd": "ddsds",
}
