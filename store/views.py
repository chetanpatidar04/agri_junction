from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render
from .models.product import Product
from .models.category import Category


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data["products"] = products
    data["categories"] = categories

    # return render(request,'orders/orders.html')
    # print(data["categories"])

    return render(request, 'index.html', {"data": data})


def signup(request):
    return render(request,"signup.html")
