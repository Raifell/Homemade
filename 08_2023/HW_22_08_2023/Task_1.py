# Задание №1
# а) Получить погоду в Ташкенте с статического сайта погоды, используя string.split()
# б) Получить погоду в Ташкенте с статического сайта погоды, используя bs4

from bs4 import BeautifulSoup
import requests

url = 'https://www.gismeteo.kz'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'
}

s = requests.session()
response = s.get(url=url, headers=headers).text
soup = BeautifulSoup(response, features='html.parser')

weather_block = soup.find('div', class_='frame-now')

weather_time = weather_block.find('div', class_='current-time').text
weather_now = weather_block.find('span', class_='unit unit_temperature_c').text
wind = weather_block.find('span', class_='unit unit_wind_m_s').text[:-3]
atmospheric_pressure = weather_block.find('span', class_='unit unit_pressure_mm_hg_atm').text
humidity = weather_block.find('div', class_='weather-item weather-humidity').find('div', class_='item-value').text


print(weather_time)
print('Температура: ', weather_now)
print('Скорость ветра: ', wind)
print('Давление: ', atmospheric_pressure)
print('Влажность: ', humidity)

