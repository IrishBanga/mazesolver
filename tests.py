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

    def test_maze_reset_visited(self):
        # Test that all cells are marked as visited after breaking walls
        test_values = [
            (10, 10),
            (10, 20),
            (10, 12),
            (10, 15),
            (15, 10),
        ]

        for num_rows, num_cols in test_values:
            with self.subTest(num_rows=num_rows, num_cols=num_cols):
                m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
                m1._break_walls(0, 0)
                for column in m1.cells:
                    for cell in column:
                        self.assertTrue(
                            cell.visited
                        )  # Expect all cells to be visited after breaking walls

                # Now we reset the visited state and check again
                m1._reset_visited()
                for column in m1.cells:
                    for cell in column:
                        self.assertFalse(
                            cell.visited
                        )  # We expect all cells state to be reset to not visited after calling _reset_visited


if __name__ == "__main__":
    unittest.main()
