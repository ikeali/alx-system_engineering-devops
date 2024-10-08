#!/usr/bin/python3
"""
This function queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers on a given Reddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ikeali)"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
