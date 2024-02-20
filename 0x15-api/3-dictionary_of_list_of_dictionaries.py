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

    res = requests.get(user_str).json()
    for res in users:
        print(users)

    res_todos = requests.get(todos_str)
    data = res_todos.json()
    print(data)
