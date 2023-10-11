#!/usr/bin/python3
"""Module defines a single function"""
import requests


def top_ten(subreddit):
    """This function will send a request
        to the reddit api.
        params:
            subreddit: string identifying a subreddit
        return:
            number of subs
    """
    uri = f'https://www.reddit.com/r/{subreddit}/hot.json'
    custom = {'User-Agent': 'My Agent'}
    param = {'limit': 10}
    response = requests.get(uri,
                            params=param,
                            headers=custom,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
