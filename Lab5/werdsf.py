import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Імпорт даних в масив NumPy та побудова графіків
def import_and_plot_data(filename):
    data = pd.read_csv(filename)
    dates = data['Date'].values
    prices = data['Price'].values

    # Побудова графіку
    plt.plot(dates, prices)
    plt.xlabel('Дата')
    plt.ylabel('Ціна')
    plt.title(f'Ціна акцій з файлу {filename}')
    plt.xticks(rotation=45)  # Повернення підписів на вісі X
    plt.grid(True)

# Список файлів для імпорту та побудови графіків
files = ['123.csv', '321.csv']  # Перелічіть імена ваших CSV-файлів тут

# Побудова графіків для кожного файлу
num_files = len(files)
num_cols = 2
num_rows = num_files // num_cols + (num_files % num_cols > 0)  # Округлення до ближчого цілого в більшу сторону
plt.figure(figsize=(15, 7 * num_rows))

for i, file in enumerate(files, start=1):
    plt.subplot(num_rows, num_cols, i)
    import_and_plot_data(file)

plt.tight_layout()  # Автоматична оптимізація розміщення графіків
plt.show()
