from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

# Инициализация драйвера
driver = webdriver.Chrome()

# URL страницы
url = 'https://www.divan.ru/izhevsk/category/divany-i-kresla'
driver.get(url)

try:
    # Ожидание загрузки элементов с ценами
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-LD-ZU KIkOH'))
    )

    # Парсинг цен
    prices = []
    for element in elements:
        price_text = element.text.split()[0].replace(' ', '')  # Убираем пробелы
        if price_text.isdigit():  # Проверка, что цена корректная
            prices.append(int(price_text))

finally:
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