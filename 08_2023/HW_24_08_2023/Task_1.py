# Задание №1
# а) Получить погоду с динамического сайта погоды, используя selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://www.accuweather.com/ru/uz/tashkent/351199/weather-forecast/351199')
weather_time = driver.find_element(By.CLASS_NAME, "temp-container").text[:4]

print(weather_time)
time.sleep(5)

driver.close()
driver.quit()
