def display_board(board):
    for item in board:
        print(*item)


def print_characteristics(characteristics):
    for key, value in characteristics.items():
        print(f'{key} : {value}')


def print_inventory(inventory):
    print(inventory)
