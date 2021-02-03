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
        pass

    def set_alive(self):
        """
        """
        pass

    def is_alive(self):
        """
        """
        pass

    def get_print_character(self):
        """
        """
        pass
