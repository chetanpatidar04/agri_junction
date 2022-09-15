from django.shortcuts import render
from django.views import View
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class View_order(View):    
    def get(self, request):
        customer = request.session.get("customer")
        orders = Order.get_orders_by_customer(customer)
        orders = orders[::-1]
        return render(request, "orders.html", {"orders": orders})