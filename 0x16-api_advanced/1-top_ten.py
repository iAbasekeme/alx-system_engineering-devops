#!/usr/bin/python3
'''A file that sends a request to the reddit API
'''
import requests


def top_ten(subreddit):
  '''A function that sends a request queries the reddit api and prints the
    title of the first ten hot posts
  '''
  url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
  header = {
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
  }
  response = requests.get(url, headers=header, allow_redirects=False)
  if response.status_code != 200:
    return None

  try:
    data = response.json()
    posts = data['data']['titles']
    for post in posts:
      print(post)
  except (KeyError, ValueError):
    return None
