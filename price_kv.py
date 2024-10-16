import csv

with open('prices.csv', mode='r', newline='', encoding='utf-8') as infile, \
        open('processed_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Price'])
    next(csv.reader(infile))  # Пропускаем заголовок
    for row in csv.reader(infile):
        if row:
            try:
                writer.writerow([int(float(row[0].replace('₽/мес.', '').replace(' ', '').strip()))])
            except ValueError as e:
                print(f"Ошибка преобразования: {row[0]}: {e}")

print("Данные обработаны и сохранены в 'processed_prices.csv'")