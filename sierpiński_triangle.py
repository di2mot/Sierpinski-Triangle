import turtle
from random import choice, randint
from fractions import Fraction

# CONSTANTS:

# A = (x, y)
# To set the triangle placement range. Can be set manually
A = (randint(-350, 350), randint(100, 350))

B = (randint(-350, 100), randint(-350, 100))

C = (randint(100, 350), randint(-350, 100))

COORDINATE = (A, B, C)

# KOEF  = 1/1 as 1, or you can use like 1/2 as 0.5
KOEF = Fraction(1, 1)

# first point
TEMP_COORD = [randint(0, 200), randint(0, 200)]

# speed of turtle
SPEED = 100

# number of iterations
ITERATION = 2000

# Main script
t = turtle.Turtle()
t.speed(SPEED)
t.up()  # In order not to leave a mark

def make_points(t):

    for POINT in COORDINATE:
        t.goto(POINT)
        t.dot(5, 'red')
    t.goto(TEMP_COORD)
    t.dot(5, 'yellow')


def add_point(t, TEMP_COORD):
    '''
    Xm = Xa + k*Xb / 1 + k
    Ym = Ya + k*Xb / 1 + k
    '''
    TEMP = TEMP_COORD
    for i in range(2000):

        ABC = choice(COORDINATE)

        NEW_X = (TEMP[0] + KOEF * ABC[0]) / (1 + KOEF)
        NEW_Y = (TEMP[1] + KOEF * ABC[1]) / (1 + KOEF)

        TEMP = [NEW_X, NEW_Y]

        t.goto(NEW_X, NEW_Y)
        t.dot(3)


def run(t, TEMP_COORD):
    make_points(t)
    add_point(t, TEMP_COORD)

    # click to exit
    turtle.exitonclick()


if __name__ == '__main__':
    run(t, TEMP_COORD)
