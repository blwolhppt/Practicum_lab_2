import random
import tkinter as tk

# Количество точек, которые будут использоваться для вычисления π
NUM_POINTS = 10000

# Радиус единичной окружности
RADIUS = 200

# Список типов точек для анимации
POINT_TYPES = ["square", "diamond", "triangle", "circle"]

# Создаем главное окно
root = tk.Tk()
root.title("Вычисление числа π")

# Создаем Canvas для рисования
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Функция для рисования картинки
def draw_picture():
    # Очищаем Canvas
    canvas.delete(tk.ALL)

    # Рисуем единичную окружность
    canvas.create_oval(200-RADIUS, 200-RADIUS, 200+RADIUS, 200+RADIUS, outline="black")

    # Генерируем случайные точки и проверяем, попадают ли они внутрь единичной окружности
    for i in range(NUM_POINTS):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            # Рисуем точки, попавшие внутрь единичной окружности, используя разные типы точек
            point_type = POINT_TYPES[i % len(POINT_TYPES)]
            canvas.create_oval(200+x*RADIUS, 200-y*RADIUS, 200+x*RADIUS, 200-y*RADIUS, outline="green", tags=point_type)
        else:
            # Рисуем точки, не попавшие внутрь единичной окружности, красным цветом
            canvas.create_oval(200+x*RADIUS, 200-y*RADIUS, 200+x*RADIUS, 200-y*RADIUS, outline="red")

    # Вычисляем приближенное значение числа π
    count_inside = len(canvas.find_withtag("square")) + len(canvas.find_withtag("diamond")) + len(canvas.find_withtag("triangle")) + len(canvas.find_withtag("circle"))
    pi_approx = 4 * count_inside / NUM_POINTS

    # Отображаем результат в заголовке окна
    root.title(f"Вычисление числа π (приближение: {pi_approx:.6f})")

    # Анимируем точки, используя метод after()
    animate_point(0)

def animate_point(i):
    if i < NUM_POINTS:
        # Выбираем случайную точку и меняем ее тип на следующий в списке
        point_type = POINT_TYPES[(i + len(POINT_TYPES) - 1) % len(POINT_TYPES)]
        point_id = random.choice(canvas.find_withtag(point_type))
        canvas.itemconfigure(point_id, outline="white")
        canvas.dtag(point_id, point_type)
        next_point_type = POINT_TYPES[i % len(POINT_TYPES)]