from django.shortcuts import render, redirect
from ..models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email_or_number = request.POST.get("email")
        password = request.POST.get("password")
        error_message = None
        try:
            customer = Customer.get_customer_by_email(email_or_number)
        except Customer.DoesNotExist:
            customer = False
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.id
                request.session["customer_email"] = customer.email
                return redirect("homepage")
            else:
                print("else")
                if email_or_number.isnumeric():
                    error_message = "Phone number or password invalid !!"
                else:
                    error_message = "Email or password invalid !!"
        else:
            error_message = "Email or password invalid !!"
        return render(request, "login.html", {"error": error_message})

def logout(request):
    request.session.clear()
    return redirect("login")
