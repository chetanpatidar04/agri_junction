from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order

class Checkout(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("mob_number")
        order_page_flag = request.POST.get("order_page_flag",False)
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_products_by_id (list(cart.keys()))
        for product in products:
            order = Order(customer=Customer(id=customer),
                            product = product,
                            price=product.price,
                            quantity=cart.get(str(product.id)),
                            address=address,
                            mob_number = phone)
            order.place_order()
        request.session["cart"]={}
        if order_page_flag:
            return redirect("view_order")
        return redirect("cart")