import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.5)Gecko/20091102 Firefox"}

def get_url():
    for count in range(1, 10):
        url = f"https://www.avito.ru/vladivostok/kvartiry/sdam-ASgBAgICAUSSA8gQ?p={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="iva-item-content-rejJg")
        for i in data:
            card_url = "https://www.avito.ru" + i.find("a").get("href")
            yield card_url
def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="style-item-view-PCYlM react-exp")
        name = data.find("h1", class_="style-title-info-title-eHW9V style-title-info-title-text-CoxZd").text
        price = data.find("span", class_="js-item-price style-item-price-text-_w822 text-text-LurtD text-size-xxl-UPhmI").text
        url_img = "iva-item-sliderLink-uLz1v" + data.find("img", class_="iva-item-sliderLink-uLz1v").get("src")
        yield name, price, url_img