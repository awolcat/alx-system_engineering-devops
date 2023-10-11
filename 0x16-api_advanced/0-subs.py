#!/usr/bin/python3
"""Module defines a single function"""
import requests


def number_of_subscribers(subreddit):
    """This function will send a request
        to the reddit api.
        params:
            subreddit: string identifying a subreddit
        return:
            number of subs
    """
    uri = f'https://www.reddit.com/r/{subreddit}/about.json'
    custom = {'User-Agent': 'My Agent'}
    response = requests.get(uri, headers=custom, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        subs = data.get('subscribers')
        return subs
    return 0
