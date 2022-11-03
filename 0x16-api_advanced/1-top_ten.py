#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Invalid subreddits may return a
    redirect to search results"""
    baseUrl = 'https://www.reddit.com/r/'
    url = baseUrl + subreddit + "/hot.json"
    headers = {'user-agent': 'linux-cli hegel v1'}
    max_number = {'limit': '10'}
    response = requests.get(url,
                            headers=headers,
                            params=max_number,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        hot_list_of_dicts = response.json().get("data").get("children")
        titles = [reddit.get("data").get("title") for
                  reddit in hot_list_of_dicts]
        for title in titles:
            print(title)
