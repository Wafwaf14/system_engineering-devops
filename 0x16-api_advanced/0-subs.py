#!/usr/bin/python3
"""
    Uses Reddit API for printing number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Getting the number of subscriberst
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    subs = data.get("subscribers")

    return subs
