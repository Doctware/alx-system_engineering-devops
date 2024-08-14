#!/usr/bin/python3
""" the module return the hot titles reursivelt """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API
    and returns a list of titles of all hot articles."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "recursion-subreddit-posts/0.1"}
    params = {"limit": 100, "after": after}

    resp = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)

    if resp.status_code != 200:
        return None

    data = resp.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        return hot_list if hot_list else None

    # Append titles of current posts to the hot_list
    hot_list.extend([post.get("data", {}).get("title") for post in posts])

    # Recursively call the function if there's more data to fetch
    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    else:
        return hot_list
