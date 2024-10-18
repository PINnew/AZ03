from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import pandas as pd
import time


driver = webdriver.Chrome()

# URL страницы
url = 'https://www.divan.ru/izhevsk/category/divany-i-kresla'

driver.get(url)

# Даем время для загрузки страницы
time.sleep(8)

# Парсинг цен
prices = []
elements = driver.find_elements(By.CLASS_NAME, 'ui-LD-ZU KIkOH')  # Находим элементы с ценами
for element in elements:
    price_text = element.text.replace('₽', '').replace(' ', '')  # Убираем символы и пробелы
    if price_text.isdigit():  # Проверка, что цена корректная
        prices.append(int(price_text))

# Закрываем драйвер
driver.quit()

# Сохранение в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('pricesdv.csv', index=False)

# Подсчет средней цены
average_price = df['Price'].mean()
print(f'Средняя цена: {average_price:.2f} ₽')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y')
plt.savefig('price_histogram.png')
plt.show()