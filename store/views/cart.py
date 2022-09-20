from statistics import median_high
from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def __init__(self):
        self.cart_msg = False

    def post(self, request):
        product_id = request.POST.get("product_id")
        cart = request.session.get("cart")
        if product_id in list(cart.keys()):
            self.cart_msg = True
            request.session["cart_msg"] = "Product removed successfully"
            del cart[product_id]
        request.session["cart"] = cart        
        return Cart.get(self, request)
    
    def get(self, request):
        if not self.cart_msg :            
            request.session["cart_msg"] = {}        
        ids = list(request.session.get('cart').keys())
        cart_empty = {}
        cart_empty["flag"] = False
        products = Product.get_products_by_id(ids)        
        if len(ids) <= 0:
            cart_empty["flag"] = True
            return render(request, "cart.html", {"products": products, "cart_empty": cart_empty})
        return render(request, 'cart.html', {'products': products})
