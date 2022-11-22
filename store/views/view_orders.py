from django.views import View
from store.models.orders import Order
from django.shortcuts import render, redirect


class View_order(View):
    def get(self, request):
        print(request.session.get("customer_firstname"))
        print(request.session.get("customer_lastname"))
        customer = request.session.get("customer")
        my_orders = Order.get_orders_by_customer(customer)
        my_orders = my_orders[::-1]
        # return orders
        orders = True
        return render(request,'profile.html', {"orders": orders,"my_orders":my_orders})

# def orders(request):
#     if request.method == "GET":
#         orders = True
#         return render(request, 'profile.html', {"orders": orders})
#     elif request.method == "POST":
#         print("sadnkdbhsabdhajvbsadvjsdvjh")
#         orders = True
#         my_orders = View_order().get(request)
#         print(" my_orders",my_orders)
#         return render(request,'profile.html', {"orders": orders,"my_orders":my_orders})