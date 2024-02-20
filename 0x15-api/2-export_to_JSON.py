#!/usr/bin/python3
""" A script that export data in the json format.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}users/{}/todos'.format(url_str, user_id)
    file = '{}.json'.format(user_id)

    res = requests.get(user_str)
    data = res.json()
    print(data)

    res = requests.get(todos_str)
    data = res.json()
    print(data)
