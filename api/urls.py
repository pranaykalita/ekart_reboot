from django.urls import path

from .views import *

urlpatterns = [

    #
    path('accounts/', AccountsList.as_view(), name='accountsAPI'),

    # GET /api/category/
    path('category/', CategoryList.as_view(), name='categorylistAPI'),

    # GET /api/products/
    path('products/', ProductList.as_view(), name='productslistAPI'),
    # GET /api/products/1/
    path('products/<int:id>/', ProductRetrive.as_view(), name='productsingleAPI'),

    # GET /api/cart/
    path('cart/', CartList.as_view(), name='cartlistAPI'),
    # GET /api/cart/cabcf175-95d5-417a-9ecb-c829af52f7ce/
    path('cart/<str:id>/', CartRetrive.as_view(), name='customercartAPI'),

]
