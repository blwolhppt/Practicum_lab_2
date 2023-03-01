import random
import tkinter as tk

# Количество точек, которые будут использоваться для вычисления π
NUM_POINTS = 90000

# Радиус единичной окружности
RADIUS = 200

# Создаем главное окно
root = tk.Tk()
root.title("Вычисление числа π")

# Создаем Canvas для рисования
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Функция для рисования картинки
def draw_picture():
    # Очищаем Canvas
    #canvas.delete(tk.ALL)

    # Рисуем единичную окружность
    canvas.create_oval(200-RADIUS, 200-RADIUS, 200+RADIUS, 200+RADIUS, outline="black", width=2)

    # Счетчик точек, попавших внутрь единичной окружности
    count_inside = 0

    # Генерируем случайные точки и проверяем, попадают ли они внутрь единичной окружности
    for i in range(NUM_POINTS):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            # Рисуем точки, попавшие внутрь единичной окружности, зеленым цветом
            canvas.create_oval(200+x*RADIUS, 200-y*RADIUS, 200+x*RADIUS, 200-y*RADIUS, outline="green")
            count_inside += 1
        else:
            # Рисуем точки, не попавшие внутрь единичной окружности, красным цветом
            canvas.create_oval(200+x*RADIUS, 200-y*RADIUS, 200+x*RADIUS, 200-y*RADIUS, outline="red")

    # Вычисляем приближенное значение числа π
    pi_approx = 4 * count_inside / NUM_POINTS

    # Отображаем результат в заголовке окна
    root.title(f"Вычисление числа π (приближение: {pi_approx:.6f})")

# Создаем кнопку для запуска вычислений и рисования картинки
button = tk.Button(root, text="Вычислить π", command=draw_picture)
button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()