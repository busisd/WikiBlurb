import requests
import re
from bs4 import BeautifulSoup

url_choice = ''

while url_choice != 'quitnow':
    url_choice = input('\n\nWhat do you want to learn about today? ')
    url_choice = url_choice.strip()
    url_choice.replace(' ', '_')

    print()

    #url_choice = 'Donald_Harris_(composer)'
    site_url = 'https://en.wikipedia.org/wiki/' + url_choice
    site_doc = requests.get(site_url, auth=('user', 'pass'))

    site_html = site_doc.content

    #print(site_doc.text)
    #print(site_doc.headers)


    site_soup = BeautifulSoup(site_html, 'html.parser')

    article_title = site_soup.h1.string

    citation_re = re.compile('\[\d*\]')
    article_blurb = ''
    for string in site_soup.p.strings:
        if not (citation_re.match(string)):
            article_blurb += string

    print(article_title+':')
    print(article_blurb)

    #for tag in site_soup.find_all('p'):
    #    print(tag.name)
