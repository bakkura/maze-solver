from tkinter import Tk, BOTH, Canvas
import time

def main():
    # this code creates the window
    win = Window(800, 600)

    maze = Maze(50, 50, 5, 5, 100, 100, win)
    maze._create_cells()
    maze._break_entrance_and_exit()

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
                 win=None, 
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
        true_color = "black"
        false_color = "#d9d9d9"
        # variables for left wall line
        lw_point1 = Point(self.x1, self.y1)
        lw_point2 = Point(self.x1, self.y2)
        lw_line = Line(lw_point1, lw_point2)
        # variables for right wall line
        rw_point1 = Point(self.x2, self.y1)
        rw_point2 = Point(self.x2, self.y2)
        rw_line = Line(rw_point1, rw_point2)
        # variables for top wall
        tw_point1 = Point(self.x1, self.y1)
        tw_point2 = Point(self.x2, self.y1)
        tw_line = Line(tw_point1, tw_point2)
        # variables for bottom wall
        bw_point1 = Point(self.x1, self.y2)
        bw_point2 = Point(self.x2, self.y2)
        bw_line = Line(bw_point1, bw_point2)
        # if/else statements to draw lines of correct color
        if self.left_wall:
            self.win.draw_line(lw_line, true_color)
        else:
            self.win.draw_line(lw_line, false_color)
        if self.right_wall:
            self.win.draw_line(rw_line, true_color)
        else:
            self.win.draw_line(rw_line, false_color)            
        if self.top_wall:
            self.win.draw_line(tw_line, true_color)
        else:
            self.win.draw_line(tw_line, false_color)            
        if self.bottom_wall:
            self.win.draw_line(bw_line, true_color)
        else:
            self.win.draw_line(bw_line, false_color)

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

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if self.num_rows < 1 or self.num_cols < 1:
            raise ValueError("There must be at least 1 row and 1 column in a maze.")
        self._create_cells()
        if self.win:
            self._draw_all_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column_i = []
            for j in range(self.num_rows):
                cell_x1 = self.x1 + (self.cell_size_x * i)
                cell_y1 = self.y1 + (self.cell_size_y * j)
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y
                column_i.append(Cell(cell_x1, cell_y1, cell_x2, cell_y2, self.win))
            self._cells.append(column_i)


    def _draw_all_cells(self):
        for i, column in enumerate(self._cells):
            for j, cell in enumerate(column):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        # self._cells[i][j] is the cell class object we're drawing
        self._cells[i][j].draw()
        # calculates where the maze starts
        # draw the cell and animate it
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False
        if self.win:
            self._draw_entrance_and_exit()

    def _draw_entrance_and_exit(self):
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

if __name__ == "__main__":
    main()