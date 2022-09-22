from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from django.forms.models import model_to_dict
from store.views.view_orders import View_order
# from store.models.orders import Order

class Profile(View):
    def __init__(self):
        self.cart_msg = False
        self.update_address = False
        self.my_orders = False
        self.orders=[]

    def post(self, request):
        profile_information = "False"        
        profile_information = request.POST.get("profile_information")
        self.my_orders = request.POST.get("my_orders")
        if profile_information:
            customer = model_to_dict(Customer.get_customer_by_id(request.session.get("customer")))
            fullname = customer.get("first_name") + " "+ customer.get("last_name")
        if self.my_orders == "True":
            self.orders = View_order.get(self,request)
        return Profile.get(self, request)

    def get(self, request):
        customer = model_to_dict(Customer.get_customer_by_id(request.session.get("customer")))
        fullname = customer.get("first_name") + " "+ customer.get("last_name")
        if self.my_orders:
            return render(request, 'profile.html', {"my_orders":self.my_orders,"orders":self.orders,"fullname":fullname})
        return render(request, 'profile.html', {"fullname":fullname})
