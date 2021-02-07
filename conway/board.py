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
        self.__init_board()

    def __init_board(self):
        """
        """
        for row in self.__grid:
            for column in row:
                # there is a 33% chance the cells spawn alive.
                chance_number = randint(0, 2)
                if chance_number == 1:
                    column.set_alive()

    def draw_board(self):
        """
        """
        print('\n' * 10)
        for row in self.__grid:
            for column in row:
                print(column.get_print_character(), end='')
            print()

    def update_board(self):
        """
        """
        bring_to_life = []
        sentence_to_death = []
        for row in range(len(self.__grid)):
            for column in range(len(self.__grid[row])):
                neighbours = self.get_neighbors(row, column)

                living_neighbours = []
                for neighbour in neighbours:
                    if neighbour.is_alive():
                        living_neighbours.append(neighbour)

                cell = self.__grid[row][column]
                if cell.is_alive():
                    if len(living_neighbours) < 2 or len(living_neighbours) > 3:
                        sentence_to_death.append(cell)

                    if len(living_neighbours) == 3 or len(living_neighbours) == 2:
                        bring_to_life.append(cell)
                else:
                    if len(living_neighbours) == 3:
                        bring_to_life.append(cell)

        for cell in bring_to_life:
            cell.set_alive()

        for cell in sentence_to_death:
            cell.set_dead()

    def get_neighbors(self, check_row, check_column):
        """
        """
        # define neighbors
        search_min = -1
        search_max = 2

        neighbors = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                is_neighbor = True
                if neighbour_row == check_row and neighbour_column == check_column:
                    is_neighbor = False

                if neighbour_row < 0 or neighbour_row >= self.__rows:
                    is_neighbor = False

                if neighbour_column < 0 or neighbour_column >= self.__columns:
                    is_neighbor = False

                if is_neighbor:
                    neighbors.append(self.__grid[neighbour_row][neighbour_column])

        return neighbors
