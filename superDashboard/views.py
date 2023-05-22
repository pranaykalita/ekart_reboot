from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request,'superDash/pages/products/index.html')

def category(request):
    return render(request,'superDash/pages/category/index.html')

def subcategory(request):
    return render(request,'superDash/pages/subcategory/index.html')

# def orders(request):
#     return render(request,'superDash/pages/orders/index.html')

