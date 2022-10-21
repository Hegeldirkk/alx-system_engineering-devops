#!/usr/bin/python3
"""Program: Alx Africa
Dev: Ikary Ryann
theme: API
Desc:Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress."""

import re
import requests
from sys import argv

"""Base Url of API Rest"""
BaseUrl = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            id = int(argv[1])
            user_res = requests.get('{}/users/{}'.format(BaseUrl, id)).json()
            todos_res = requests.get('{}/todos'.format(BaseUrl)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            with open('{}.csv'.format(id), 'w') as file:
                for todo in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            user_name,
                            todo.get('completed'),
                            todo.get('title')
                        )
                    )
