from django.urls import path

from account.views import Managerlogin, managerlogout
from .views import *

urlpatterns = [
    path('', dashboard, name='SupDash'),

    path('login/', Managerlogin, name='Suplogin'),
    path('logout.', managerlogout, name='Suplogout'),

    path('products/', products, name='SupProducts'),
    path('singleproduct/<str:id>/', singleproduct, name='Supsingleproducts'),

    path('category/', category, name='Supcategory'),
    path('category/<str:id>/', categorycrud, name='Supcategorycrud'),

    path('subcategory/', subcategory, name='Supsubcategory'),
    path('subcategory/<str:id>/', subcategorycrud, name='Supsubcategorycrud'),

    path('sellers/', Sellers, name='Supseller'),
    path('sellers/<str:id>/', Sellerdetails, name='Supsellerdetails'),

    path('neworders/', neworders, name='Supneworder'),
    path('allorders/', allorders, name='Supallorder'),
    path('orderdetails/<str:id>/', orderdetails, name='Suporderdetails'),
    path('cnforder/<str:id>/', confirmorder, name='Supconforder'),
    path('rejorder/<str:id>/', rejectorder, name='Suprejorder'),

    path('processorders/', orderprocess, name='Supprocessorder'),
    path('delivered/<str:id>/', deliverorder, name='Supdelvierorder'),

]
