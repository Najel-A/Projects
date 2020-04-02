import matplotlib.pyplot as plt
import math


# Functions
def create_circle():
    circle = plt.Circle((0, 0), radius=1, color="black")
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()


plt.title("Unit Circle")
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



show_shape(create_circle())
plt.show()
