import bs4
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def url_ym(data):
    url = f"https://market.yandex.ru/search?cvredirect=0&text={data}&local-offers-first=0"
    return url

def parse():
    url = "https://market.yandex.ru/catalog--smartfony/16814639/list?hid=91491&glfilter=16816262:16816264&onstock=1"

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'market.yandex.ru',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text.encode('utf8'))
    print(response.status_code)

parse()