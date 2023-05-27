from django.urls import path

from .views import *
from account.views import Managerlogin, managerlogout

urlpatterns = [
    path('', dashboard, name='SupDash'),

    path('login/', Managerlogin, name='Suplogin'),
    path('logout.', managerlogout, name='Suplogout'),

    path('products/', products, name='SupProducts'),
    path('category/', category, name='Supcategory'),
    path('subcategory/', subcategory, name='Supsubcategory'),

    path('neworders/', neworders, name='Supneworder'),
    path('allorders/', allorders, name='Supallorder'),
    path('orderdetails/<str:id>/', orderdetails, name='Suporderdetails'),
    path('cnforder/<str:id>/', confirmorder, name='Supconforder'),
    path('rejorder/<str:id>/', rejectorder, name='Suprejorder'),

]
