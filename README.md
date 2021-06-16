# Sierpinski Triangle on Python
## _A simple implementation of Sierpinski's triangle in Python and the turtle module with random figure generation_

How it run:
`` ''
from sierpinski_triangle import build

build(t_coord: tuple = TEMP_COORD,
        rand: bool = True,
        quanity: int = 3,
        koef: int = 1,
        iterations: int = 2000,
        speed: int = 100,
        vision: bool = 0)
`` ''
![N|Solid](https://raw.githubusercontent.com/di2mot/Sierpinski-Triangle/main/sierpinski_triangle.png)


[Sierpinski Triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle "Wikipedia") also called the Sierpiński gasket or Sierpiński sieve, is a fractal attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets—that is, it is a mathematically generated pattern that is reproducible at any magnification or reduction. It is named after the Polish mathematician Wacław Sierpiński, but appeared as a decorative pattern many centuries before the work of Sierpiński.


How to use:
Two input options are supported, actually three. In the first case, if the 'rand' variable = True, the points will be set automatically.
If you want to set it manually, you can either write it in the script body, indicate coordinates of points and add new points if necessary. 
Or just click on the screen. Where you click, there will be points. To do this you need to set 'rand' = False.
To set the number of entered points, change the QUANTITY variable.
KOEF - line segment ratio, 1/1 as 1, 1/2 as 0.5
ITERATIONS - number of iterations
SPEED -speed of turtl
vision: If you don't want to see the points added, 
        use the False flag. With the False flag, 
        the rendering is almost instantaneous.

## License

WTFPL Version 2

**Free Software, Hell Yeah!**
