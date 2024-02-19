#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests

response = requests.get(
    'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')

print(response.content)
