#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,\
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}users/{}/todos'.format(url_str, user_id)
    employee_str = 'Employee {} is done with tasks'

    response = requests.get(user_str)
    if response.status_code == 200:
        data = response.json()
    print(employee_str.format(data['name']), end="")

    todos_res = requests.get(todos_str)
    if response.status_code == 200:
        data = todos_res.json()
        count = 0
        for dat in data:
            if dat['completed'] is True:
                count += 1
        print('({}/'.format(count), end="")

    total_res = requests.get(todos_str)
    if response.status_code == 200:
        data = total_res.json()
        count2 = 0
        for dat in data:
            count2 += 1
        print('{})'.format(count2))

    for dat in data:
        if dat['completed'] is True:
            print('\t {}'.format(dat['title']))
