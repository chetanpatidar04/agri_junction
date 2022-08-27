from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render
from .models.product import Product
from .models.category import Category


def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    data = {}
    data["products"] = products
    data["categories"] =  categories
    # return render(request,'orders/orders.html')
    # print(data["categories"])

    return render(request,'index.html',{"data":data})
