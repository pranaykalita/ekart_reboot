from django.contrib import admin

from .models import *


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']


admin.site.register(Product, ProductAdmin)


class ProductdetailsAdmin(admin.ModelAdmin):
    list_display = ['product', 'SKU']


admin.site.register(Productdetails, ProductdetailsAdmin)


class productimageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


admin.site.register(Productimage, productimageAdmin)
