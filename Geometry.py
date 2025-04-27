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
