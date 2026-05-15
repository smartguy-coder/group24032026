import requests
from pprint import pprint

url = 'https://dummyjson.com/products'
# url = 'https://www.ukr.net/'
params = {
    'limit': 0,
    'skip': 0
}

response = requests.get(url=url, params=params)
# print(response.content)
# print(response.text)
response_json = response.json()

products = response_json["products"]

total_cost = 0

big_discount_percentage = 15
total_cost_products_big_discount = 0

tag = "badminton"
total_cost_by_tag = 0

for product in products:
    product_cost = product['price'] * product['stock']
    total_cost += product_cost

    if product['discountPercentage'] >= big_discount_percentage:
        total_cost_products_big_discount += product_cost

    if tag in product['tags']:
        total_cost_by_tag += product_cost

total_cost = round(total_cost, 2)
total_cost_products_big_discount = round(total_cost_products_big_discount, 2)

print(total_cost)
print(total_cost_products_big_discount)