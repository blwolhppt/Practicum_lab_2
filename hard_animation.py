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
    x_coords = [x_start]
    y_coords = [y_start]
    for i in range(num_terms, 0, -1):
        n = 2 * i - 1
        radius = amplitude * (4 / (n * math.pi))
        x = x_coords[-1] + radius * math.cos(n * frequency * t + phase)
        y = y_coords[-1] + radius * math.sin(n * frequency * t + phase)
        x_coords.insert(0, x)
        y_coords.insert(0, y)
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    canvas.create_line(x_coords, y_coords, fill="blue")

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