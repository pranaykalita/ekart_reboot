from django.urls import path

from .views import *
from account.views import *

urlpatterns = [
    path('', homepage, name='fhomepage'),
    path('createaccount/', customersignup, name='fsignup'),
    path('login/', customerlogin, name='fsignin'),
    path('logout/', custoemrlogout, name='flogout'),

    path('account/', dashboard, name='fdashboard'),
    path('editaccount/<str:id>/', editprofile, name='feditdashboard'),
    path('editpassword/<str:id>/', editpassword, name='feditpass'),

    path('orders/', dashboardorders, name='fdashboardorder'),
    path('orderdetails/<str:id>/', dashboardorderdetails, name='fdashboardorderdetails'),

    path('products/', products, name='fproductpage'),
    path('product/<str:id>/', singleproduct, name='fsingleproduct'),


    path('cart/', customercart, name='fcustomercart'),
    path('checkout/', checkout, name='fcustomercheckout'),
]
