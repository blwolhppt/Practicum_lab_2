import random
import tkinter as tk
import time

NUM_POINTS = 50000

RADIUS = 200

root = tk.Tk()
root.title("Вычисление числа π")

canvas = tk.Canvas(root, width=400, height=400, background="black")
canvas.pack()


def draw_picture():
    canvas.create_oval(200 - RADIUS, 200 - RADIUS, 200 + RADIUS, 200 + RADIUS,
                       outline="black", width=2)

    count_inside = 0

    for i in range(NUM_POINTS):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        canvas.create_oval(200 - RADIUS, 200 - RADIUS, 200 + RADIUS,
                           200 + RADIUS, outline="white", width=2)
        if x ** 2 + y ** 2 <= 1:
            canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                               200 + x * RADIUS, 200 - y * RADIUS,
                               outline="#7CFC00", width=3)
            count_inside += 1
        else:
            canvas.create_oval(200 + x * RADIUS, 200 - y * RADIUS,
                               200 + x * RADIUS, 200 - y * RADIUS,
                               outline="#1E90FF", width=3)

    pi_approx = 4 * count_inside / NUM_POINTS

    root.title(f"Вычисление числа π (приближение: {pi_approx:.6f})")


button = tk.Button(root, text="Вычислить π", command=draw_picture)
button.pack()

root.mainloop()
