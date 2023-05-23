from django.urls import path

from .views import *
from account.views import sellerLogin,sellerregister

urlpatterns = [
    path('login/',sellerLogin,name='sellerlogin'),
    path('register/', sellerregister,name='sellerregister'),

    path('dashboard/', dashboard, name='sellerdashboard'),
    path('products/', products, name='sellerproducts'),

    path('category/', category, name='sellercategory'),
    path('category/<str:id>/', categoryCrud, name='categorycrud'),

    path('subcategory/', subcategory, name='sellersubcategory'),
    path('subcategory/<str:id>/', subcategoryCrud, name='subCategorycrud'),

    path('singleproduct/<str:id>/', singleproduct, name='sellersingleproducts'),
    path('deleteprod/<str:id>/', delteproduct, name='deleteproduct'),
    path('addproduct/', addproduct, name='addproduct'),
    path('editproduct/<str:id>/', editproduct, name='editproduct'),


    path('orders/', orderbyseller, name='orders'),


]
