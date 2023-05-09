from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<str:name>/', CategoryDetail.as_view()),

    path('subcategory/', SubcategoryList.as_view()),
    path('subcategory/<str:name>/', SubcategoryDetail.as_view()),

    path('products/', ProductList.as_view()),
    path('products/<str:name>/', ProductDetail.as_view()),
]
