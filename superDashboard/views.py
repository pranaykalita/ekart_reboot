from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.models import Order, orderapprovals
from .api_urls import *
from .apicall import *


# Create your views here.

@login_required(login_url='Suplogin')
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser and request.user.is_seller:
        return render(request, 'superDash/pages/home/index.html')
    else:
        return redirect('Suplogout')


@login_required(login_url='Suplogin')
def products(request):
    api_url = product_url
    products = get_products(api_url)

    context = {'products': products}
    return render(request, 'superDash/pages/products/index.html', context)


@login_required(login_url='sellerlogin')
def singleproduct(request, id):
    api_url = product_url + id
    singleproduct = single_products(api_url)

    context = {
        'viewproduct': singleproduct,
    }
    return render(request, 'superDash/pages/productdetails/index.html', context)


@login_required(login_url='Suplogin')
def category(request):
    api_url = category_url
    category = get_category(api_url)

    if request.method == 'POST':
        name = request.POST['catname']

        data = {'name': name}

        api_url = categorycrud_url
        add_category(api_url, data)
        return redirect('Supcategory')

    context = {
        'category': category
    }
    return render(request, 'superDash/pages/category/index.html', context)


@login_required(login_url='sellerlogin')
def categorycrud(request, id):
    api_url = categorycrud_url + id + '/'

    if request.method == 'POST':
        name = request.POST['upcatname']
        data = {'name': name, }
        update_category(api_url, data)

    else:
        delete_category(api_url)

    return redirect('Supcategory')


@login_required(login_url='Suplogin')
def subcategory(request):
    capi_url = category_url
    category = get_category(capi_url)

    sapi_url = subcategorycrud_url
    subcategory = get_subcategory(sapi_url)

    if request.method == 'POST':
        catname = request.POST['prodCategory']
        name = request.POST['subcatname']

        data = {
            'category': catname,
            'name': name, }
        print(data)

        api_url = subcategorycrud_url
        add_subcategory(api_url, data)
        return redirect('Supsubcategory')

    context = {
        'category': category,
        'subcategory': subcategory
    }
    return render(request, 'superDash/pages/subcategory/index.html', context)


@login_required(login_url='sellerlogin')
def subcategorycrud(request, id):
    api_url = subcategorycrud_url + id + '/'

    if request.method == 'POST':
        name = request.POST['upsubcatname']
        data = {'name': name, }
        update_subcategory(api_url, data)

    else:
        delete_subcategory(api_url)

    return redirect('Supsubcategory')


@login_required(login_url='Suplogin')
def Sellers(request):
    url = 'http://127.0.0.1:8000/api/accounts/'
    resp = requests.get(url)
    ac = resp.json()
    seller_accounts = [account for account in ac if account.get('is_seller', False) and not account.get('is_superuser', False)]

    # context = {'accounts': ac}
    context = {'accounts': seller_accounts}
    return render(request, 'superDash/pages/sellers/index.html', context)


@login_required(login_url='Suplogin')
def Sellerdetails(request, id):
    url = 'http://127.0.0.1:8000/api/accounts/'f'{id}/'
    resp = requests.get(url)
    ac = resp.json()
    seller = ac['username']
    data = ac['profileImage']
    url2 = 'http://127.0.0.1:8000/api/sellerproducts/'f'{seller}/'
    resp2 = requests.get(url2)
    products = resp2.json()
    context = {'accounts': ac, 'product': products, 'data': data}
    return render(request, 'superDash/pages/profile/index.html', context)


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
    # set order status
    orderdata = Order.objects.get(id=id)
    orderdata.orderstatus = "approved"
    orderdata.save()
    # set customer model
    approvals = orderapprovals.objects.get(order=id, seller=orderdata.customer)
    approvals.approval = "approved"
    approvals.save()

    return redirect('Supallorder')


@login_required(login_url='Suplogin')
def rejectorder(request, id):
    # set order status
    orderdata = Order.objects.get(id=id)
    orderdata.orderstatus = "cancelled"
    orderdata.save()
    # set customer model
    approvals = orderapprovals.objects.get(order=id, seller=orderdata.customer)
    approvals.approval = "rejected"
    approvals.save()

    return redirect('Supallorder')


@login_required(login_url='Suplogin')
def orderprocess(request):
    url = "http://127.0.0.1:8000/api/allorders/"
    response = requests.get(url)
    allorder = response.json()
    context = {'allorders': allorder}
    print(url)
    return render(request, 'superDash/pages/processorders/index.html', context)


@login_required(login_url='Suplogin')
def deliverorder(request, id):
    orderdata = Order.objects.get(id=id)
    orderdata.orderstatus = "delivered"
    orderdata.save()
    # set customer model
    approvals = orderapprovals.objects.get(order=id, seller=orderdata.customer)
    approvals.approval = "delivered"
    approvals.save()
    return redirect('Supallorder')
