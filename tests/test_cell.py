import unittest
from conway.cell import Cell


class TestCell(unittest.TestCase):

    def test_is_alive(self):
        c = Cell()
        self.assertFalse(c.is_alive())
        c.set_alive()
        self.assertTrue(c.is_alive())

    def test_get_print_character(self):
        c = Cell()
        self.assertEqual(c.get_print_character(), '.')
        c.set_alive()
        self.assertEqual(c.get_print_character(), '❃')
        c.set_dead()
        self.assertEqual(c.get_print_character(), '.')


if __name__ == '__main__':
    unittest.main()