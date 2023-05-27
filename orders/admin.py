from django.contrib import admin

from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'subtotal','orderno']

admin.site.register(Order, OrderAdmin)

class OrderaddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'city','country']

admin.site.register(Orderaddress, OrderaddressAdmin)


class orderapprovalsAdmin(admin.ModelAdmin):
    list_display = ['order', 'seller', 'approval']

admin.site.register(orderapprovals, orderapprovalsAdmin)