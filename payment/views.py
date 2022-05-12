import stripe
import os
from dotenv import find_dotenv, load_dotenv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace(".", "")
    total = int(total)
    load_dotenv(find_dotenv(".env"))
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
    intent = stripe.PaymentIntent.create(
        amount=total, currency="gbp", metadata={"userid": request.user.id}
    )

    context = {"client_secret": intent.client_secret}
    return render(request, "payment/home.html", context)
