
import requests

def showproducts(api_url):
    response = requests.get(api_url)
    products = response.json()
    return products

def showsingleproduct(api_url):
    response = requests.get(api_url)
    product = response.json()
    return product
