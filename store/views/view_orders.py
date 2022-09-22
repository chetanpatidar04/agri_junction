from django.views import View
from store.models.orders import Order
# from django.shortcuts import render


class View_order(View):
    def get(self, request):
        customer = request.session.get("customer")
        orders = Order.get_orders_by_customer(customer)
        orders = orders[::-1]
        return orders
        # return render(request, "orders.html", {"orders": orders})
