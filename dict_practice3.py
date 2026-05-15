import requests
from pprint import pprint

url = 'https://dummyjson.com/users'
# url = 'https://www.ukr.net/'
params = {
    'limit': 0,
    'skip': 0
}

response = requests.get(url=url, params=params)
# print(response.content)
# print(response.text)
response_json = response.json()

users = response_json["users"]
# pprint(users)


mississippi_users = []
female_up_to_30_greene_yes = []

for user in users:
    pprint(user)

    if user['address']['state'] == "Mississippi":
        mississippi_users.append(user)

    is_green_eyes = user["eyeColor"] == 'Green'
    is_female = user['gender'] == "female"
    is_age_below_30 = user['age'] < 30

    if is_green_eyes and is_female and is_age_below_30:
        female_up_to_30_greene_yes.append(user)


