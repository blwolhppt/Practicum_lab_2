import math
import tkinter as tk

# создание окна
window = tk.Tk()
window.title("Ряды Фурье")
window.geometry("800x600")

# задание параметров для прямоугольной функции
amplitude = 100  # амплитуда
frequency = 1/2  # частота
phase = 0  # фаза

# задание параметров для разложения Фурье
num_terms = 50  # количество гармоник

# создание холста для рисования графика
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# функция для рисования рядов Фурье
def draw_fourier_series():
    canvas.delete("all")
    x_start, x_end = 50, 550
    y_start, y_end = 200, 200
    x = x_start
    y = y_start
    x_center, y_center = x, y
    radius = amplitude * 4 / math.pi
    canvas.create_oval(x_center - radius, y_center - radius, x_center + radius,
                       y_center + radius, outline="black")
    for i in range(1, num_terms+1):
        prev_x, prev_y = x, y
        n = 2 * i - 1
        radius = amplitude * (4 / (n * math.pi))
        x += radius * math.cos(n * frequency * t + phase)
        y += radius * math.sin(n * frequency * t + phase)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        canvas.create_line(prev_x, prev_y, x, y)
    canvas.create_line(x, y, x_end, y)

# функция для обновления анимации
def update_animation():
    global t
    t += 0.05
    draw_fourier_series()
    window.after(50, update_animation)

# запуск анимации
t = 0
update_animation()

# запуск главного цикла
window.mainloop()