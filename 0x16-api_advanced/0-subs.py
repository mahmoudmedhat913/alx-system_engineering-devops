#!/usr/bin/python3
"""module for number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""

    if subreddit is None or type(subreddit) is not str:
        return 0

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    r = request.get(base_url, headers=headers, allow_redirects=False).json()

    if r.get('data') is None:
        return 0
    
    return r.get('data').get('subscribers')
