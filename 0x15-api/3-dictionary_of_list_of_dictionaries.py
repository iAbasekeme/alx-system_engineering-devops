#!/usr/bin/python3
""" A script that export all data in the JSON format.
"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = '{}/users'.format(url_str)
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}users/{}/todos'.format(url_str, user_id)
    file = '{}.json'.format(user_id)
    username = requests.get(user_str).json()

    res = requests.get(todos_str)
    tasks = []
    data = res.json()
    for dat in data:
        task_dict = {"task": dat['title'],
                     "completed": dat['completed'],
                     "username": username.get('username')}
        tasks.append(task_dict)
    print(tasks)
