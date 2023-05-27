from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render, redirect

from account.models import CustomerUser
from cart.models import Cart
from cart.views import ip
from orders.models import *

# Create your views here.

@login_required(login_url='fsignin')
def checkout(request):
    customerid = request.session.get('customerID')
    customerac = CustomerUser.objects.get(id=customerid)
    cartid = Cart.objects.filter(customer=customerid).first()

    addr = ip(request)
    url = f"http://{addr}:8000/api/cart/{cartid}/{customerid}"

    resp = requests.get(url)
    cart = resp.json()
    context = {'items': cart}

    items = cart["items"]
    subtotal = cart["Subtotal"]

    if request.method == "POST":
        firstname = request.POST.get("billing-fname")
        lastname = request.POST.get("billing-lname")
        email = request.POST.get("billing-email")
        phone = request.POST.get("billing-phone")
        address1 = request.POST.get("billing-street")
        address2 = request.POST.get("billing-street-optional")
        country = request.POST.get("billing-country")
        city = request.POST.get("billing-town-city")
        state = request.POST.get("billing-state")
        postal = request.POST.get("billing-zip")
        note = request.POST.get("order-note")
        payment = request.POST.get("cash-on-delivery")

        order = Order(
            customer=customerac,
            items=items,
            subtotal=subtotal,
            payment=payment
        )
        order.save()

        # Create the seller approval instance
        seller_approval = orderapprovals(
            order=order,
            seller=customerac,
            approval='pending',  # Set the initial approval status as pending
            note=''  # Provide an empty note or modify it based on your requirements
        )
        seller_approval.save()

        # Get a set of unique sellers from the items (excluding customer's account)
        sellers = set()
        for item in items:
            product = item["product"]
            item_seller = product["seller"]

            # Exclude the customer's account (seller) and check if the seller is a seller account
            if item_seller != customerac.username and CustomerUser.objects.filter(username=item_seller, is_seller=True).exists():
                sellers.add(item_seller)

        # Iterate over the unique sellers and store seller approval
        for seller_username in sellers:
            # Find the seller account for the seller's username
            seller_account = CustomerUser.objects.get(username=seller_username)
            if seller_account:
                item_approval = orderapprovals(
                    order=order,
                    seller=seller_account,
                    approval='pending',  # Set the initial approval status as pending
                    note=''  # Provide an empty note or modify it based on your requirements
                )
                item_approval.save()

        orderID = order.id
        orderitem = Order.objects.get(id=orderID)

        orderaddress = Orderaddress(
            order=orderitem,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            email=email,

            address1=address1,
            address2=address2,
            country=country,
            city=city,
            state=state,
            postal=postal,

            note=note
        )
        orderaddress.save()
        cartid.delete()


        return redirect('fdashboardorder')

    return render(request, 'frontend/pages/checkout/index.html', context)
