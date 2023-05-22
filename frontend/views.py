from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from account.models import CustomerUser,Customerdetail
# Create your views here.
from .apicall import *
from .apiurl import *


def allcategory():
    url = allcategoryurl
    response = requests.get(url)
    allcategory = response.json()
    return allcategory


def homepage(request):
    # trending
    url = productsurl
    products = showproducts(url)

    # featured products
    categories = allcategory()
    context = {'products': products,
               'allcategory': categories}

    return render(request, 'frontend/pages/homepage/index.html', context)


def products(request):
    filter_param = request.GET.get('filter')
    if filter_param is not None:
        url = productsurl + '?filter=' + filter_param
    else:
        url = productsurl

    products = showproducts(url)

    # featured products
    categories = allcategory()

    context = {'products': products,
               'allcategory': categories}

    return render(request, 'frontend/pages/products/index.html', context)


def singleproduct(request, id):
    url = productsurl + id + '/'
    product = showsingleproduct(url)
    categories = allcategory()
    context = {'product': product,
               'allcategory': categories}
    return render(request, 'frontend/pages/productdetails/index.html', context)


@login_required(login_url='fsignin')
def dashboard(request):
    customerID = request.session.get('customerID')
    customer = CustomerUser.objects.get(id=customerID)
    try:
        customer_detail = Customerdetail.objects.get(customeruser=customerID)
    except Customerdetail.DoesNotExist:
        customer_detail = "Null"
    context= {'customer': customer, 'customer_detail': customer_detail}
    return render(request,'frontend/pages/dashboard/index.html',context)

@login_required(login_url='fsignin')
def editprofile(request,id):
    customer = CustomerUser.objects.get(id=id)
    try:
        customer_detail = Customerdetail.objects.get(customeruser=id)
    except Customerdetail.DoesNotExist:
        customer_detail = "Null"
    # update
    if request.method == 'POST':
        fname = request.POST.get('reg-fname')
        lname = request.POST.get('reg-lname')
        phone = request.POST.get('reg-mobile')
        uname = request.POST.get('reg-uname')

        customer.firstname = fname
        customer.lastname = lname
        customer.username = uname

        customer.save()
        customer_detail.mobile = phone
        customer_detail.save()
        return redirect('fdashboard')

    context = {'customer': customer, 'customer_detail': customer_detail}
    return render(request, 'frontend/pages/dashboard/dasheditprofile/index.html', context)

@login_required(login_url='fsignin')
def editpassword(request,id):
    customer = CustomerUser.objects.get(id=id)
    try:
        customer_detail = Customerdetail.objects.get(customeruser=id)
    except Customerdetail.DoesNotExist:
        customer_detail = "Null"

    if request.method == 'POST':
        current_password  = request.POST.get('reg-cpass')
        new_password = request.POST.get('reg-newpass')

        if check_password(current_password, customer.password):

            # Update the user's password
            customer.set_password(new_password)
            customer.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('flogout')
        else:
            messages.error(request, 'Incorrect current password. Please try again.')

    context = {'customer': customer, 'customer_detail': customer_detail,}
    return render(request, 'frontend/pages/dashboard/dasheditpass/index.html', context)

@login_required(login_url='fsignin')
def dashboardorders(request):
    return render(request,'frontend/pages/dashboard/dashorders/index.html')

@login_required(login_url='fsignin')
def dashboardorderdetails(request,id):
    return  render(request,'frontend/pages/dashboard/dashorderdetails/index.html')

@login_required(login_url='fsignin')
def customercart(request):
    return render(request,'frontend/pages/cart/index.html')

@login_required(login_url='fsignin')
def checkout(request):
    return render(request,'frontend/pages/checkout/index.html')