#!/usr/bin/python3
"""Program: Alx Africa
Dev: Ikary Ryann
theme: API
Desc: script to export data 
in the JSON format."""

import json
import requests

"""Base Url of API Rest"""
BaseUrl = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(BaseUrl)).json()
    todos_res = requests.get('{}/todos'.format(BaseUrl)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
