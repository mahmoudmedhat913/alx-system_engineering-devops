#!/usr/bin/python3
"""module for number_of_subscribers"""


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/[]/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
