from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:id>/', CategoryDetail.as_view()),

    path('subcategory/', SubcategoryList.as_view()),
    path('subcategory/<int:id>/', SubcategoryDetail.as_view()),

    # path('products/', ProductList.as_view()),
    # path('products/<str:name>/', ProductData.as_view()),
    #
    # path('prod/', addproductDetails.as_view()),

    path('products/', ProductsList.as_view(),name='crudproduct'),
    path('products/<str:id>/', ProductDetail.as_view()),




    path('accounts/', AccountList.as_view()),
    path('account/<str:username>/', AccountList.as_view()),


    path('signupapi/', CreateAccountApi.as_view()),
    path('signupapi/<int:id>/', InsertAcoountDetail.as_view()),
]
