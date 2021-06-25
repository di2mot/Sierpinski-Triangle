import turtle
from tkinter import _tkinter
from random import choice, randint


# CONSTANTS:

# A = (x, y)



# If you write the coordinates manually, add them to this list
COORDINATE = []

COORD = []

# first point
first_dot = (randint(0, 200), randint(0, 200))

exit_text = 'Premature program close'
errore_text = "Something's gone wrong."

def make_points_random(t, quanity, first_dot):
    # generate points
    for i in range(quanity):
        COORDINATE.append((randint(-350, 350), randint(100, 350)))

    # To set points random
    for POINT in COORDINATE:
        t.goto(POINT)
        t.dot(5, 'red')
    t.goto(first_dot)
    t.dot(5, 'yellow')


def make_points(t, quanity, point_color):

    # To set points manually
    while len(COORD) < quanity:
        turtle.onscreenclick(clic)
        t.home()

    for i in COORD:
        t.up()
        t.goto(i[0], i[1])
        t.dot(10, 'red')

    t.goto(first_dot)
    t.dot(5, point_color)


def clic(x, y):
    COORD.append([x, y])


def add_point(t, first_dot, koef, iterations, dot_color, vision):
    '''
    Sets a new point between the old point and a random vertex of the triangle.

    Xm = Xa + k*Xb / 1 + k
    Ym = Ya + k*Xb / 1 + k
    '''

    if not vision:
        turtle.title(f'number of points = {iterations}')
        turtle.tracer(0, 0)

    TEMP = first_dot
    for i in range(iterations):

        # If the COORD list is empty, it will select COORDINATE
        if len(COORD) != 0:
            ABC = choice(COORD)

        else:
            ABC = choice(COORDINATE)

        NEW_X = (TEMP[0] + koef * ABC[0]) / (1 + koef)
        NEW_Y = (TEMP[1] + koef * ABC[1]) / (1 + koef)

        TEMP = [NEW_X, NEW_Y]

        t.goto(NEW_X, NEW_Y)
        t.dot(3, dot_color)

        # Updates the point counter in the header
        if vision:
            turtle.title(f'number of points = {i}')


def build(first_dot: tuple = first_dot,
          rand: bool = True,
          quanity: int = 3,
          koef: int = 1,
          iterations: int = 2000,
          speed: int = 100,
          vision: bool = True,
          dot_color: str = 'black',
          point_color: str = 'yellow'):
    '''
    Function for starting script

    first_dot:  coordinate of the first dot, (x, y)
    rand: If you need to randomly place points: rand = True
    quanity:  the number of points that click on the screen, use ven rand=False
    koef:  line segment ratio, 1/1 as 1, 1/2 as 0.5
    iterations:  number of iterationss
    speed: speed of turtle
    vision: If you don't want to see the points added, 
            use the False flag. With the False flag, 
            the rendering is almost instantaneous.

    '''
    # Main script
    t = turtle.Turtle()

    t.up()  # In order not to leave a mark
    t.ht()  # make turtle invisibl
    canvas = turtle.getcanvas()
    t.speed(speed)

    #if not vision:
        #turtle.tracer(0, 0)

    if rand:
        make_points_random(t, quanity, first_dot)
    else:
        make_points(t, quanity, point_color)

    # it`s add point
    # and for closing th window
    try:
        add_point(t, first_dot, koef, iterations, dot_color, vision)
        turtle.update()
        # click to exit
        turtle.exitonclick()

    except turtle.Terminator as errore:
        print(exit_text, errore)
    except _tkinter.TclError:
        print(exit_text)
    except Exception as errore:
        print(errore_text, errore)

if __name__ == '__main__':
    build()
