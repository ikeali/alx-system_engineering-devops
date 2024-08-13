#!/usr/bin/python3
"""This module makes a request to the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers of a subreddit"""
    if subreddit is None:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        subreddit_data = res.json()
    except Exception:
        return 0

    if 'error' in subreddit_data.keys():
        return 0

    return subreddit_data['data']['subscribers']

