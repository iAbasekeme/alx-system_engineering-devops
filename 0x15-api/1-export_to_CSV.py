#!/usr/bin/python3
""" A script that export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}users/{}/todos'.format(url_str, user_id)
    file = '{}.csv'.format(user_id)

    res = requests.get(user_str)
    username = res.json().get('username')

    res = requests.get(todos_str)
    tasks = []
    if res.status_code == 200:
        data = res.json()
        for task in data:
            tasks.append([user_id, username, task['completed'], task['title']])

    with open(file, 'w') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"')
        for task in tasks:
            csv_writer.writerow(task)
