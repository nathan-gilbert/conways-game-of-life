import unittest
from conway.board import Board


class TestBoard(unittest.TestCase):

    def test_draw_board(self):
        b = Board(1, 1)
        self.assertEqual(b, [])

    def test_get_neighbors(self):
        b = Board(10, 10)
        n = b.get_neighbors(1, 1)
        self.assertEqual(n, [])


if __name__ == '__main__':
    unittest.main()
