import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://www.labirint.ru'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


# start
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
def get_data(html):
    bs = BS4(html, 'html.parser')
    items = bs.find_all('div',class_='js-content-block-tab js-content-block-tab_all content-block')  # content-block-outer
    book_list = []
    for item in items:
        title = item.find('div', class_='product-cover').get_text(strip=True)
        image = URL + item.find('div', class_='product-cover__cover-wrapper').find('img').get('src')
        book_list.append({'title': title, 'image': image})
    return book_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        book_list2 = []
        for page in range(1, 2):
            response = get_html(
                "https://www.labirint.ru/books/", params={'page': page})
            book_list2.extend(get_data(response.text))
        return book_list2
    else:
        raise Exception('Error in Parsing')


print(parsing())
