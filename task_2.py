""" Homework """

import requests
from bs4 import BeautifulSoup


def get_weather_with_split():
    response = requests.get("https://www.gismeteo.kz/weather-astana-5165/")
    data = response.text
    weather_info = data.split('<div class="value">')[1].split('</div>')[0]
    print("Погода в Астане (с использованием split):", weather_info)


def get_weather_with_bs4():
    response = requests.get("https://www.gismeteo.kz/weather-astana-5165/")
    soup = BeautifulSoup(response.content, 'html.parser')
    weather_info = soup.find('div', class_='value').text
    print("Погода в Астане (с использованием bs4):", weather_info)


if __name__ == "__main__":
    get_weather_with_split()
    get_weather_with_bs4()
