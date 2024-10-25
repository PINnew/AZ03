from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициализация браузера
driver = webdriver.Chrome()

url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)
time.sleep(5) # Задаём время, подгружаем сайт
# Поиск всех светильников на странице
elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
prices = []

for element in elements:
    price = element.find_element(By.CSS_SELECTOR, '[itemprop="price"]').get_attribute('content')
    price_text = price.replace('₽', '').replace(' ', '')  # Убираем символы и пробелы
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
