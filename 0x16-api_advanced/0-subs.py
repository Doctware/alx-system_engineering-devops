#!/usr/bin/python3
""" this module fetches api from suraddit """
import requests


def number_of_subscribers(subreddit):
    """ this function returns number of subscriber base give args """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "test"}

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
