import requests


def get_category(api_url):
    response = requests.get(api_url)
    cat = response.json()
    return cat


def get_subcategory(api_url):
    response = requests.get(api_url)
    cat = response.json()
    return cat


def add_category(api_url, json_data):
    response = requests.put(api_url, data=json_data)
    if response.status_code == 201:
        return True
    else:
        return False


def add_subcategory(api_url, json_data):
    response = requests.put(api_url, data=json_data)
    if response.status_code == 201:
        print(response)
        return True
    else:
        print(response)
        return False


def delete_category(api_url):
    response = requests.delete(api_url)
    if response.status_code == 201:
        return True
    else:
        return False


def delete_subcategory(api_url):
    response = requests.delete(api_url)
    if response.status_code == 201:
        return True
    else:
        return False


def update_category(api_url, json_data):
    response = requests.patch(api_url, data=json_data)
    if response.status_code == 201:
        return True
    else:
        return False


def update_subcategory(api_url, json_data):
    response = requests.patch(api_url, data=json_data)
    if response.status_code == 201:
        return True
    else:
        return False


def get_subcategory(api_url):
    response = requests.get(api_url)
    subcategory = response.json()
    return subcategory


def get_products(api_url,seller_id):
    params = {'seller_id': seller_id}
    response = requests.get(api_url, params=params)
    products = response.json()
    print(products)
    return products


def single_products(api_url):
    response = requests.get(api_url)
    singleproduct = response.json()
    return singleproduct


def delete_product(api_url):
    response = requests.delete(api_url)
    if response.status_code == 201:
        return True
    else:
        return False


def add_product(api_url, data):
    response = requests.put(api_url, data=data, headers={'Content-Type': 'application/json'})
    if response.status_code == 201:
        return True
    else:
        return False

def get_orders(api_url):
    response = requests.get(api_url)
    orders = response.json()
    return orders

def get_order_detail(api_url):
    response = requests.get(api_url)
    order = response.json()
    return order