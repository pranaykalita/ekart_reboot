from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.models import *
from products.models import *
from .api_urls import *
from .apicall import *


# Create your views here.

@login_required(login_url='sellerlogin')
def dashboard(request):
    return render(request, 'sellerDash/pages/home/index.html')


@login_required(login_url='sellerlogin')
def category(request):
    api_url = category_url
    category = get_category(api_url)

    if request.method == 'POST':
        name = request.POST['catname']

        data = {'name': name}

        api_url = categorycrud_url
        add_category(api_url, data)
        return redirect('sellercategory')

    context = {
        'category': category
    }
    return render(request, 'sellerDash/pages/category/index.html', context)


@login_required(login_url='sellerlogin')
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
        return redirect('sellersubcategory')

    context = {
        'category': category,
        'subcategory': subcategory
    }
    return render(request, 'sellerDash/pages/subcategory/index.html', context)


@login_required(login_url='sellerlogin')
def categoryCrud(request, id):
    api_url = categorycrud_url + id + '/'

    if request.method == 'POST':
        name = request.POST['upcatname']
        data = {'name': name, }
        update_category(api_url, data)

    else:
        delete_category(api_url)

    return redirect('sellercategory')


@login_required(login_url='sellerlogin')
def subcategoryCrud(request, id):
    api_url = subcategorycrud_url + id + '/'

    if request.method == 'POST':
        name = request.POST['upsubcatname']
        data = {'name': name, }
        update_subcategory(api_url, data)

    else:
        delete_subcategory(api_url)

    return redirect('sellersubcategory')


# product Display
@login_required(login_url='sellerlogin')
def products(request):
    api_url = product_crud_url
    seller_id = request.session.get('sellerID')
    products = get_products(api_url, seller_id)

    context = {'products': products}
    return render(request, 'sellerDash/pages/products/index.html', context)


@login_required(login_url='sellerlogin')
def singleproduct(request, id):
    api_url = product_url + id
    singleproduct = single_products(api_url)

    context = {
        'viewproduct': singleproduct,
    }
    return render(request, 'sellerDash/pages/productdetails/index.html', context)


@login_required(login_url='sellerlogin')
def delteproduct(request, id):
    api_url = product_crud_url + id
    del_product = delete_product(api_url)
    if del_product:
        return redirect('sellerproducts')
    else:
        print('Failed to delete')
    return redirect('sellerproducts')


@login_required(login_url='sellerlogin')
def addproduct(request):
    api_caturl = category_url
    api_subcaturl = subcategory_url
    category = get_category(api_caturl)
    subcategory = get_subcategory(api_subcaturl)

    if request.method == "POST":
        name = request.POST.get("productname")
        price = request.POST.get("productprice")
        quantity = request.POST.get("productqty")

        categoryID = request.POST.get("prodCategory")
        category = Category.objects.get(pk=categoryID)
        subcategoryID = request.POST.get("prodSubcategory")
        subcategory = Subcategory.objects.get(pk=subcategoryID)

        about = request.POST.get("productabout")
        description = request.POST.get("productdescription")
        size = request.POST.get("productsize")
        variant = request.POST.get("productvar")
        # sku = request.POST.get("productSKU")

        mainimg = request.FILES.get("mainimage")
        img1 = request.FILES.get("prodimg1")
        img2 = request.FILES.get("prodimg2")
        img3 = request.FILES.get("prodimg3")

        # seller details
        sellerID = request.session.get('sellerID')
        seller = CustomerUser.objects.get(id=sellerID)

        # insert to product
        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            category=category,
            subcategory=subcategory,
            mainimage=mainimg,
            seller=seller
        )
        product.save()
        product_id = product.id
        item = Product.objects.get(pk=product_id)

        details = Productdetails(
            product=item,
            about=about,
            description=description,
            size=size,
            variant=variant
        )
        details.save()

        if mainimg or img1 or img2 or img3:
            if img1:
                prodimg1 = Productimage(product=item, image=img1)
                prodimg1.save()
            if img2:
                prodimg2 = Productimage(product=item, image=img2)
                prodimg2.save()
            if img3:
                prodimg3 = Productimage(product=item, image=img3)
                prodimg3.save()

        return redirect('sellerproducts')

    context = {
        'category': category,
        'subcategory': subcategory
    }
    return render(request, 'sellerDash/pages/addproduct/index.html', context)


@login_required(login_url='sellerlogin')
def editproduct(request, id):
    if request.method == "POST":
        name = request.POST.get("productname")
        price = request.POST.get("productprice")
        quantity = request.POST.get("productqty")

        categoryID = request.POST.get("prodCategory")
        category = Category.objects.get(pk=categoryID)
        subcategoryID = request.POST.get("prodSubcategory")
        subcategory = Subcategory.objects.get(pk=subcategoryID)

        about = request.POST.get("productabout")
        description = request.POST.get("productdescription")
        size = request.POST.get("productsize")
        variant = request.POST.get("productvar")
        sku = request.POST.get("productSKU")

        mainimg = request.FILES.get("mainimage")
        img1 = request.FILES.get("prodimg1")
        img2 = request.FILES.get("prodimg2")
        img3 = request.FILES.get("prodimg3")

        product = Product.objects.get(id=id)
        productDetail = Productdetails.objects.get(product=id)
        productimages = Productimage.objects.all().filter(product=id)

        # if selected the uplaod the images
        if mainimg:
            product.mainimage = mainimg
            product.save()
        else:
            images = [img for img in [img1, img2, img3] if img]
            for image, productimage in zip(images, productimages):
                productimage.image = image
                productimage.save()

        product.name = name
        product.price = price
        product.quantity = quantity
        product.category = category
        product.subcategory = subcategory
        product.save()

        productDetail.about = about
        productDetail.description = description
        productDetail.size = size
        productDetail.variant = variant
        productDetail.SKU = sku
        productDetail.save()
        return redirect('sellersingleproducts', id=id)

    api_url = product_url + id
    productdata = single_products(api_url)

    api_caturl = category_url
    api_subcaturl = subcategory_url
    categorydata = get_category(api_caturl)
    subcategorydata = get_subcategory(api_subcaturl)

    context = {
        'singleproduct': productdata,
        'cat': categorydata,
        'subcat': subcategorydata
    }
    return render(request, 'sellerDash/pages/editproduct/index.html', context)


# ORders by seller
@login_required(login_url='sellerlogin')
def orderbyseller(request):
    sellername = request.session.get('sellerUsername')
    api_url = order_url + sellername
    order_data = get_orders(api_url)
    context = {'orders': order_data}
    print(api_url)
    return render(request, 'sellerDash/pages/orders/index.html', context)

@login_required(login_url='sellerlogin')
def allorders(request):
    sellername = request.session.get('sellerUsername')
    api_url = order_url + sellername
    order_data = get_orders(api_url)
    context = {'orders': order_data}
    print(api_url)
    print(context)
    return render(request, 'sellerDash/pages/allorders/index.html', context)


def orderdetails(request, id):
    sellername = request.session.get('sellerUsername')
    api_url = order_url + sellername + '/' + id
    order_detail = get_order_detail(api_url)
    context = {'order_detail': order_detail}
    return render(request, 'sellerDash/pages/orderDetails/index.html', context)


def orderapprove(request, id):
    seller = request.session.get('sellerID')
    sellerorder = orderapprovals.objects.get(order=id,seller=seller)

    status = 'approved'
    sellerorder.approval = status
    sellerorder.save()
    return redirect('orders')

def orderreject(request, id):
    seller = request.session.get('sellerID')
    sellerorder = orderapprovals.objects.get(order=id,seller=seller)
    status = 'rejected'

    sellerorder.approval = status
    sellerorder.save()
    return redirect('orders')
