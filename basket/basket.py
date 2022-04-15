class Basket:
    """A basket class providing default behaviours which
    can be inherited or overriden as necessary"""

    def __init__(self, request):
        """creates a session on any page the user visits"""
        self.session = request.session
        basket = self.session.get("skey")
        if not basket:
            basket = self.session["skey"] = {}
        self.basket = basket

    def add(self, product):
        """Adding product to user basket session data"""
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {"price": str(product.price)}

        self.session.modified = True
