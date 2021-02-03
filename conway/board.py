from random import randint

from conway.cell import Cell


class Board:
    def __init__(self, rows, columns):
        """
        """
        self.__rows = rows
        self.__columns = columns
        self.__grid = [
            [Cell() for _ in range(self.__columns)] for _ in range(self.__rows)
        ]
        self.__generate_board()

    def draw_board(self):
        """
        """
        pass

    def __generate_board(self):
        """
        """
        pass

    def update_board(self):
        """
        """
        pass

    def get_neighbors(self, check_row, check_column):
        """
        """
        pass
