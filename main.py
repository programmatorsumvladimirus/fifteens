# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

RIGHT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    field = RIGHT.copy()
    for i in list(range(100)):
        shuffle = random.randint(0, 3)
        key = list(MOVES.keys())[shuffle]
        try:
            perform_move(field, key)
        except IndexError:
            pass
    return field
    pass


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    for i in list(range(16)):
        if field[i] == EMPTY_MARK or field[i] < 10:
            print(' ', end = '')
        print(field[i], end = '')
        if (i + 1) % 4 == 0:
            print('\n')
        else:
            print(' ', end = '')
    pass


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    if field == RIGHT:
        print('YOU ARE WINNER!')
        return True
    else:
        return False
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    empty_index = field.index(EMPTY_MARK) # положение пустой клетки
    move = MOVES[key] # переданные ходы пользователя
    target_index = empty_index + move #
    if target_index < 0 or target_index >= len(field) or is_valid_move(empty_index, target_index):
        raise IndexError("You shall not pass!")
    else:
        field[empty_index] = field[target_index]
        field[target_index] = EMPTY_MARK
    pass

def is_valid_move(start_index, target_index):
    return (start_index % 4 == 0 and start_index - target_index == 1) or (target_index % 4 == 0 and target_index - start_index == 1)


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    key = ''
    while key not in MOVES:
        key = input('your move ->')
    return key
    pass


def main():
    field = shuffle_field()
    while not is_game_finished(field):
        print_field(field)
        key = handle_user_input()
        try:
            perform_move(field, key)
        except IndexError as ex:
            print(str(ex))


    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()