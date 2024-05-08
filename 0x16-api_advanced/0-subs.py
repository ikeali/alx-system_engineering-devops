#!/usr/bin/python3
"""This module makes a request to the reddit api""":wq


import requests

def number_of_subscribers(subreddit):
    """
    Gets number of subscribers of a subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers.
    """
    if subreddit is None:
        return 0

    headers = {'User-Agent': 'YourBot/1.0'}  # Update User-Agent header
    
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()
        subreddit_data = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0

    if 'error' in subreddit_data:
        print(f"Error: {subreddit_data['error']}")
        return 0

    return subreddit_data['data']['subscribers']

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    print(f"Number of subscribers: {number_of_subscribers(subreddit_name)}")

