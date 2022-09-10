from email.headerregistry import Address
from pydoc import describe
from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', "category", "description", "price"]


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', "last_name", "email",
                    "mob_number", "address", "city", "state", "pincode"]


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', "customer", "quantity", "price", "date"]


# Register models here to show in admin pannel
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
