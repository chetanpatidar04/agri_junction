from django.shortcuts import render
from django.views import View
from store.models.product import Product
from store.models.customer import Customer
from django.forms.models import model_to_dict

class Cart(View):
    def __init__(self):
        self.cart_msg = False
        self.update_address = False

    def post(self, request):
        product_id = request.POST.get("product_id")
        prod_id = request.POST.get("prod_id")
        reduce = request.POST.get("reduce")
        cart = request.session.get("cart")
        update_address = request.POST.get("update_address",False)
        if update_address == "True":
            request.session["address"] = request.POST.get("address","") 
            request.session["mob_number"] = request.POST.get("mob_number","")
            request.session["pincode"] = request.POST.get("pin_code","")
            print(request.session["address"],request.session["mob_number"],request.session["pincode"],"my adress")
            self.update_address = True
            return Cart.get(self, request)    
        quantity = cart.get(prod_id)
        if quantity:
            if reduce:
                if quantity <= 1:
                    self.cart_msg = True
                    request.session["cart_msg"] = "Product removed successfully"
                    cart.pop(prod_id)
                else:
                    cart[prod_id] = quantity - 1
            else:
                cart[prod_id] = quantity + 1
        if product_id in list(cart.keys()):
            self.cart_msg = True
            request.session["cart_msg"] = "Product removed successfully"
            del cart[product_id]
        request.session["cart"] = cart
        return Cart.get(self, request)

    def get(self, request):
        if not self.update_address:
            customer = model_to_dict(Customer.get_customer_by_id(request.session.get("customer")))
            request.session["address"] = customer.get("address","") + " " + customer.get("city","") + " " + customer.get("state","")
            request.session["mob_number"] = customer.get("mob_number")
            request.session["pincode"] = customer.get("pincode")
            request.session["msg"] = {}            
        if not self.cart_msg:
            request.session["cart_msg"] = {}
        ids = list(request.session.get('cart').keys())
        cart_empty = {}
        cart_empty["flag"] = False
        products = Product.get_products_by_id(ids)
        if len(ids) <= 0:
            cart_empty["flag"] = True
            return render(request, "cart.html", {"products": products, "cart_empty": cart_empty})
        return render(request, 'cart.html', {'products': products})
