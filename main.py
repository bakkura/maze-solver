from tkinter import Tk, BOTH, Canvas
import time
from src.classwindow import Window
from src.classpoint import Point
from src.classline import Line

def main():
    # this code creates the window
    win = Window(800, 600)

    # example points to test point class
    point1 = Point(50, 50)
    point2 = Point(150, 150)

    # using above points to create line
    line = Line(point1, point2)

    # use window class method to draw above line
    win.draw_line(line, "red")

    # this code keeps the window open
    win.wait_for_close()

main()

