from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from django.views import View


class Index(View):
    def post(self, request):
        print("home_post_request")
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")        
        if cart:
            quantity = cart.get(product)
            if quantity:                
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session["cart"] = cart
        return redirect("homepage")

    def get(self, request):
        print("home_get_request")
        cart = request.session.get("cart")
        data = {}
        if not cart:
            request.session["cart"] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        data["product_flag"] = True
        if categoryID:
            products = Product.get_all_products_by_category_id(categoryID)            
            if not products :
                data["product_flag"] = False
        else:
            products = Product.get_all_products()        
        data["products"] = products
        data["categories"] = categories
        return render(request, 'index.html', {"data": data})
