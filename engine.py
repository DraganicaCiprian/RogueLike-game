from termcolor import colored
import random


def create_board(width, height, border_color=colored('#', 'grey'), fill_color=' ', border_width=1):
    matrix = []
    lst = []
    colored_lst = []
    for i in range(width):
        colored_lst.append(border_color[:])
    for i in range(border_width):
        matrix.append(colored_lst[:])
        lst.append(border_color[:])
    for i in range(width - border_width * 2):
        lst.append(fill_color[:])
    for i in range(border_width):
        lst.append(border_color[:])
    for i in range(height - 2 * border_width):
        matrix.append(lst[:])
    for i in range(border_width):
        matrix.append(colored_lst[:])
    return matrix


def level_one():
    board = create_board(30, 20)
    for i in range(1, 10):
        board[i][10] = colored('#', 'grey')
    for i in range(16, 20):
        board[i][10] = colored('#', 'grey')
    for i in range(1, 6):
        board[i][20] = colored('#', 'grey')
    for i in range(10, 20):
        board[i][20] = colored('#', 'grey')
    board[2][15] = colored('&', 'cyan')
    board[12][29] = colored('/', 'yellow')
    board[13][28] = colored('#', 'grey')
    board[11][28] = colored('#', 'grey')
    return board


def level_two():
    board = create_board(30, 20)
    for i in range(2, 3):
        for j in range(1, 20):
            board[i][j] = colored('#', 'grey')
    for i in range(4, 5):
        for j in range(1, 15):
            board[i][j] = colored('#', 'grey')
    for i in range(4, 13):
        for j in range(15, 16):
            board[i][j] = colored('#', 'grey')
    for i in range(2, 11):
        for j in range(19, 20):
            board[i][j] = colored('#', 'grey')
    for i in range(13, 14):
        for j in range(15, 30):
            board[i][j] = colored('#', 'grey')
    for i in range(11, 12):
        for j in range(19, 30):
            board[i][j] = colored('#', 'grey')
    board[3][18] = colored('&', 'cyan')
    board[12][16] = colored('Q', 'green')
    board[12][29] = colored('/', 'yellow')
    return board


def level_three():
    board = create_board(30, 20)
    for i in range(10):
        board[4][i + 1] = colored('#', 'grey')
    board[1][10] = colored('#', 'grey')
    board[3][10] = colored('#', 'grey')
    for i in range(8):
        board[i + 1][14] = colored('#', 'grey')
    board[8][1] = colored('#', 'grey')
    for i in range(11):
        board[8][i + 3] = colored('#', 'grey')
    for i in range(8):
        board[i + 9][4] = colored('#', 'grey')
    board[18][4] = colored('#', 'grey')
    for i in range(8):
        board[i + 9][14] = colored('#', 'grey')
    board[18][14] = colored('#', 'grey')
    board[1][18] = colored('#', 'grey')
    for i in range(16):
        board[i+3][18] = colored('#', 'grey')
    for i in range(4):
        board[4][i+19] = colored('#', 'grey')
    for i in range(5):
        board[4][i+24] = colored('#', 'grey')
    for i in range(4):
        board[8][i+19] = colored('#', 'grey')
    for i in range(5):
        board[8][i+24] = colored('#', 'grey')
    for i in range(4):
        board[12][i+19] = colored('#', 'grey')
    for i in range(5):
        board[12][i+24] = colored('#', 'grey')
    board[10][9] = colored('&', 'cyan')
    board[6][19] = colored('&', 'cyan')
    board[10][28] = colored('Q', 'green')
    board[18][28] = colored('!', 'magenta')
    board[18][22] = colored('#', 'grey')
    board[18][24] = colored('#', 'grey')
    board[19][23] = colored('/', 'yellow')
    return board


def boss_level():
    board = create_board(30, 20)
    x = random.randint(1, 9)
    y = random.randint(11, 19)
    for i in range(x, x+5):
        for j in range(y, y+5):
            board[i][j] = colored('X', 'red')
    board[6][25] = '%'        
    return board


def create_player(poz1, poz2):
    player = {'PLAYER_ICON': '@', 'PLAYER_height': poz1, 'PLAYER_width': poz2}
    return player


def put_player_on_board(board, player):
    board[list(player.values())[1]][list(player.values())[2]] = list(player.values())[0]
    return board


def player_movement(board, player, key):
    if key == 'd':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_width'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_width'] -= 1
    elif key == 'a':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_width'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_width'] += 1
    elif key == 's':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_height'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_height'] -= 1
    elif key == 'w':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_height'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_height'] += 1


# def fight():
#     print('LET THE HUNGER GAME BEGINS')
#     player_health = 100
#     monster_health = 100
#     while player_health > 0 or monster_health > 0:
        

def player_movement_boss_level(board, player, key):
    if key == 'd':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_width'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_width'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('X', 'red'):
            fight()
    elif key == 'a':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_width'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_width'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('X', 'red'):
            fight()
    elif key == 's':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_height'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_height'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('X', 'red'):
            fight()
    elif key == 'w':
        board[player['PLAYER_height']][player['PLAYER_width']] = ' '
        player['PLAYER_height'] -= 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('#', 'grey'):
            player['PLAYER_height'] += 1
        if board[player['PLAYER_height']][player['PLAYER_width']] == colored('X', 'red'):
            fight()


def player_characteristics():
    print('Insert your name traveler!')
    name = input()
    print("Select your race", name + '.')
    races = ['Human', 'Elf', 'Dwarf', 'Orc', 'Tauren', 'Goblin']
    ok = 1
    for item in races:
        print(str(ok) + ':', item)
        ok = ok + 1
    race = input()
    while race not in ('1', '2', '3', '4', '5', '6'):
        ok = 1
        for item in races:
            print(str(ok) + ':', item)
            ok = ok + 1
        race = input('Wrong input, try again.')
    for item in races:
        if race == str(races.index(item) + 1):
            race = item
    return {'Name': name, 'Race': race}


def player_inventory(board, player, inventory):
    if board[player['PLAYER_height']][player['PLAYER_width']] == colored('Q', 'green'):
        if 'health' not in inventory:
            inventory.update({'health': 100})
        elif 'health' in inventory:
            inventory['health'] += 25
    if board[player['PLAYER_height']][player['PLAYER_width']] == colored('&', 'cyan'):
        if 'armour piece' not in inventory:
            inventory.update({'armour piece': 25})
        elif 'armour piece' in inventory:
            inventory['armour piece'] += 25
    if board[player['PLAYER_height']][player['PLAYER_width']] == colored('!', 'magenta'):
        if 'sword' not in inventory:
            inventory.update({'sword': 1})
        elif 'sword' in inventory:
            inventory['sword'] += 1
    return inventory
