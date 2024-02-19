#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from sys import argv
import requests

response = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
if response.status_code == 200:
    data = response.json()
print('Employee {} is done with tasks'.format(data['name']))

todos_res = requests.get(
    f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
if response.status_code == 200:
    data = todos_res.json()
    count = 0
    for dat in data:
        if dat['completed'] == True:
            count += 1
    print('({}/'.format(count))

total_res = requests.get(f'https://jsonplaceholder.typicode.com/users/2/todos')
if response.status_code == 200:
    data = total_res.json()
    count2 = 0
    for dat in data:
        count2 +=1
    print(count2)
print('Employee {} is done with tasks ({}/{}'.format(data['name'], count, count2))
