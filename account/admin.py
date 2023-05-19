from django.contrib import admin
from .models import *


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'is_seller', 'is_customer')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_seller', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomerUser, CustomerUserAdmin)


class CustomerdetailAdmin(admin.ModelAdmin):
    list_display = ['customeruser', 'mobile']


admin.site.register(Customerdetail, CustomerdetailAdmin)
