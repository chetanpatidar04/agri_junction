from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.views import View



class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get("first_name")
        last_name = post_data.get("last_name")
        email = post_data.get("email")
        password = post_data.get("password")
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
                            password=password,
                            mob_number=mob_number,
                            address=address,
                            city=city,
                            state=state,
                            pincode=pincode)
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
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
            error_message = 'Phone Number required'
        elif len(customer.mob_number) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists_email() and customer.isExists_mob_number():
            error_message = 'Email address and Mobile Number Already Registered..'
        elif customer.isExists_email():
            error_message = 'Email Address Already Registered..'
        elif customer.isExists_mob_number():
            error_message = 'Mobile Number Already Registered..'
        return error_message
