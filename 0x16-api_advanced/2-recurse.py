#!/usr/bin/python3
"""
    Using Reddit API to get hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Getting all hot posts"""
    if after is None:
        return []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    r_json = response.json()
    top_posts_json = r_json.get("data").get("children")

    for postt in top_posts_json:
        hot_list.append(postt.get("data").get("title"))

    return hot_list + recurse(subreddit, [], r_json.get("data").get("after"))
