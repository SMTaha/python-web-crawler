import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.olx.com.pk/all-results/q-raspberry-pi/?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class' : 'detailsLink'}):
            href = link.get('href')
            title = link.span
            title = str(title)[6: -7]
            # print(href)
            # print(title)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('h1', {'class': 'brkword lheight28'}):
        print('Name: ', item_name.string.strip())
    for item_price in soup.findAll('strong', {'class': 'xxxx-large margintop7 block not-arranged'}):
        print(item_price.string)
trade_spider(1)