from Geometry import *
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

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
        self._animate(0.005)
    
    def _animate(self, delay=0.025):
        if self._win:
            self._win.redraw()
            time.sleep(delay)

    def _break_entrance_and_exit(self):
        self._cells[0][0].walls[0] = False
        self._cells[0][0].draw()
        self._cells[self._num_cols - 1][self._num_rows - 1].walls[1] = False
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()

    def _break_walls(self, row, col):
        curr_cell = self._cells[col][row]
        curr_cell._visited = True

        while True:
            to_visit = []
            neighbors = self._neighbors_of(row, col)
            for cell in neighbors:
                if not cell[2]._visited:
                    to_visit.append((cell[0], cell[1]))
            if len(to_visit) == 0:
                curr_cell.draw()
                return
            else:
                cc = to_visit[random.randint(0,len(to_visit) - 1)]
                if cc[0] == -1:
                    curr_cell.walls[0] = False
                    self._cells[col][row - 1].walls[1] = False
                    curr_cell.draw()
                    self._cells[col][row - 1].draw()
                    self._break_walls(row - 1, col)
                    self._animate(0.025)
                if cc[0] == 1:
                    curr_cell.walls[1] = False
                    self._cells[col][row + 1].walls[0] = False
                    curr_cell.draw()
                    self._cells[col][row + 1].draw()
                    self._break_walls(row + 1, col)
                    self._animate(0.025)
                if cc[1] == -1:
                    curr_cell.walls[2] = False
                    self._cells[col - 1][row].walls[3] = False
                    curr_cell.draw()
                    self._cells[col - 1][row].draw()
                    self._break_walls(row, col - 1)
                    self._animate(0.025)
                if cc[1] == 1:
                    curr_cell.walls[3] = False
                    self._cells[col + 1][row].walls[2] = False
                    curr_cell.draw()
                    self._cells[col + 1][row].draw()
                    self._break_walls(row, col + 1)
                    self._animate(0.025)

    
    def _neighbors_of(self, row, col):
        neighbors = []
        if row > 0 and row < self._num_rows and col >= 0 and col < self._num_cols:
            neighbors.append((-1, 0, self._cells[col][row - 1])) # above
        if row >= 0 and row < self._num_rows - 1 and col >= 0 and col < self._num_cols:
            neighbors.append((1, 0, self._cells[col][row + 1])) # below
        if row >= 0 and row < self._num_rows and col > 0 and col < self._num_cols:
            neighbors.append((0, -1, self._cells[col - 1][row])) # left
        if row >= 0 and row < self._num_rows and col >= 0 and col < self._num_cols - 1:
            neighbors.append((0, 1, self._cells[col + 1][row])) # right
        return neighbors
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False