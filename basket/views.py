from django.shortcuts import render, get_object_or_404

from .models import *


def basket_summary(request):

    context = {}
    return render(request, "store/basket/summary.html", context)
