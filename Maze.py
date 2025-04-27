from Geometry import *
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []

        for j in range(self._num_cols):
            next_col = []
            for i in range(self._num_rows):
                tl_corner = Point(self._x1 + j * self._cell_size_x,
                                  self._y1 + i * self._cell_size_y)
                br_corner = Point(self._x1 + (j + 1) * self._cell_size_x,
                                  self._y1 + (i + 1) * self._cell_size_y)
                walls = [True, True, True, True]
                next_cell = Cell(tl_corner, br_corner, self._win, walls)
                next_col.append(next_cell)
            self._cells.append(next_col)
        
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._win is None:
            return
        self._cells[col][row].draw()
        self._animate()
    
    def _animate(self):
        if self._win:
            self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls[0] = False
        self._cells[0][0].draw()
        self._cells[self._num_cols - 1][self._num_rows - 1].walls[1] = False
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()