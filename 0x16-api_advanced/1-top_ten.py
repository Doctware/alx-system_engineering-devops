#!/usr/bin/python3
""" this module get the top ten hot post """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "top-ten-subreddit-posts/0.1"}
    params = {"limit": 10}

    resp = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)

    if resp.status_code == 200:
        data = resp.json()
        posts = data.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
