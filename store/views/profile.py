# from sys import flags
from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from django.forms.models import model_to_dict
# from store.views.view_orders import View_order
from store.views.signup import Signup
from django.contrib.auth.hashers import check_password, make_password


class Profile(View):
    def __init__(self):
        self.cart_msg = False
        self.update_address = False
        self.my_orders = False
        self.orders = []
        self.customer = []

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get("first_name")
        last_name = post_data.get("last_name")
        email = post_data.get("email")
        mob_number = post_data.get("mob_number")
        address = post_data.get("address")
        city = post_data.get("city")
        state = post_data.get("state")
        if state is None:
            state = ""
        pincode = post_data.get("pincode")
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mob_number': mob_number,
            'email': email,
            'address': address,
            'city': city,
            'state': state,
            'pincode': pincode
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            mob_number=mob_number,
                            address=address,
                            city=city,
                            state=state,
                            pincode=pincode)
        error_message = validateCustomer_edit(customer)
        if not error_message:
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'profile.html', data)

    # def post(self, request):
    #     profile_information = "False"
    #     profile_information = request.POST.get("profile_information")
    #     self.my_orders = request.POST.get("my_orders")
    #     if profile_information:
    #         self.customer = model_to_dict(
    #             Customer.get_customer_by_id(request.session.get("customer")))
    #     if self.my_orders == "True":
    #         self.orders = View_order.get(self, request)
    #     return Profile.get(self, request)

    def get(self, request):
        if request.method == "GET":
            self.customer = model_to_dict(
                Customer.get_customer_by_id(request.session.get("customer")))
            return render(request, 'profile.html', {"customer": self.customer})


def profile_update(request):
    check_password = request.POST.get("check_password", "")
    if check_password:
        print("check_password", check_password)
    customer = Customer.get_customer_by_id(request.session.get("customer"))
    password = request.POST.get("password")
    customer_temp = {}
    first_name = request.POST.get("first_name", "")
    if first_name:
        customer.first_name = first_name
    last_name = request.POST.get("last_name", "")
    if last_name:
        customer.last_name = last_name
    address = request.POST.get("address", "")
    if address:
        customer.address = address
    state = request.POST.get("state")
    if state:
        customer.state = state
    pincode = request.POST.get("pincode", "")
    if pincode:
        customer.pincode = pincode
    city = request.POST.get("city")
    if city:
        customer.city = city
    customer.save()
    request.session["profile_update_msg"] = "Profile updated successfully"
    return redirect("profile")


def password_update(request):
    request.session["pass_update_msg"] = ""
    if request.method == "GET":
        update_password = True
        return render(request, 'profile.html', {"update_password": update_password})
    elif request.method == "POST":
        update_password = True
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        error_message = None
        if old_password and new_password and confirm_password:
            if old_password == new_password:
                error_message = "old password and new password should not be same"
            elif new_password != confirm_password:
                error_message = "new password and confirm password should be same"

        if error_message is None:
            customer_email = request.session["customer_email"]
            customer = Customer.get_customer_by_email(customer_email)
            flag = check_password(old_password, customer.password)
            if flag:
                customer.password = make_password(confirm_password)
                customer.save()
                request.session["pass_update_msg"] = "Password updated successfuly"
            else:
                error_message = "Invalid Old Password"
    return render(request, 'profile.html', {"update_password": update_password, "error": error_message})


def validateCustomer_edit(customer):
    error_message = None
    if (not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.mob_number:
        error_message = 'Mobile Number Required'
    elif len(customer.mob_number) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExists_email():
        error_message = 'Email Address Already Registered..'
    elif customer.isExists_mob_number():
        error_message = 'Mobile Number Already Registered..'
    return error_message
