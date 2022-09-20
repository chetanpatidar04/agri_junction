from statistics import median_high
from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def __init__(self):
        self.cart_msg = False

    def post(self, request):        
        product_id = request.POST.get("product_id")
        prod_id = request.POST.get("prod_id")
        reduce = request.POST.get("reduce")
        cart = request.session.get("cart")
        

        quantity = cart.get(prod_id)
        print("cart.py",quantity,reduce)
        print("cart_berfore",cart)
        if quantity:
            if reduce:
                if quantity <= 1:
                    self.cart_msg = True
                    request.session["cart_msg"] = "Product removed successfully"
                    cart.pop(prod_id)
                else:
                    cart[prod_id] = quantity - 1
            else:
                cart[prod_id] = quantity + 1

        print("cart",cart)


        if product_id in list(cart.keys()):
            self.cart_msg = True
            request.session["cart_msg"] = "Product removed successfully"
            del cart[product_id]            
        request.session["cart"] = cart
        return Cart.get(self, request)
    
    def get(self, request):
        print("cart",request.session.get('cart'))
        request.session["msg"] = {}
        if not self.cart_msg :
            request.session["cart_msg"] = {}
        ids = list(request.session.get('cart').keys())
        print("ids",ids)
        print("cart.py",request.session.get('cart'))
        cart_empty = {}
        cart_empty["flag"] = False
        products = Product.get_products_by_id(ids)
        for i in products:
            print("product.name",i)
        if len(ids) <= 0:
            cart_empty["flag"] = True
            return render(request, "cart.html", {"products": products, "cart_empty": cart_empty})
        return render(request, 'cart.html', {'products': products})