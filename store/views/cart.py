from django.shortcuts import render
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        cart_empty={}
        cart_empty["flag"] = False
        products = Product.get_products_by_id(ids)
        if len(ids)<= 0:
            cart_empty["flag"] = True
            return render(request,"cart.html",{"products":products,"cart_empty":cart_empty})            
        return render(request, 'cart.html', {'products': products})
