import requests
from bs4 import BeautifulSoup
import csv
import time
import random


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}


url = 'https://www.detmir.ru/catalog/index/name/encyclopedias_children/page/'
num_page = '1'
book_hrefs = []

def UrlList(html):
    with open('hrefsDM.txt', 'a', encoding='utf-8') as file:
        file.write(html + ',\n')

with open('DetMir.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
        'Articule',
        'Code',
        'Seller',
        'Brand'
        )
    )


while True: 
    response = requests.get(url = url + num_page, headers = headers)
    if response.status_code == 200:        
        soup = BeautifulSoup(response.text, "lxml")
        book_items = soup.find_all('a', class_='sC', href = True)
        for i in book_items:
            UrlList(i['href'])
            book_hrefs.append(i['href'])
        print(len(book_hrefs))
        num_page = str(int(num_page) + 1)



    
    

    




