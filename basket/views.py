from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from store.models import Product
from .basket import Basket


def basket_summary(request):

    context = {}
    return render(request, "store/basket/summary.html", context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get("action") == "basket_key":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

    return JsonResponse({"qty": product_qty})
