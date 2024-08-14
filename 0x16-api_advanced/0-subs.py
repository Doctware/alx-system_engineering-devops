#!/usr/bin/python3
""" this module fetches api from suraddit """
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "subreddit-subscriber-counter"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            # Return 0 if the subreddit is not valid or if an error occurred
            return 0
    except requests.RequestException:
        # Handle any network-related errors
        return 0
