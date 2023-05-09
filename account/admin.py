from django.contrib import admin

from .models import *


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']


admin.site.register(CustomerUser, CustomerUserAdmin)


class CustomerdetailAdmin(admin.ModelAdmin):
    list_display = ['customeruser', 'firstname', 'lastname', 'mobile']


admin.site.register(Customerdetail, CustomerdetailAdmin)
