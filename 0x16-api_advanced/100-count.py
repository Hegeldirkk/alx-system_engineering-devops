#!/usr/bin/python3
""" Contains the function count_words(subreddit, word_list)) """
import requests


def count_words(subreddit, word_list, hot_list_titles=[], after='null'):
    """ returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    baseUrl = 'https://www.reddit.com/r/'
    url = baseUrl + subreddit + "/hot.json"
    headers = {'User-Agent': "linux:1:v1.0 (by /u/hegel)"}
    parameters = {"limit": "100", "after": after}
    response = requests.get(url,
                            headers=headers,
                            params=parameters,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    hot_list_of_dicts = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    """""to print the after string, which acts as a "pointer"
    to the next response uncomment the following line"""
    hot_list_titles.extend([reddit.get("data").get("title") for
                            reddit in hot_list_of_dicts])
    """to print the length of the hot_list_titles uncomment
    the following line"""

    if after is None:
        to_print_dict = {x: 0 for x in word_list}
        for word in word_list:
            count = 0
            for title in hot_list_titles:
                split_title = title.split()
                new_split = [element.lower() for element in split_title]
                count = count + new_split.count(word.lower())
            if count != 0:
                to_print_dict[word] = to_print_dict[word] + count

        for elem in sorted(to_print_dict.items(), key=lambda x: (-x[1], x[0])):
            if elem[1] != 0:
                print("{}: {}".format(elem[0], elem[1]))
    else:
        return count_words(subreddit, word_list,
                           hot_list_titles, after)
