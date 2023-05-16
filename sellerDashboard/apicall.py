import requests

def get_catsubcat(api_url):
    response = requests.get(api_url)
    cat = response.json()
    return cat

def get_subcatsubcat(api_url):
    response = requests.get(api_url)
    subcategory = response.json()
    return subcategory

def get_products(api_url):
    response = requests.get(api_url)
    products = response.json()
    return products

def single_products(api_url):
    response = requests.get(api_url)
    singleproduct = response.json()
    return singleproduct

def delete_product(api_url):
    response = requests.delete(api_url)
    if response.status_code == 204:
        return True
    else:
        return False

def add_product(api_url,data):
    response = requests.put(api_url, json=data, headers={'Content-Type': 'application/json'})
    if response.status_code == 201:
        return True
    else:
        return False