from django.urls import path

from .views import *
from account.views import sellerLogin,sellerregister,sellerlogout

urlpatterns = [
    path('login/',sellerLogin,name='sellerlogin'),
    path('register/', sellerregister,name='sellerregister'),
    path('slogout/', sellerlogout,name='sellerlogout'),

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
    path('allorders/', allorders, name='allorders'),
    path('order/<str:id>/', orderdetails, name='orderdetails'),

    path('approveorder/<str:id>/', orderapprove, name='ordapprove'),
    path('rejectorder/<str:id>/', orderreject, name='ordreject'),


]
