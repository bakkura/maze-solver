from tkinter import Tk, BOTH, Canvas
import time

def main():
    # this code creates the window
    win = Window(800, 600)

    cell = Cell(50, 50, 150, 150, win, False, True, True, True)
    cell.draw()

    cell2 = Cell(160, 200, 250, 210, win)
    cell2.draw()

    cell.draw_move(cell2, False)

    # this code keeps the window open
    win.wait_for_close()

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

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, 
                 x1, 
                 y1, 
                 x2, 
                 y2, 
                 win, 
                 left_wall=True, 
                 right_wall=True, 
                 top_wall=True, 
                 bottom_wall=True
                 ):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall

    def draw(self):
        if self.left_wall:
            lw_point1 = Point(self.x1, self.y1)
            lw_point2 = Point(self.x1, self.y2)
            lw_line = Line(lw_point1, lw_point2)
            self.win.draw_line(lw_line, "black")
        if self.right_wall:
            rw_point1 = Point(self.x2, self.y1)
            rw_point2 = Point(self.x2, self.y2)
            rw_line = Line(rw_point1, rw_point2)
            self.win.draw_line(rw_line, "black")
        if self.top_wall:
            tw_point1 = Point(self.x1, self.y1)
            tw_point2 = Point(self.x2, self.y1)
            tw_line = Line(tw_point1, tw_point2)
            self.win.draw_line(tw_line, "black")
        if self.bottom_wall:
            bw_point1 = Point(self.x1, self.y2)
            bw_point2 = Point(self.x2, self.y2)
            bw_line = Line(bw_point1, bw_point2)
            self.win.draw_line(bw_line, "black")

    def draw_move(self, to_cell, undo=False):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        center = Point(center_x, center_y)
        center_x_to_cell = (to_cell.x1 + to_cell.x2) / 2
        center_y_to_cell = (to_cell.y1 + to_cell.y2) / 2
        center_to_cell = Point(center_x_to_cell, center_y_to_cell)
        center_to_center = Line(center, center_to_cell)
        if not undo:
            self.win.draw_line(center_to_center, "red")
        elif undo:
            self.win.draw_line(center_to_center, "gray")


        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

main()