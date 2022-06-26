from decimal import Decimal

from store.models import Product


class Basket:
    """A basket class providing default behaviours which
    can be inherited or overriden as necessary"""

    def __init__(self, request):
        """creates a session on any page the user visits"""
        self.session = request.session
        basket = request.session.get("skey")
        if not basket:
            basket = request.session["skey"] = {}
        self.basket = basket

    def add(self, product, qty):
        """Adding product to user basket session data"""
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {
                "price": str(product.price),
                "qty": int(qty),
            }

        self.session.modified = True

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())

    def __iter__(self):
        """iterate over the session data of
        basket items and fetch the from the database"""
        product_ids = self.basket.keys()
        products = Product.active_products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]

            yield item

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]["qty"] = qty
        self.save()

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )

    def get_subtotal_price(self):
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.basket.values()
        )

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
             
            self.save()

    def save(self):
        self.session.modified = True
    
    def clear(self):
        self.basket.clear()