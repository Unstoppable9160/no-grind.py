from bs4 import BeautifulSoup
import requests


def prettify(link):
    """Returns website as string"""
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')
    return soup.prettify()


def text(link):
    """Get all text from link"""
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')
    return soup.text


def find_tag(link, tag="h2"):
    """Find all uses of an html tag in a website"""
    website = requests.get(link)
    soup = BeautifulSoup(website.content, 'html.parser')
    tags = soup.find_all(tag)
    for soups in tags:
        return soups.string
