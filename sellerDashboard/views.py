import base64
import json

from django.shortcuts import render, redirect

from .api_urls import *
from .apicall import *


# Create your views here.

def dashboard(request):
    return render(request, 'sellerDash/pages/home/index.html')


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


def del_category(request, id):
    api_url = categorycrud_url + id
    del_category = delete_category(api_url)
    if del_category:
        return redirect('sellercategory')
    else:
        print('Failed to delete')
    return redirect('sellercategory')

def del_subcategory(request, id):
    api_url = subcategorycrud_url + id
    del_subcategory = delete_subcategory(api_url)

    if del_subcategory:
        return redirect('sellersubcategory')
    else:
        print('Failed to delete')
    return redirect('sellersubcategory')


def products(request):
    api_url = product_url
    products = get_products(api_url)

    context = {
        'products': products,
    }
    return render(request, 'sellerDash/pages/products/index.html', context)


def singleproduct(request, id):
    api_url = product_url + id
    singleproduct = single_products(api_url)

    context = {
        'viewproduct': singleproduct,
    }
    return render(request, 'sellerDash/pages/productdetails/index.html', context)


def delteproduct(request, id):
    api_url = product_crud_url + id
    del_product = delete_product(api_url)
    if del_product:
        return redirect('sellerproducts')
    else:
        print('Failed to delete')
    return redirect('sellerproducts')


def addproduct(request):
    api_caturl = category_url
    api_subcaturl = subcategory_url

    category = get_category(api_caturl)
    subcategory = get_subcategory(api_subcaturl)

    if request.method == "POST":
        name = request.POST.get("productname")
        price = request.POST.get("productprice")
        quantity = request.POST.get("productqty")
        category = request.POST.get("prodCategory")
        subcategory = request.POST.get("prodSubcategory")

        about = request.POST.get("productabout")
        description = request.POST.get("productdescription")
        size = request.POST.get("productsize")
        variant = request.POST.get("productvar")
        sku = request.POST.get("productSKU")

        mainimg = request.FILES.get("mainimage")
        img1 = request.FILES.get("prodimg1")
        img2 = request.FILES.get("prodimg2")
        img3 = request.FILES.get("prodimg3")

        # Convert images to base64-encoded strings
        mainimg_data = base64.b64encode(mainimg.read()).decode('utf-8')
        img1_data = base64.b64encode(img1.read()).decode('utf-8')
        img2_data = base64.b64encode(img2.read()).decode('utf-8')
        img3_data = base64.b64encode(img3.read()).decode('utf-8')

        jsondata = {
            "productdetail": {
                "about": about,
                "description": description,
                "size": size,
                "variant": variant,
                "SKU": sku,
            },
            "productimg": [
                {"image": img1_data},
                {"image": img2_data},
                {"image": img3_data},
            ],
            "name": name,
            "price": price,
            "quantity": quantity,
            "mainimage": mainimg_data,
            "category": category,
            "subcategory": subcategory,
        }

        json_data = json.dumps(jsondata)

        # save to database
        api_url = product_crud_url
        add_product(api_url, json_data)

        print(json_data)
        print("\n")
        print(api_url)
        return redirect('sellerproducts')

    context = {
        'category': category,
        'subcategory': subcategory
    }
    return render(request, 'sellerDash/pages/addproduct/index.html', context)
