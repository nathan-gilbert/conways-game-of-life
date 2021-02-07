import unittest
from conway.board import Board


class TestBoard(unittest.TestCase):

    def test_get_neighbors(self):
        b = Board(10, 10)
        n = b.get_neighbors(1, 1)
        self.assertEqual(len(n), 8)
        n = b.get_neighbors(0, 0)
        self.assertEqual(len(n), 3)


if __name__ == '__main__':
    unittest.main()
