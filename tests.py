import unittest
from main import Maze

class Tests(unittest.TestCase):
    # logic only tests
    # test for maze method create cells
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

    # tests for different maze dimensions
    def test_maze_different_dimensions(self):
        num_cols = 6
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_minimal(self):
        m3 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m3._cells), 1)
        self.assertEqual(len(m3._cells[0]), 1)

    def test_maze_no_columns(self):
        num_cols = 0
        num_rows = 10
        with self.assertRaises(ValueError):
            Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_no_rows(self):
        num_cols = 10
        num_rows = 0
        with self.assertRaises(ValueError):
            Maze(0, 0, num_rows, num_cols, 10, 10)

    # tests for class maze method to form entrance and exit
    def test_break_entrance_and_exit_method_standard(self):
        num_cols = 6
        num_rows = 10
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2._break_entrance_and_exit()
        self.assertFalse(m2._cells[0][0].top_wall)
        self.assertFalse(m2._cells[num_cols - 1][num_rows - 1].bottom_wall)

    def test_break_entrance_and_exit_method_single_cell(self):
        num_cols = 1
        num_rows = 1
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2._break_entrance_and_exit()
        self.assertFalse(m2._cells[0][0].top_wall)
        self.assertFalse(m2._cells[num_cols - 1][num_rows - 1].bottom_wall)


if __name__ == "__main__":
    unittest.main()
