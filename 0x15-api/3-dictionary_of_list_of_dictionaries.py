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

    res = requests.get(user_str)
    if res.status_code == 200:
        print(res)
        print(res.content)
