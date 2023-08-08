#!/usr/bin/python3
""" recurse """
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """ Return a list containing the titles of all article
    for a given subreddit
    """
    if after is None:
        return hot_list

    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    try:
        js = r.json()
    except ValueError:
        return None

    try:
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))
    except Exception:
        return None

    return recurse(subreddit, hot_list, after)
