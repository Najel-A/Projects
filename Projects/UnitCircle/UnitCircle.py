import matplotlib.pyplot as plt
import math
from matplotlib.legend import Legend


# Functions
def create_circle():
    circle = plt.Circle((0, 0), radius=1, color="black")
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.title("Unit Circle Graph",fontsize="24",color="white")
    plt.axis('scaled')
    ax.set_facecolor((1.0, .47, .42))
    #plt.axis()
    plt.ylabel("Y-Coordinates",fontsize="24")
    plt.xlabel("X-Coordinates",fontsize="24")
    plt.show()


# Background Color
plt.figure().patch.set_facecolor("magenta")

# Horizontal Line
x = [-1, 1]
y = [0, 0]
plt.plot(x, y, color="white")

# Vertical Line
x1 = [0, 0]
y1 = [-1, 1]
plt.plot(x1, y1, color="white")

# Points
origin = [0, 0]
point1 = [math.sqrt(3) / 2, 1 / 2]
point2 = [1 / math.sqrt(2), 1 / math.sqrt(2)]
point3 = [1 / 2, math.sqrt(3) / 2]

point4 = [-math.sqrt(3) / 2, 1 / 2]
point5 = [-1 / math.sqrt(2), 1 / math.sqrt(2)]
point6 = [-1 / 2, math.sqrt(3) / 2]

point7 = [-math.sqrt(3) / 2, -1 / 2]
point8 = [-1 / math.sqrt(2), -1 / math.sqrt(2)]
point9 = [-1 / 2, -math.sqrt(3) / 2]

point10 = [math.sqrt(3) / 2, -1 / 2]
point11 = [1 / math.sqrt(2), -1 / math.sqrt(2)]
point12 = [1 / 2, -math.sqrt(3) / 2]

# Quadrant 1
line1x = [origin[0], point1[0]]
line1y = [origin[1], point1[1]]
first_line = [line1x, line1y]

line2x = [origin[0], point2[0]]
line2y = [origin[1], point2[1]]

line3x = [origin[0], point3[0]]
line3y = [origin[1], point3[1]]

plt.plot(line1x, line1y, color="blue", ls="dashed")
plt.plot(line2x, line2y, color="blue", ls="dashed")
plt.plot(line3x, line3y, color="blue", ls="dashed")
# Quadrant 2
line4x = [origin[0], point4[0]]
line4y = [origin[1], point4[1]]

line5x = [origin[0], point5[0]]
line5y = [origin[1], point5[1]]

line6x = [origin[0], point6[0]]
line6y = [origin[1], point6[1]]

plt.plot(line4x, line4y, color="red", ls="dashed")
plt.plot(line5x, line5y, color="red", ls="dashed")
plt.plot(line6x, line6y, color="red", ls="dashed")

# Quadrant 3
line7x = [origin[0], point7[0]]
line7y = [origin[1], point7[1]]

line8x = [origin[0], point8[0]]
line8y = [origin[1], point8[1]]

line9x = [origin[0], point9[0]]
line9y = [origin[1], point9[1]]

plt.plot(line7x, line7y, color="green", ls="dashed")
plt.plot(line8x, line8y, color="green", ls="dashed")
plt.plot(line9x, line9y, color="green", ls="dashed")
# Quadrant 4
line10x = [origin[0], point10[0]]
line10y = [origin[1], point10[1]]

line11x = [origin[0], point11[0]]
line11y = [origin[1], point11[1]]

line12x = [origin[0], point12[0]]
line12y = [origin[1], point12[1]]

plt.plot(line10x, line10y, color="yellow", ls="dashed")
plt.plot(line11x, line11y, color="yellow", ls="dashed")
plt.plot(line12x, line12y, color="yellow", ls="dashed")

# Legend
plt.plot([point1[0]], label="            KEY     ")
plt.plot([point1[0]], label=" ")

plt.plot([point1[0]], label="Quadrant 1", color="blue")
plt.plot([point4[0]], label="Quadrant 2", color="red")
plt.plot([point7[0]], label="Quadrant 3", color="green")
plt.plot([point10[0]], label="Quadrant 4", color="yellow")

plt.plot([point1[0]], label=" ")

plt.plot([point1[0]], label="π/6 at (√3/2, 1/2)")
plt.plot([point1[0]], label="π/4 at (√3/2, 1/2)")
plt.plot([point1[0]], label="π/3 at (√3/2, 1/2)")

plt.plot([point1[0]], label=" ")

plt.plot([point1[0]], label="2π/3 at (√3/2, 1/2)")
plt.plot([point1[0]], label="3π/4 at (√3/2, 1/2)")
plt.plot([point1[0]], label="5π/6 at (√3/2, 1/2)")

plt.plot([point1[0]], label=" ")

plt.plot([point1[0]], label="7π/6 at (√3/2, 1/2)")
plt.plot([point1[0]], label="5π/4 at (√3/2, 1/2)")
plt.plot([point1[0]], label="4π/3 at (√3/2, 1/2)")

plt.plot([point1[0]], label=" ")

plt.plot([point1[0]], label="5π/3 at (√3/2, 1/2)")
plt.plot([point1[0]], label="7π/4 at (√3/2, 1/2)")
plt.plot([point1[0]], label="11π/6 at (√3/2, 1/2)")

legend = plt.legend(bbox_to_anchor=(1, 1), loc="upper left", handlelength=0, handletextpad=-.2, facecolor="black",
                    framealpha=1)
color_lines = ["white", "black", "blue", "red", "green", "yellow", "black", "blue", "blue", "blue", "black", "red",
               "red", "red", "black", "green", "green", "green", "black", "yellow", "yellow", "yellow"]
for n, text in enumerate(legend.texts):
    print(n, text)
    text.set_color(color_lines[n])

# Points Plot
plt.plot(point1[0], point1[1], "ro", markersize=4.5, color="cyan")
plt.plot(point2[0], point2[1], "ro", markersize=4.5, color="cyan")
plt.plot(point3[0], point3[1], "ro", markersize=4.5, color="cyan")

plt.plot(point4[0], point4[1], "ro", markersize=4.5, color="cyan")
plt.plot(point5[0], point5[1], "ro", markersize=4.5, color="cyan")
plt.plot(point6[0], point6[1], "ro", markersize=4.5, color="cyan")

plt.plot(point7[0], point7[1], "ro", markersize=4.5, color="cyan")
plt.plot(point8[0], point8[1], "ro", markersize=4.5, color="cyan")
plt.plot(point9[0], point9[1], "ro", markersize=4.5, color="cyan")

plt.plot(point10[0], point10[1], "ro", markersize=4.5, color="cyan")
plt.plot(point11[0], point11[1], "ro", markersize=4.5, color="cyan")
plt.plot(point12[0], point12[1], "ro", markersize=4.5, color="cyan")

# Draw Graph
show_shape(create_circle())
