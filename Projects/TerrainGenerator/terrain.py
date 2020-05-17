import math
import turtle
import random
from tkinter import *

VERTICES = []
TRIANGLES = []
count = 0
def parameters():
    x1 = float(x1_entry.get())
    y1 = float(y1_entry.get())
    z1 = float(z1_entry.get())

    x2 = float(x2_entry.get())
    y2 = float(y2_entry.get())
    z2 = float(z2_entry.get())

    x3 = float(x3_entry.get())
    y3 = float(y3_entry.get())
    z3 = float(z3_entry.get())

    level = int(level_entry.get())

    terrain(x1, y1, z1, x2, y2, z2, x3, y3, z3, level)
    main()


def terrain(x1, y1, z1, x2, y2, z2, x3, y3, z3, level):
    global TRIANGLES
    global count
    count +=1

    mx1 = (x1 + x2) / 2
    my1 = (y1 + y2) / 2

    mx2 = (x2 + x3) / 2
    my2 = (y2 + y3) / 2

    mx3 = (x3 + x1) / 2
    my3 = (y3 + y1) / 2

    if count == 1:
        mz1 = float("{:.2f}".format(random.uniform(-1, 1)))
        mz2 = float("{:.2f}".format(random.uniform(-1, 1)))
        mz3 = float("{:.2f}".format(random.uniform(-1, 1)))
    else:
        mz1 = ((z1 + z2) / 2) + (.1 * -level)
        mz2 = ((z2 + z3) / 2) + (.1 * -level)
        mz3 = ((z3 + z1) / 2) + (.1 * -level)

    if level > 1:
        TRIANGLES = TRIANGLES[:-1]

        # With Random Z displacement

        # Triangle 1
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((mx1, my1, mz1))
        VERTICES.append((mx2, my2, mz2))
        VERTICES.append((mx3, my3, mz3))
        terrain(mx1, my1, mz1, mx2, my2, mz2, mx3, my3, mz3, level - 1)

        # Triangle 2
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((mx1, my1, mz1))
        VERTICES.append((mx2, my2, mz2))
        VERTICES.append((x2, y2, z2))
        terrain(mx1, my1, mz1, mx2, my2, mz2, x2, y2, z2, level - 1)

        # Triangle 3
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((mx1, my1, mz1))
        VERTICES.append((mx3, my3, mz3))
        VERTICES.append((x1, y1, z1))
        terrain(mx1, my1, mz1, mx3, my3, mz3, x1, y1, z1, level - 1)

        # Triangle 4
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((mx2, my2, mz2))
        VERTICES.append((mx3, my3, mz3))
        VERTICES.append((x3, y3, z3))
        terrain(mx2, my2, mz2, mx3, my3, mz3, x3, y3, z3, level - 1)

    elif level == 1 and count == 1:
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((mx1, my1, mz1))
        VERTICES.append((mx2, my2, mz2))
        VERTICES.append((mx3, my3, mz3))

    else:
        TRIANGLES.append((len(VERTICES), len(VERTICES) + 1, len(VERTICES) + 2))
        VERTICES.append((x1, y1, z1))
        VERTICES.append((x2, y2, z2))
        VERTICES.append((x3, y3, z3))

    return VERTICES, TRIANGLES


def transform(x, y, z, angle, tilt):
    # Animation control (around y-axis). If considered as a view of earth from space, it's moving over the equator.
    s, c = math.sin(angle), math.cos(angle)
    x, z = x * c - z * s, x * s + z * c

    # Camera tilt  (around x-axis). If considered as a view of earth from space, the tilt angle is measured from the equator.
    s, c = math.sin(tilt), math.cos(tilt)
    y, z = y * c - z * s, y * s + z * c

    # Setting up View Parameters
    z += 5  # Fixed Distance from top
    FOV = 1000  # Fixed Field of view
    f = FOV / z
    sx, sy = x * f, y * f
    return sx, sy


def main():
    # Creates terrain using turtle
    terrain = turtle.Turtle()
    terrain.pencolor("pink")
    terrain.pensize(2)
    turtle.bgcolor("dark blue")
    turtle.penup()
    turtle.pencolor("red")
    turtle.goto(350, -350)
    turtle.write("Terrain Generated", align="right", font="Arial 24 normal")

    # Turn off move time for instant drawing
    turtle.tracer(0, 0)
    terrain.up()
    angle = 0

    while True:
        # Clear the screen
        terrain.clear()

        # Transform the terrain
        VERT2D = []
        for vert3D in VERTICES:
            x, y, z = vert3D
            sx, sy = transform(x, y, z, angle, .25)
            VERT2D.append((sx, sy))

        # Draw the terrain
        for triangle in TRIANGLES:
            points = []
            points.append(VERT2D[triangle[0]])
            points.append(VERT2D[triangle[1]])
            points.append(VERT2D[triangle[2]])

            # Draw the trangle
            terrain.goto(points[0][0], points[0][1])
            terrain.down()

            terrain.goto(points[1][0], points[1][1])
            terrain.goto(points[2][0], points[2][1])
            terrain.goto(points[0][0], points[0][1])
            terrain.up()

        # Update screen
        turtle.update()

        # Control the speed of animation
        angle += 0.0085


if __name__ == '__main__':
    window = Tk()
    window.title("Terrain Generator")
    window.geometry("500x500")
    title = Label(window, text="Terrain Generator", bg="gray", font="times 12 bold")
    title.grid(row=1, column=2)

    prompt = Label(window, text="Enter vertices in 'XYZ' format and recursion level", bg="red", font="times 12 bold")
    prompt.grid(row=2, column=2)

    x1 = Label(window, text="Triangle 1 (x-value):", bg="light blue", font="times 12 bold")
    x1.grid(row=3, column=1)
    x1_entry = Entry(window)
    x1_entry.grid(row=3, column=2)

    y1 = Label(window, text="Triangle 1 (y-value):", bg="light blue", font="times 12 bold")
    y1.grid(row=4, column=1)
    y1_entry = Entry(window)
    y1_entry.grid(row=4, column=2)

    z1 = Label(window, text="Triangle 1 (z-value):", bg="light blue", font="times 12 bold")
    z1.grid(row=5, column=1)
    z1_entry = Entry(window)
    z1_entry.grid(row=5, column=2)

    x2 = Label(window, text="Triangle 2 (x-value):", bg="light green", font="times 12 bold")
    x2.grid(row=6, column=1)
    x2_entry = Entry(window)
    x2_entry.grid(row=6, column=2)

    y2 = Label(window, text="Triangle 2 (y-value):", bg="light green", font="times 12 bold")
    y2.grid(row=7, column=1)
    y2_entry = Entry(window)
    y2_entry.grid(row=7, column=2)

    z2 = Label(window, text="Triangle 2 (z-value):", bg="light green", font="times 12 bold")
    z2.grid(row=8, column=1)
    z2_entry = Entry(window)
    z2_entry.grid(row=8, column=2)

    x3 = Label(window, text="Triangle 3 (x-value):", bg="pink", font="times 12 bold")
    x3.grid(row=9, column=1)
    x3_entry = Entry(window)
    x3_entry.grid(row=9, column=2)

    y3 = Label(window, text="Triangle 3 (y-value):", bg="pink", font="times 12 bold")
    y3.grid(row=10, column=1)
    y3_entry = Entry(window)
    y3_entry.grid(row=10, column=2)

    z3 = Label(window, text="Triangle 3 (z-value):", bg="pink", font="times 12 bold")
    z3.grid(row=11, column=1)
    z3_entry = Entry(window)
    z3_entry.grid(row=11, column=2)

    level = Label(window, text="Recursion Level:", bg="orange", font="times 12 bold")
    level.grid(row=12, column=1)
    level_entry = Entry(window)
    level_entry.grid(row=12, column=2)

    show_turtle = Button(window, text="Show Turtle", bg="purple", font="times 14 bold", command=parameters)
    show_turtle.grid(row=14, column=2)

    window.mainloop()
