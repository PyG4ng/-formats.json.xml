import json
from collections import Counter
from pprint import pprint


def get_all_news_in_list_of_words(file):
    """Open a json file, get all the text in the description key, split it in
     words and put them all in a list

    Args:
        file: Name, if the file is in the same folder, or path
        to the json file

    Returns: A list of words

    """
    with open(file, 'r', encoding='utf-8') as f:
        content = json.load(f)

    items = content.get('rss').get('channel').get('items')

    all_news_words = []
    for article in items:
        all_news_words.extend(article.get('description').split())
    return all_news_words


def n_most_common_words_length_greater_m(data, n, m):
    """Take a list of words an return the n most common words with length
     greater than m

    Args:
        data (list[str]): list of words
        n (int): Number of common words to find
        m (int): length to compare to

    Returns: list of n most common words

    """
    sequence_words = [word.lower() for word in data if len(word) > m]
    count = Counter(sequence_words).most_common(n)
    return count


if __name__ == '__main__':
    words = get_all_news_in_list_of_words('newsafr.json')
    most_common = n_most_common_words_length_greater_m(words, 10, 6)

    pprint(most_common)
