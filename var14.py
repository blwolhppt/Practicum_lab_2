import tkinter as tk
import random
import sys

sys.setrecursionlimit(1500)

window = tk.Tk()

window.title('Вариант 14. Pi через метод Монте-Карло ')

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


# def point():
#    coord = random.randint(6, 299)
#    return coord
#
#
# def check_point():
#    x = point()
#    y = point()
#    canvas.create_oval(x, y, x + 1, y, fill="red",
#                       outline="red", width=2)
#
#
# window.after(10, lambda: check_point)
# window.after(10, lambda: check_point)
# window.after(10, lambda: check_point)

def points():


    window.after(100, points)


points()

window.mainloop()
