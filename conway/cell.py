from enum import Enum


class CellStatus(Enum):
    ALIVE = 1
    DEAD = 2
    UNKNOWN = 3


class Cell:
    def __init__(self):
        """
        """
        self.__status = CellStatus.DEAD

    def set_dead(self):
        """
        """
        self.__status = CellStatus.DEAD

    def set_alive(self):
        """
        """
        self.__status = CellStatus.ALIVE

    def is_alive(self):
        """
        """
        return self.__status == CellStatus.ALIVE

    def get_print_character(self):
        """
        """
        if self.is_alive():
            return '❃'
        return '.'
