import tkinter as tk

# Create a tkinter window and a Canvas widget
root = tk.Tk()
root.title("Elastic Collision")
canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

# Define initial parameters of the particle
radius = 20
x = 400
y = 300
vy = 5
ay = 1


# Define the function for moving the particle and handling collisions
def move_particle():
    global x, y, vy, ay
    canvas.delete("all")
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                       fill="grey",
                       outline="white")
    vy += ay
    y += vy
    # Handle collisions with the top and bottom edges of the screen
    if y + radius >= 600:
        y = 600 - radius
        vy = -vy
    elif y - radius <= 0:
        y = radius
        vy = -vy
    # Call the move_particle function after a delay of 10 milliseconds
    root.after(20, move_particle)


# Call the move_particle function to start the animation
move_particle()

# Run the tkinter main loop
root.mainloop()
