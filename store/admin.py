from pydoc import describe
from django.contrib import admin
from .models import Product
from .models import Category

class AdminProduct(admin.ModelAdmin):
    list_display=['name',"category","description","price"]


class AdminCategory(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)

