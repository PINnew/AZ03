import csv
import matplotlib.pyplot as plt

# Имя файла, из которого нужно считать данные
output_filename = 'processed_prices.csv'

# Считываем цены из выходного файла
prices = []
with open(output_filename, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        prices.append(int(row[0]))  # Добавляем цену в список

# Строим гистограмму
plt.hist(prices, bins=20, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)

# Показываем график
plt.show()