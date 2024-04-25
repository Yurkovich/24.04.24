import requests
from bs4 import BeautifulSoup
from time import sleep

def check_discount(discount_element):
            if discount_element is not None:
                return discount_element.text
            else:
                return 'Отсутствует'

for page in range(1):

    sleep(3)
    url = f'https://gabestore.ru/catalog?&page={page}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='shop-item')

    for games in data:
        name = games.find('a', class_="shop-item__name").text
        price = games.find('div', class_='shop-item__price-current').text
        discount_element = games.find('div', class_='shop-item__price-discount')

        result = (f'Название: {name}\nЦена: {price}\nСкидка: {check_discount(discount_element)}\n\n')
        with open('parsed.txt', 'a', encoding='utf-8') as file:
              file.write(result)


























# for count in range(1, 8):

#     sleep(3)
#     url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'lxml')
#     data = soup.find_all('div', class_='w-full rounded border')


#     for i in data:
#         name = i.find('h4').text.replace('\n', '')
#         price = i.find('h5').text
#         url_img = 'https://scrapingclub.com' + i.find('img', class_='card-img-top img-fluid').get('src')
#         print(name + '\n' + price + '\n' + url_img + '\n\n')
