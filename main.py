from Window import Window
from Geometry import Point, Line

def main():
    win = Window(800, 600)

    L1 = Line(Point(0,0), Point(200,200))
    L2 = Line(Point(200,0), Point(0,200))
    L3 = Line(Point(200,0), Point(200,200))
    L4 = Line(Point(200,200), Point(0,200))
    for line in [L1, L2, L3, L4]:
        win.draw_line(line, "black")
    win.wait_for_close()

if __name__ == "__main__":
    main()