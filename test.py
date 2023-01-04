import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "https://kinobaza.com.ua/movies/top"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
link = "https://kinobaza.com.ua" + soup.find('div', class_="col-md-8").find('h2', class_="h3 mb-0" ).find('a').get('href')
uk_name = soup.find('div', class_="col-md-8").find('h2', class_="h3 mb-0" ).find('span', itemprop="name").text
ua_name = soup.find('div', class_="col-md-8").find('h4').text


data = []


for p in range(1, 5):

    url = f"https://kinobaza.com.ua/movies/top?page={p}"
    r = requests.get(url)
    sleep(1)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div', class_="col-md-8")


    for film in films:
        link = "https://kinobaza.com.ua" + film.find('h2', class_="h3 mb-0").find('a').get('href')
        uk_name = film.find('h2', class_="h3 mb-0").find('span', itemprop="name").text
        ua_name = film.find('h4').text

        data.append([link, uk_name, ua_name])

header = ['link', 'uk_name', 'ua_name']

df = pd.DataFrame(data, columns=header)
df.to_csv("/Users/User/PycharmProjects/requests_test.csv", sep=';', encoding='cp1251')