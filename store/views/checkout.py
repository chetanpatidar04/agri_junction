from typing import OrderedDict
from django.shortcuts import redirect
from ..models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class Checkout(View):
    def post(self, request):        
        address = request.POST.get("address")
        phone = request.POST.get("mob_number")
        order_page_flag = request.POST.get("order_page_flag", False)
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order = Order(customer= Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          address = request.session.get("address","N/A"),
                          mob_number = request.session.get("mob_number","N/A"))
            order.place_order()
        request.session["cart"] = OrderedDict()
        if order_page_flag:
            return redirect("view_order")
        return redirect("cart")
