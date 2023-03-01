import random
import tkinter as tk

NUM_POINTS = 90000

RADIUS = 200

root = tk.Tk()
root.title("Вычисление числа π")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


def draw_picture():
    canvas.create_oval(200 - RADIUS, 200 - RADIUS, 200 + RADIUS, 200 + RADIUS,
                       outline="black", width=2)
    count_inside = 0
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                           200 + x * RADIUS, 200 - y * RADIUS,
                           outline="green", width=1)
        count_inside += 1
    else:
        canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                           200 + x * RADIUS, 200 - y * RADIUS,
                           outline="red", width=1)

    root.after(10, draw_picture)


button = tk.Button(root, text="Вычислить π", command=draw_picture)
button.pack()

root.mainloop()
