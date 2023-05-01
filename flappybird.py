from tkinter import *
import keyboard
import time
import random

window = Tk()
window.title("Flappy Bird")
window.geometry("400x500")

canvas = Canvas(window, bg="black", width=400, height=500)
canvas.pack()

bird = canvas.create_oval(50, 225, 75, 250, fill="white")

pipes = []
for i in range(3):
    x = 400 + (i * 150)
    y = random.randint(100, 400)
    pipe_top = canvas.create_rectangle(x, 0, x - 50, y, fill="white")
    pipe_bottom = canvas.create_rectangle(x, y + 100, x - 50, 500,
                                          fill="white")
    pipes.append((pipe_top, pipe_bottom))

gravity = 0.1
jump = 0.5
velocity = 0


def move_bird_up():
    global velocity
    velocity -= jump
    canvas.move(bird, 0, velocity*0.3)
    window.update()
    time.sleep(0.05)
    velocity += gravity


def move_bird_down():
    global velocity
    velocity -= jump
    canvas.move(bird, 0, -velocity)
    window.update()
    time.sleep(0.05)
    velocity += gravity


def move_pipes():
    for pipe in pipes:
        canvas.move(pipe[0], -5, 0)
        canvas.move(pipe[1], -5, 0)
        if canvas.coords(pipe[0])[2] < 0:
            y = random.randint(100, 400)
            canvas.coords(pipe[0], 400, 0, 350, y)
            canvas.coords(pipe[1], 400, y + 100, 350, 500)
    window.update()
    time.sleep(0.05)


def check_collision():
    bird_coords = canvas.coords(bird)
    for pipe in pipes:
        pipe_top_coords = canvas.coords(pipe[0])
        pipe_bottom_coords = canvas.coords(pipe[1])
        if bird_coords[2] > pipe_top_coords[0] and bird_coords[0] < \
                pipe_top_coords[2]:
            if bird_coords[1] < pipe_top_coords[3] or bird_coords[3] > \
                    pipe_bottom_coords[1]:
                return True
    if bird_coords[1] < 0 or bird_coords[3] > 500:
        return True
    return False


def start_game():
    global velocity
    while True:
        if check_collision():
            canvas.create_text(200, 200, text="GAME OVER!",
                               font=("Helvetica", 30), fill="red")
            window.update()
            break

        if keyboard.is_pressed('up'):
            move_bird_up()
        else:
            move_bird_down()
        #if keyboard.is_pressed('down'):
        #    move_bird_down()

        move_pipes()


start_game()

window.mainloop()
