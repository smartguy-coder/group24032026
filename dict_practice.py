import requests
from pprint import pprint

url = 'https://dummyjson.com/todos'
# url = 'https://www.ukr.net/'
params = {
    'limit': 0,
    'skip': 0
}

response = requests.get(url=url, params=params)
# print(response.content)
# print(response.text)
response_json = response.json()

todos = response_json['todos']
# pprint(todos)

uncompleted_todos = []
uncompleted_performance_todos = []
user_id_162_todos = []

for todo in todos:
    print(todo)
    if todo['userId'] == 162:
        user_id_162_todos.append(todo)

    if not todo['completed']:
        uncompleted_todos.append(todo['todo'])
        if 'performance' in todo['todo'].lower():
            uncompleted_performance_todos.append(todo['todo'])


# pprint(uncompleted_todos)
# uncompleted_todos_count = len(uncompleted_todos)
# print(uncompleted_todos_count)
# pprint(user_id_162_todos)
pprint(uncompleted_performance_todos)