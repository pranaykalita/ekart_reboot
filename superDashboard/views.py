import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.models import Order, orderapprovals


# Create your views here.

@login_required(login_url='Suplogin')
def dashboard(request):
    return render(request, 'superDash/pages/home/index.html')


@login_required(login_url='Suplogin')
def products(request):
    return render(request, 'superDash/pages/products/index.html')


@login_required(login_url='Suplogin')
def category(request):
    return render(request, 'superDash/pages/category/index.html')


@login_required(login_url='Suplogin')
def subcategory(request):
    return render(request, 'superDash/pages/subcategory/index.html')


@login_required(login_url='Suplogin')
def neworders(request):
    url = "http://127.0.0.1:8000/api/allorders/"
    response = requests.get(url)
    allorder = response.json()
    context = {'allorders': allorder}
    return render(request, 'superDash/pages/orders/index.html', context)


@login_required(login_url='Suplogin')
def allorders(request):
    url = "http://127.0.0.1:8000/api/allorders/"
    response = requests.get(url)
    allorder = response.json()
    context = {'allorders': allorder}
    return render(request, 'superDash/pages/allorders/index.html', context)


@login_required(login_url='Suplogin')
def orderdetails(request, id):
    url = "http://127.0.0.1:8000/api/orderdetails/"f"{id}"
    print(url)
    response = requests.get(url)
    order = response.json()
    context = {'orderdata': order}
    return render(request, 'superDash/pages/orderDetails/index.html', context)

@login_required(login_url='Suplogin')
def confirmorder(request, id):
    #set order status
    orderdata = Order.objects.get(id=id)
    orderdata.orderstatus = "approved"
    orderdata.save()
    # set customer model
    approvals = orderapprovals.objects.get(order=id,seller=orderdata.customer)
    approvals.approval = "approved"
    approvals.save()

    return redirect('Supallorder')

@login_required(login_url='Suplogin')
def rejectorder(request, id):
    #set order status
    orderdata = Order.objects.get(id=id)
    orderdata.orderstatus = "cancelled"
    orderdata.save()
    # set customer model
    approvals = orderapprovals.objects.get(order=id,seller=orderdata.customer)
    approvals.approval = "rejected"
    approvals.save()

    return redirect('Supallorder')