from conway.board import Board

if __name__ == "__main__":
    print("Conway's Game of Life")

    rows = 40
    columns = 100
    game_of_life_board = Board(rows, columns)
    game_of_life_board.draw_board()

    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')
        user_action = user_action.strip()

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()
