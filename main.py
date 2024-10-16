from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv


driver = webdriver.Chrome()

# URL страница
url = 'https://www.cian.ru/snyat-1-komnatnuyu-kvartiru/'

# Открываем сайт
driver.get(url)

# Даем странице время загрузиться
time.sleep(5)  # лучше использовать WebDriverWait для более надежного ожидания

# Находим элементы, содержащие цены
prices = driver.find_elements(By.XPATH, '//span[@data-mark="MainPrice"]/span')

# Открытие файла CSV для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price']) # Запись заголовка

    # Извлекаем текст цен и выводим их
    for price in prices:
        writer.writerow([price.text])

print(f"Данные о ценах сохранены в 'prices.csv'")

# Закрываем браузер
driver.quit()