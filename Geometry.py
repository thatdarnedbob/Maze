class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, begin, end, width=3):
        self.begin = begin
        self.end = end
        self.width = width

    def draw(self, canvas, fill_c):
        canvas.create_line(self.begin.x, self.begin.y,
                           self.end.x, self.end.y,
                           fill=fill_c, width=self.width)

class Cell:
    def __init__(self, tl_corner, br_corner, window=None, walls=[True, True, True, True]):
        self.walls = walls
        # walls format: top, bottom, left, right
        self._top_left_corner = tl_corner
        self._bottom_right_corner = br_corner

        self._top_right_corner = Point(self.x2(), self.y1())
        self._bottom_left_corner = Point(self.x1(), self.y2())
        self._win = window
        self._visited = False
    
    def x1(self):
        return self._top_left_corner.x
    def x2(self):
        return self._bottom_right_corner.x
    def y1(self):
        return self._top_left_corner.y
    def y2(self):
        return self._bottom_right_corner.y
    def center_point(self):
        return Point(0.5 * (self.x1() + self.x2()),
                     0.5 * (self.y1() + self.y2()))

    def draw(self):
        if self._win is None:
            return
        if(self.walls[0]):
            self._win.draw_line(Line(self._top_left_corner, self._top_right_corner), "black")
        else:
            self._win.draw_line(Line(self._top_left_corner, self._top_right_corner), "white")
        if(self.walls[1]):
            self._win.draw_line(Line(self._bottom_left_corner, self._bottom_right_corner), "black")
        else:
            self._win.draw_line(Line(self._bottom_left_corner, self._bottom_right_corner), "white")
        if(self.walls[2]):
            self._win.draw_line(Line(self._top_left_corner, self._bottom_left_corner), "black")
        else:
            self._win.draw_line(Line(self._top_left_corner, self._bottom_left_corner), "white")
        if(self.walls[3]):
            self._win.draw_line(Line(self._top_right_corner, self._bottom_right_corner), "black")
        else:
            self._win.draw_line(Line(self._top_right_corner, self._bottom_right_corner), "white")
        return
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo:
            c = "gray"
        else:
            c = "red"
        self._win.draw_line(Line(self.center_point(), to_cell.center_point(), width = 2), c)