"""Retrive and print words from an URL 

Usage:
    python3 story.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL 
    
    Args:
        url: the URL to fetch the words from

    Returns:
        A list of strings containing the words from the
        document
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print a list of items

    Args:
        items: list of items that will be printed
    """
    for item in items:
        print(item)


def main(url):
    print_items(fetch_words(url))


if __name__ == '__main__':
    main(sys.argv[1])
