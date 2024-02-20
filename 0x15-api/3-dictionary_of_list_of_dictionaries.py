#!/usr/bin/python3
""" A script that export all data in the JSON format.
"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users'.format(url_str)
    todos_str = '{}/todos'.format(url_str)
    first_dict = {}

    res = requests.get(user_str).json()
    res_todos = requests.get(todos_str).json()
    for users in res:
        tasks_list = []
        for todos in res_todos:
            if users['id'] == todos['userId']:
                task_dict = {"username": users['username'],
                             "task": todos['title'],
                             "completed": todos['completed']}
                tasks_list.append(task_dict)
        first_dict[users['id']] = tasks_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(first_dict, file)
