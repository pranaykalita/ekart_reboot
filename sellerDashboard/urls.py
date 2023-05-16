from django.urls import path

from .views import *

urlpatterns = [

    path('dashboard/', dashboard, name='sellerdashboard'),
    path('products/', products, name='sellerproducts'),

    path('category/', category, name='sellercategory'),

    path('singleproduct/<str:id>/', singleproduct, name='sellersingleproducts'),
    path('deleteproj/<str:id>/', delteproduct, name='deleteproduct'),
    path('addproduct/', addproduct, name='addproduct'),

]
