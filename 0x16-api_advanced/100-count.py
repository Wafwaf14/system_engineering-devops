#!/usr/bin/python3
"""Modulee Doneee"""

import requests


def count_words(subreddit, listWord, countWord={}, after=None):
    """Querying Reddit API"""

    mysubInfo = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": after},
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False
    )

    if mysubInfo.status_code != 200:
        return None

    info = mysubInfo.json()

    myhot_l = [child.get("data").get("title")
               for child in info.get("data").get("children")]

    if not myhot_l:
        return None

    listWord = list(dict.fromkeys(listWord))

    if countWord == {}:
        countWord = {word: 0 for word in listWord}

    for title in myhot_l:
        splitWords = title.split(' ')
        for word in listWord:
            for myWord in splitWords:
                if myWord.lower() == word.lower():
                    countWord[word] += 1

    if not info.get("data").get("after"):
        countsOrdred = sorted(countWord.items(), key=lambda kv: kv[0])
        countsOrdred = sorted(countWord.items(),
                              key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in countsOrdred if v != 0]
    else:
        return count_words(subreddit, listWord, countWord,
                           info.get("data").get("after"))
