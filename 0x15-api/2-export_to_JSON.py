#!/usr/bin/python3
""" A script that export data in the json format.
"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}users/{}/todos'.format(url_str, user_id)
    file = '{}.json'.format(user_id)
    username = requests.get(user_str).json()
    # print(username['username'])

    res = requests.get(todos_str)
    tasks = []
    data = res.json()
    print(data)
    for dat in data:
        task_dict = {"task": dat['title'],
                     "completed": dat['completed'], "username": username.get('username')}
        tasks.append(task_dict)
    print(tasks)
