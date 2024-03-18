from tkinter import Tk, BOTH, Canvas
import time
from .classline import Line
from .classpoint import Point

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
            time.sleep(0.01) # delay to improve CPU usage

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)