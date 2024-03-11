#!/usr/bin/python3
"""
    Using reddit API too get first 10 hot posts
"""
import requests


def hot_ten(subreddit):
    """Getting first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    mydata = response.json().get("mydata").get("children")
    hotTen = "\n".join(post.get("mydata").get("title") for post in mydata)
