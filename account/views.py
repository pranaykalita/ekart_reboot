from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from frontend.views import allcategory
from .models import *


# Create your views here.
# seller Login:

def Managerlogin(request):
    if request.user.is_authenticated:
        return redirect('SupDash')
    else:
        if request.method == 'POST':

            email = request.POST.get("emailaddress")
            password = request.POST.get("password")
            print(email, password)

            manager = authenticate(request, email=email, password=password)
            if manager is not None and manager.is_superuser == True and manager.is_seller == True:
                login(request, manager)

                # store session
                request.session['managerID'] = manager.id
                request.session['managerUsername'] = manager.username
                return redirect('SupDash')
            else:
                return redirect('SupDash')
        return render(request, 'superDash/pages/login_registration/login.html')

def ManagerRegister(request):
    if not request.user.is_superuser:
        return redirect('Suplogin')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('emailaddress')
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")

        # Check if user already exists
        if CustomerUser.objects.filter(email=email).exists():
            print("exist alrady")
            return redirect('sellerlogin')

        CustomerUser.objects.create_superuser(
            first_name = firstname,
            last_name = lastname,
            email=email,
            password=password,
            username=username,)

        return redirect('sellerlogin')
    return render(request, 'superDash/pages/login_registration/register.html')
def sellerLogin(request):
    if request.user.is_authenticated:
        return redirect('sellerdashboard')
    else:
        if request.method == 'POST':

            email = request.POST.get("emailaddress")
            password = request.POST.get("password")
            print(email, password)

            seller = authenticate(request, email=email, password=password)
            if seller is not None and seller.is_seller and seller.is_staff == True:
                login(request, seller)
                # store session
                request.session['sellerID'] = seller.id
                request.session['sellerUsername'] = seller.username
                return redirect('sellerdashboard')
            else:
                return redirect('sellerlogin')
        return render(request, 'sellerDash/pages/login_registration/login.html')



@login_required(login_url='Suplogin')
def sellerregister(request):
    if not request.user.is_superuser:
        return redirect('sellerlogin')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('emailaddress')
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")

        # Check if user already exists
        if CustomerUser.objects.filter(email=email).exists():
            print("exist alrady")
            return redirect('sellerlogin')

        CustomerUser.objects.create_seller(
            first_name= firstname,
            last_name = lastname,
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
                Cart.objects.get_or_create(customer=customer)
                return redirect('fhomepage')
            else:
                return redirect('fsignin')
    categories = allcategory()
    return render(request, 'frontend/pages/signin/index.html', {'allcategory': categories})


def custoemrlogout(request):
    logout(request)
    return redirect('fsignin')


def sellerlogout(request):
    logout(request)
    return redirect('sellerlogin')


def managerlogout(request):
    logout(request)
    return redirect('Suplogin')
