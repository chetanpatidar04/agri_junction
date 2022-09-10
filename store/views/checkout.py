from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order

class Checkout(View):
    def post(self, request):       
        address = request.POST.get("address")
        phone = request.POST.get("mob_number")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id (list(cart.keys()))
        for product in products:
            order = Order(customer = Customer(id = customer),
            product = product,
            price=product.price,
            quantity=cart.get(str(product.id)),
            address=address,
            mob_number = phone)
            order.place_order()
        return redirect("cart")