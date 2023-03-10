import random
import tkinter as tk

window = tk.Tk()
window.geometry('500x500')

canvas = tk.Canvas(window, width=400, height=400, bg='white')
canvas.pack()

canvas.create_rectangle(50, 50, 350, 350)
canvas.create_oval(50, 50, 350, 350)

total_points = 0
points_in_circle = 0


def generate_point():
    global total_points, points_in_circle
    x = random.uniform(50, 350)
    y = random.uniform(50, 350)
    if (x - 200) ** 2 + (y - 200) ** 2 <= 150 ** 2:
        points_in_circle += 1
    total_points += 1

    pi_estimate = 4 * points_in_circle / total_points
    pi_label.config(text=f'π ≈ {pi_estimate:.5f}')
    amount_label.config(text=f'кол-во точек = {total_points}')

def add_points():
    canvas.create_rectangle(50, 50, 350, 350, width=2)
    canvas.create_oval(50, 50, 350, 350, width=2)
    for i in range(200):
        generate_point()
        x = random.uniform(50, 350)
        y = random.uniform(50, 350)
        if (x - 200) ** 2 + (y - 200) ** 2 <= 150 ** 2:
            color = '#7CFC00'
        else:
            color = '#1E90FF'
        canvas.create_oval(x, y, x, y, outline=color, width=2)

    window.after(10, add_points)


pi_label = tk.Label(window, text='π ≈ 0', font=('Arial', 16))
amount_label = tk.Label(window, text='кол-во точек =', font=('Arial', 16))
pi_label.pack()
amount_label.pack()

window.after(0, add_points)

window.mainloop()
