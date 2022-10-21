#!/usr/bin/python3
"""Program: Alx Africa
Dev: Ikary Ryann
theme: API
Desc:Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress. export json"""

import json
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
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open("{}.json".format(id), 'w') as json_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                    },
                    todos
                ))
                user_data = {
                    "{}".format(id): user_data
                }
                json.dump(user_data, json_file)
