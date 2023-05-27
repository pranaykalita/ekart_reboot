from django.urls import path

from .views import *

urlpatterns = [

    #
    path('accounts/', AccountsList.as_view(), name='accountsAPI'),

    # GET /api/category/
    path('combinecategory/', CategorySubList.as_view(), name='categorylistAPI'),
    path('category/', CategoryList.as_view(), name='categoryAPI'),
    path('subcategory/', SubcategoryList.as_view(), name='subcategoryAPI'),

    # GET /api/products/
    # 127.0.0.1:8000/api/products/?filter=Fashion
    path('products/', ProductList.as_view(), name='productslistAPI'),
    # GET /api/products/1/
    path('products/<int:id>/', ProductRetrive.as_view(), name='productsingleAPI'),

    # GET /api/cart/
    path('cart/', cartListView.as_view(), name='cartlist'),
    # GET /api/cart/cabcf175-95d5-417a-9ecb-c829af52f7ce/
    path('cart/<str:id>/<str:customer>/', cartRetriveView.as_view(), name='cartdatalist'),


    path('orders/<str:customer>/', orderlist.as_view(), name='orderapi'),
    path('orders/<str:customer>/<str:id>/', orderRetrive.as_view(), name='orderretrive'),

    path('allorders/', allorderView.as_view(), name='allorders'),
    path('orderdetails/<int:id>/', RetriveorderView.as_view(), name='orderdetails'),



]
