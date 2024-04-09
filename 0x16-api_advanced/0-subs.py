#!/usr/bin/python3
"""module for number_of_subscribers"""
from requests import get


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    r = requests.get(base_url, headers=headers, allow_redirects=False).json()

    try:
        return r.get('data').get('subscribers')
    except Exception:
        return 0
