#!/usr/bin/python3
'''A file that sends a request to the reddit Api
'''
import requests


def number_of_subscribers(subreddit):
    '''A function that makes a request and returns subscribers
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        print(0)
        return
    try:
        data = response.json()
        print('This is the {}'.format(data))
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, ValueError):
        print(0)
        return
