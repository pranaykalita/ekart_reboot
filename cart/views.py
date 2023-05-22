import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *


def ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required(login_url='fsignin')
def customercart(request):
    userid = request.session.get('customerID')
    user = request.user
    # create uuid cart if not present
    createcart = Cart.objects.get_or_create(customer=user)

    cartid = Cart.objects.filter(customer=userid).first()

    addr = ip(request)
    url = f"http://{addr}:8000/api/cart/{cartid}/{userid}"
    print(url)

    resp = requests.get(url)
    items = resp.json()

    context = {'cartitems': items}
    return render(request, 'frontend/pages/cart/index.html', context)


@login_required(login_url='fsignin')
def AddtoCart(request, product):
    userid = request.session.get('customerID')
    cartid = Cart.objects.filter(customer=userid).first()

    if request.method == 'POST':
        productid = product
        product = Product.objects.get(id=productid)
        quantity = int(request.POST.get('qtybtn', 1))
        cart_item = CartItem.objects.filter(cart=cartid, product=product).first()
        # increase product if availabe
        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            CartItem(cart=cartid, product=product, quantity=quantity).save()

    return redirect('fcustomercart')

def deltecart(request):
    userid = request.session.get('customerID')
    cartuuid = Cart.objects.filter(customer=userid).first()
    cartuuid.delete()
    return redirect('fcustomercart')

# clear item from cart
def removecartItem(request, itemID):
    itemid = itemID
    CartItem.objects.filter(product=itemid).delete()
    return redirect('fcustomercart')


