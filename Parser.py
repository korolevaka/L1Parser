import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://sibdroid.ru/catalog/smartfony_apple/'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all('div', class_="card-product__bottom-value")
    iphone_prices = []
    for price in prices:
        iphone_prices.append(
            int(price.find('span', class_='card-product__bottom-new-price').text.replace("\n              ",
                                                                                         '').replace(
                "₽              \n\n\n\n\n", '').replace(" ", '')))
    print("Минимальная цена: ", min(iphone_prices))
    print("Максимальная цена: ", max(iphone_prices))
    print("Средняя цена: ", sum(iphone_prices) / len(iphone_prices))