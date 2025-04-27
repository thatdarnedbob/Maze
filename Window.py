from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_c):
        line.draw(self.canvas, fill_c)