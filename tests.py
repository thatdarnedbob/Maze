import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        m2 = Maze(400, 400, 100, 100, 10, 10)
        self.assertEqual(len(m2._cells), len(m2._cells[0]))

    def test_create_maze_exits(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()

        self.assertEqual(m1._cells[0][0].walls[0], False)
        self.assertEqual(m1._cells[num_cols-1][num_rows-1].walls[1], False)
        
if __name__ == "__main__":
    # print("doin")
    unittest.main()
