from datetime import datetime
import csv
import requests

file = open('my_info.txt',  encoding='utf-8')

file_content = file.read()

print(file_content)
print("--------------------")
file.seek(5)
file_content2 = file.read()

print(file_content2)
# 1/0

file.close()

file.seek(1)
file_content2 = file.read()

print(file_content2)


# CORRECT WAY
# -READ- OPEN TEXT FILES
# with open('files_theory.py', mode='r', encoding='utf-8') as file:
#     # 1 all content
#     content = file.read()
#     print(content)
#
#     # 2 all rows as list of strings
#     # lines = file.readlines()
#     # print(lines)
#     # for line in lines:
#     #     print(line, end='')

# WRITE FILES
# with open('new_txt_file.txt', mode='w', encoding='utf-8') as file:
with open('new_txt_file.txt', mode='a', encoding='utf-8') as file:
    file.write('11111\n11111111\n')
    file.write('222222222222222\n')
    file.write('33333333333333\n')

# CSV files
with open('logs.csv', mode='a', encoding='utf-8') as file:
    file.write(f'{datetime.now()};Василь;Bush;56565\n')

# with open('logs.csv', mode='r', encoding='utf-8') as file:
#     # 1
#     # lines = file.readlines()
#     # for line in lines:
#     #     print(line, end='')
#     #     elements = line.split(';')
#     #     print(elements, elements[1])
#
#     # 2
#     reader = csv.DictReader(file, delimiter=';', fieldnames=['time2', 'bla-bla', 'ggg', 'dkfgh'])
#     for row in reader:
#         print(row, row['time2'])


# BINARY FILES
# url = 'https://49.zdo.zhitomir.ua/wp-content/uploads/2023/04/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg'
#
# response = requests.get(url)
# print(response.content)
# with open('spring.jpeg', mode='bw') as file:
#     file.write(response.content)

# with open('spring.jpeg', mode='br') as file:
#     content = file.read()
#     print(content)

# with open('spring.jpeg', mode='ba') as file:
#     file.write(b'   Vasyl - hello there')


# JSON
import json
from pprint import pprint

# dict -> json
user_info = {
    'name': 'Alex',
    'age': 15,
    'city': 'Одеса',
    'hobbies': [
        'tennis',
        'swimming'
    ],
    'additional_data': None,
    "is_married": False,
}
pprint(user_info)

user_data_as_json_string = json.dumps(user_info, ensure_ascii=False)
pprint(user_data_as_json_string)

# json -> dict

user_data_from_json = json.loads(user_data_as_json_string)
pprint(user_data_from_json)

# dict -> file.json
# with open('user_data.json', mode='w', encoding='utf-8') as json_file:
#     json.dump(user_info, json_file, indent=4, ensure_ascii=False)

# file.json -> dict
with open('user_data.json', mode='r', encoding='utf-8') as json_file:
    user_data_from_file = json.load(json_file)
    print(user_data_from_file)
