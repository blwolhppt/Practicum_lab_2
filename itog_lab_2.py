import math
import random
import tkinter as tk

NUM_POINTS = 90000

RADIUS = 200

root = tk.Tk()
root.title("Вычисление числа π")

canvas = tk.Canvas(root, width=400, height=400, background="black")
canvas.pack()

count_inside = 0


def draw_picture():
    canvas.create_oval(200 - RADIUS, 200 - RADIUS, 200 + RADIUS, 200 + RADIUS,
                       outline="white", width=2)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                           200 + x * RADIUS, 200 - y * RADIUS,
                           outline="#00FF00", width=4)

        m = 30
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 60
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)
        m = 90
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 120
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)
        m = 150
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 180
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 210
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 240
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)
        m = 270
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 300
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 330
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)

        m = 360
        x_new = x * math.cos(m) - y * math.sin(m)
        y_new = x * math.sin(m) + y * math.cos(m)
        canvas.create_oval(200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           200 + x_new * RADIUS, 200 - y_new * RADIUS,
                           outline="#00FF00", width=4)
    else:
        canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                           200 + x * RADIUS, 200 - y * RADIUS,
                           outline="#4169E1", width=4)
        canvas.create_oval(200 - x * RADIUS, 200 - y * RADIUS,
                           200 - x * RADIUS, 200 - y * RADIUS,
                           outline="#4169E1", width=4)
        canvas.create_oval(200 - x * RADIUS, 200 + y * RADIUS,
                           200 - x * RADIUS, 200 + y * RADIUS,
                           outline="#4169E1", width=4)
        canvas.create_oval(200 + x * RADIUS, 200 + y * RADIUS,
                           200 + x * RADIUS, 200 + y * RADIUS,
                           outline="#4169E1", width=4)

    root.after(1, draw_picture)


button = tk.Button(root, text="Вычислить π", command=draw_picture)
button.pack()

root.mainloop()
