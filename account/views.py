from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import *
from frontend.views import allcategory
# Create your views here.
# seller Login:

def sellerLogin(request):
    if request.user.is_authenticated:
        return redirect('sellerdashboard')
    else:
        if request.method == 'POST':

            email = request.POST.get("emailaddress")
            password = request.POST.get("password")
            print(email,password)

            seller = authenticate(request,email=email,password=password)
            if seller is not None and seller.is_seller and seller.is_staff == True:
                login(request,seller)
                # store session
                request.session['sellerID'] = seller.id
                return redirect('sellerdashboard')
            else:
                return redirect('sellerlogin')
        return render(request,'sellerDash/pages/login_registration/login.html')

def sellerregister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('emailaddress')

        # Check if user already exists
        if CustomerUser.objects.filter(email=email).exists():
            print("exist alrady")
            return redirect('sellerlogin')

        CustomerUser.objects.create_seller(
            email=email,
            password=password,
            username=username,
            is_seller=True)

        return redirect('sellerlogin')
    return render(request, 'sellerDash/pages/login_registration/register.html')

def customersignup(request):
    if request.user.is_authenticated:
        return redirect('fhomepage')
    msg = ''
    if request.method == "POST":
        firstname = request.POST["reg-fname"]
        lastname = request.POST["reg-lname"]
        username = request.POST["reg-username"]
        email = request.POST["reg-email"]
        password = request.POST["reg-password"]
        print(firstname, lastname, username, email, password)
        customer = CustomerUser.objects.create_customer(
            email=email,
            password=password,
            username=username,
            firstname=firstname,
            lastname=lastname
        )
        if customer:
            success = True
            msg = 'Registration successful!'  # Add success message
    categories = allcategory()
    return render(request, 'frontend/pages/signup/index.html', {'success': msg, 'allcategory': categories})


def customerlogin(request):
    if request.user.is_authenticated:
        return redirect('fhomepage')
    else:
        if request.method == "POST":
            email = request.POST["login-email"]
            password = request.POST["login-password"]
            customer = authenticate(request, email=email, password=password)
            if customer is not None and customer.is_customer and customer.is_active == True:
                login(request, customer)
                request.session['customerID'] = customer.id
                request.session['customerUsername'] = customer.username
                return redirect('fhomepage')
            else:
                return redirect('fsignin')
    categories = allcategory()
    return render(request, 'frontend/pages/signin/index.html', {'allcategory': categories})


def custoemrlogout(request):
    logout(request)
    return redirect('fsignin')