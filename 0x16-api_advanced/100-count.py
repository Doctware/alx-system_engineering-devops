#!/usr/bin/python3
""" this module count base on given sorted out keyward """
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively counts the occurrences of keywords
    in the titles of hot articles on a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "keyword-counter/0.1"}
    params = {"limit": 100, "after": after}

    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if resp.status_code != 200:
        return

    data = resp.json().get("data", {})
    posts = data.get("children", [])

    if not posts and not after:
        return

    # Normalize keywords in the word_list to lowercase
    word_list = [word.lower() for word in word_list]

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words_in_title = title.split()

        for word in words_in_title:
            # Clean the word to remove non-alphanumeric characters
            clean_word = ''.join(filter(str.isalnum, word))
            if clean_word in word_list:
                counts[clean_word] = counts.get(clean_word, 0) + 1

    if data.get("after"):
        return count_words(subreddit, word_list, data.get("after"), counts)
    else:
        # When recursion is complete, sort and print the results
        sorted_counts = sorted(counts.items(),
                               key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
