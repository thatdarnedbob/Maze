from Window import Window
from Geometry import *
from Maze import Maze

def main():
    win = Window(800, 600)

    maze_test(win)
    
    win.wait_for_close()

def maze_test(win):
    maze = Maze(10, 10, 3, 8, 40, 40, win)
    maze._break_entrance_and_exit()
    maze._animate()

def basic_cell_test(win):
    A1, A2 = Point(10,10), Point(50,50)
    Awalls = [True, True, True, True]

    B1, B2 = Point(410,10), Point(450, 50)
    Bwalls = [True, True, False, False]
    
    C1, C2 = Point(410,410), Point(450, 450)
    Cwalls = [False, False, True, True]

    D1, D2 = Point(10, 410), Point(50, 450)
    Dwalls = [False, True, False, False]

    Acell = Cell(A1, A2, win, Awalls)
    Bcell = Cell(B1, B2, win, Bwalls)
    Ccell = Cell(C1, C2, win, Cwalls)
    Dcell = Cell(D1, D2, win, Dwalls)

    for cell in [Acell, Bcell, Ccell, Dcell]:
        cell.draw()
    Bcell.draw_move(Ccell, False)
    Ccell.draw_move(Dcell, True)

def basic_line_test(win):
    L1 = Line(Point(0,0), Point(200,200))
    L2 = Line(Point(200,0), Point(0,200))
    L3 = Line(Point(200,0), Point(200,200))
    L4 = Line(Point(200,200), Point(0,200))
    for line in [L1, L2, L3, L4]:
        win.draw_line(line, "black")

if __name__ == "__main__":
    main()