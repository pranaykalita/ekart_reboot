from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import *

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
