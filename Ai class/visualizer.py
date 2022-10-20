import turtle
from aStar import a_star
from theta_star import theta_star

# setup
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(800, 800)
screen.title("A*-Family Pathfinding Algorithm Visualizer")
trtl = turtle.Turtle()
GOAL = "green"
START = "red"
POINT_RADIUS = 2


# param x: size of x-axis
# param y: size of y-axis
# return: draws the grid
def getXY(coordinates):
    x, y = map(int, coordinates.split(' '))
    return x, y


def draw_grid(x, y):
    screen.setworldcoordinates(0, y + 2, x + 2, 0)
    trtl.up()
    trtl.pensize(1)
    trtl.color('grey')
    for val in range(1, x + 2):
        trtl.setpos(val, 1)
        trtl.down()
        trtl.goto(val, y + 1)
        trtl.up()

    for val in range(1, y + 2):
        trtl.setpos(1, val)
        trtl.down()
        trtl.goto(x + 1, val)
        trtl.up()


# param point_type: type of point (start/goal) dictates color of point
# param coordinates: string of coordinate to be marked as a point
# return:
def set_point(point_type, coordinates):
    x, y = getXY(coordinates)
    trtl.color(point_type)
    trtl.setpos(x, y - POINT_RADIUS)
    trtl.begin_fill()
    trtl.circle(POINT_RADIUS)
    trtl.end_fill()
    trtl.up()


# param: tuple of coordinates of filled cells
# return: fills in all cells that are blocked
def fill_cells(coordinates):
    x, y, z = map(int, coordinates.split(' '))
    if z != 1:
        return
    trtl.color('grey')
    trtl.setpos(x, y + 1)
    trtl.begin_fill()
    for x in range(4):
        trtl.forward(1)
        trtl.right(90)
    trtl.end_fill()


# param: tuple of start coordinates, goal coordinates, grid dimensions, and all filled cells
# return: draws the grid with all data
def draw_board(data):
    turtle.tracer(0, 0)
    x, y = getXY(data[2])
    draw_grid(x, y)
    for i in data[3]:
        fill_cells(i)
    set_point(START, data[0])
    set_point(GOAL, data[1])
    trtl.hideturtle()
    turtle.update()


# param: absolute filepath
# return: tuple containing start coordinates, goal coordinates, grid dimensions, and list of all filled cells
def load_data(filepath):
    with open(filepath, 'r') as f:
        start = f.readline().strip()
        goal = f.readline().strip()
        dim = f.readline().strip()
        fill = []
        for l in f:
            fill.append(l[:-1])
    return (start, goal, dim, fill)


def draw_path(path):
    turtle.tracer(1)
    trtl.speed(3)
    x, y = map(int, path[0])
    trtl.setpos(x, y)
    trtl.down()
    trtl.color('blue')
    trtl.pensize(3)

    for c in path:
        x, y = map(int, c)
        print(str(x) + ' ' + str(y) + '\n')
        trtl.goto(x, y)


# def solve(data):


# main execution
data = load_data('sample.txt')
draw_board(data)
choice= input("Write a if you want to run A* or if you want to run Theta* type t:")
if choice == 'a':
    star_a = a_star('sample.txt')
    draw_path(star_a.answer)
    print(star_a.runtime, "seconds")


elif choice == 't':
    star_theta = theta_star('sample.txt')
    draw_path(star_theta.answer)
    print(star_theta.runtime," seconds")

else:
    print("Invalid Input")



screen.mainloop()

