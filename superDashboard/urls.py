from django.urls import path

from .views import *

urlpatterns = [
    path('products/', products, name='SupProducts'),
    path('category/', category, name='Supcategory'),
    path('subcategory/', subcategory, name='Supsubcategory'),

]
