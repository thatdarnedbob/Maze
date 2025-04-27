from Geometry import *

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win):
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
                next_cell.draw()
            self._cells.append(next_col)

        