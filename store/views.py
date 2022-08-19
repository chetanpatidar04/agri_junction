from django.shortcuts import render
from .models.product import Product


def index(request):
    all_products = Product.get_all_products()
    return render(request,'index.html',{"products":all_products})
