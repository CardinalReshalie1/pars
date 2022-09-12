
from turtle import ScrolledCanvas
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.5)Gecko/20091102 Firefox"}

def get_url():
    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
        for i in data:
            card_url ="https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

def array():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p", class_="card-text").text
        url_img = "card-img-top img-fluid" + data.find("img", class_="card-img-top img-fluid").get("src")
        yield name, price, text, url_img