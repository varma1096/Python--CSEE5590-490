import requests
from bs4 import BeautifulSoup

def collect_href():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    source_code = requests.get(url) # Gets the source code
    source_text = source_code.text
    soup_text = BeautifulSoup(source_text, 'html.parser')

    with open(r'input1.txt','a') as file:
        for line in soup_text.find_all('p'):
            file.write(str(line.text))

if  __name__ == '__main__':
    collect_href()