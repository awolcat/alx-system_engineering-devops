#!/usr/bin/python3
"""Module defines a single function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """This function will send a request
        to the reddit api.
        params:
            subreddit: string identifying a subreddit
        return:
            a list of hot articles
    """
    uri = f'https://www.reddit.com/r/{subreddit}/hot.json'
    custom = {'User-Agent': 'My Agent'}
    param = {'limit': 99, 'after': after}
    response = requests.get(uri,
                            params=param,
                            headers=custom,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        after = data['after']
        posts = data['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
