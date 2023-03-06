import tkinter as tk
import random
import math

# Создаем окно приложения
root = tk.Tk()
root.title('Аппроксимация экспоненты методом Монте-Карло')

# Создаем холст для рисования
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Отображаем текстовое поле для вывода результата
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=('Arial', 16),
                        pady=10)
result_label.pack()

# Инициализируем переменные для подсчета точек и точек внутри круга
total_points = 0
inside_points = 0


# Функция для обработки нажатия кнопки "Старт"
def start_simulation():
    global total_points, inside_points

    # Генерируем 100 случайных точек внутри квадрата
    for i in range(100):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        total_points += 1

        # Если точка попала внутрь круга, увеличиваем счетчик
        if y <= math.exp(x):
            inside_points += 1

        # Отображаем точку на холсте
        canvas.create_oval(x * canvas_width, (1 - y) * canvas_height,
                           x * canvas_width + 1, (1 - y) * canvas_height + 1,
                           fill='blue')

    # Вычисляем приближенное значение экспоненты
    exp_approx = (inside_points / total_points) * canvas_width

    # Выводим результат на экран
    result_text.set(f'Приближенное значение экспоненты: {exp_approx:.4f}')

    # Если не все точки нарисованы, повторяем симуляцию через 50 мс
    if total_points < 10000:
        root.after(50, start_simulation)


# Создаем кнопку для запуска симуляции
start_button = tk.Button(root, text='Старт', font=('Arial', 16),
                         command=start_simulation)
start_button.pack()

root.mainloop()