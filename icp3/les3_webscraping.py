import requests
from bs4 import BeautifulSoup

def collect_href():
    url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

    i_code = requests.get(url)
    source_text = i_code.text
    soup_text = BeautifulSoup(source_text, 'html.parser')
    #print(soup_text)
    for link in soup_text.findAll('a'):
        href = link.get('href')
        print(href)


collect_href()