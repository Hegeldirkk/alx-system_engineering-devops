#!/usr/bin/python3
"""
0-subs function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""
    baseUrl = 'https://www.reddit.com/r/'
    url = baseUrl + subreddit + "/about.json"
    agent = {'User-Agent': "ikaryqnneje"}
    response = requests.get(url, headers=agent, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
