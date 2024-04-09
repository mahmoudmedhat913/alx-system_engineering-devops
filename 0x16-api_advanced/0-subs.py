#!/usr/bin/python3
"""module for number_of_subscribers"""


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""
    import requests
    if subreddit is None or type(subreddit) is not str:
        return 0

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    r = request.get(base_url, headers=headers, allow_redirects=False)

    if r.status_code >= 300:
        return 0
    
     return r.json().get('data').get('subscribers')
