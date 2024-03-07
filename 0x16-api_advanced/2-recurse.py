#!/usr/bin/python3
import requests
'''A file that makes a call to an api recursively
'''


def recurse(subreddit, hot_list=[], after=None):
    """A fucntion that makes a request to an api recursively
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
