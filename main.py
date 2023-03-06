import random
import tkinter as tk

# создание окна tkinter
window = tk.Tk()
window.geometry('500x500')
window.title('Приближение числа π методом Монте-Карло')

# создание холста для отображения точек
canvas = tk.Canvas(window, width=400, height=400, bg='white')
canvas.pack(padx=20, pady=20)

# создание прямоугольника и круга на холсте
canvas.create_rectangle(50, 50, 350, 350)
canvas.create_oval(50, 50, 350, 350)

# переменные для подсчета точек
total_points = 0
points_in_circle = 0

# функция для генерации точек и подсчета числа π
def generate_point():
    global total_points, points_in_circle
    # генерация случайных координат точки внутри квадрата
    x = random.uniform(50, 350)
    y = random.uniform(50, 350)
    # проверка, находится ли точка внутри круга
    if (x-200)**2 + (y-200)**2 <= 150**2:
        points_in_circle += 1
    total_points += 1
    # обновление значения числа π на метке
    pi_estimate = 4 * points_in_circle / total_points
    pi_label.config(text=f'π ≈ {pi_estimate:.5f}')

# функция для добавления 100 точек на холст
def add_points():
    canvas.create_rectangle(50, 50, 350, 350, width=2)
    canvas.create_oval(50, 50, 350, 350, width=2)
    for i in range(300):
        generate_point()
        # отображение точки на холсте
        x = random.uniform(50, 350)
        y = random.uniform(50, 350)
        if (x-200)**2 + (y-200)**2 <= 150**2:
            color = '#7CFC00'
        else:
            color = '#1E90FF'
        canvas.create_oval(x, y, x, y, outline=color, width=2)
    # повторный вызов функции через 100 миллисекунд
    window.after(100, add_points)

# создание метки для отображения значения π
pi_label = tk.Label(window, text='π ≈ 0', font=('Arial', 16))
pi_label.pack()

# запуск добавления точек на холст
window.after(0, add_points)

# запуск главного цикла tkinter
window.mainloop()