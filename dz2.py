import numpy as np
import matplotlib.pyplot as plt

# Генерируем два массива случайных чисел
x = np.random.rand(5)  # массив из 5 случайных чисел для оси X
y = np.random.rand(5)  # массив из 5 случайных чисел для оси Y

# Выводим сгенерированные данные
print("X:", x)
print("Y:", y)

# Создаем диаграмму рассеяния
plt.scatter(x, y)

# Добавляем заголовок и метки осей
plt.title('Диаграмма рассеяния')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Показываем график
plt.show()