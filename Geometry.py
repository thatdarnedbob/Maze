class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def draw(self, canvas, fill_c):
        canvas.create_line(self.begin.x, self.begin.y,
                           self.end.x, self.end.y,
                           fill=fill_c, width=2)

class Cell:
    def __init__(self, tl_corner, br_corner, window, walls=[True, True, True, True]):
        self.walls = walls
        # walls format: top, bottom, left, right
        self._top_left_corner = tl_corner
        self._bottom_right_corner = br_corner

        self._top_right_corner = Point(self.x2(), self.y1())
        self._bottom_left_corner = Point(self.x1(), self.y2())
        self._win = window
    
    def x1(self):
        return self._top_left_corner.x
    def x2(self):
        return self._bottom_right_corner.x
    def y1(self):
        return self._top_left_corner.y
    def y2(self):
        return self._bottom_right_corner.y

    def draw(self):
        if(self.walls[0]):
            self._win.draw_line(Line(self._top_left_corner, self._top_right_corner), "black")
        if(self.walls[1]):
            self._win.draw_line(Line(self._bottom_left_corner, self._bottom_right_corner), "black")
        if(self.walls[2]):
            self._win.draw_line(Line(self._top_left_corner, self._bottom_left_corner), "black")
        if(self.walls[3]):
            self._win.draw_line(Line(self._top_right_corner, self._bottom_right_corner), "black")
        return
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            c = "gray"
        else:
            c = "red"
        self._win.draw_line(Line(Point(0.5 * (self.x1() + self.x2()),
                                       0.5 * (self.y1() + self.y2())),
                                Point(0.5 * (to_cell.x1() + to_cell.x2()),
                                       0.5 * (to_cell.y1() + to_cell.y2()))),
                            c)