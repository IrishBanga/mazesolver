import unittest
from main import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        # Test the creation of cells in the maze
        test_values = [
            (0, 0),
            (10, 10),
            (10, 20),
            (10, 12),
            (10, 15),
            (15, 10),
        ]

        for num_rows, num_cols in test_values:
            with self.subTest(num_rows=num_rows, num_cols=num_cols):
                m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
                self.assertEqual(
                    len(m1.cells),
                    num_cols,
                )
                self.assertEqual(
                    len(m1.cells[0] if m1.cells else []),
                    num_rows,
                )


if __name__ == "__main__":
    unittest.main()
