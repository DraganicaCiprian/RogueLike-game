import util
import engine
import ui
from termcolor import colored


def main():
    inventory = {}
    player_characteristics = engine.player_characteristics()
    level_one_board = engine.level_one()
    level_two_board = engine.level_two()
    level_three_board = engine.level_three()
    # boss_level_board_1 = engine.boss_level_1()
    util.clear_screen()
    # loop condition
    is_running = True
    # first position on level one
    player = engine.create_player(3, 1)
    # level one loop
    while is_running:
        engine.put_player_on_board(level_one_board, player)
        ui.display_board(level_one_board)
        ui.print_characteristics(player_characteristics)
        key = util.key_pressed()
        engine.player_movement(level_one_board, player, key)
        engine.player_inventory(level_one_board, player, inventory)
        if level_one_board[player['PLAYER_height']][player['PLAYER_width']] == colored('/', 'yellow'):
            util.clear_screen()
            break
        if key == 'q':
            is_running = False
        while key == 'i':
            util.clear_screen()
            ui.display_board(level_one_board)
            ui.print_inventory(inventory)
            key = util.key_pressed()
            util.clear_screen()
        util.clear_screen()
    # first position on level two
    player = engine.create_player(3, 1)
    # level two loop
    while is_running:
        engine.put_player_on_board(level_two_board, player)
        ui.display_board(level_two_board)
        ui.print_characteristics(player_characteristics)
        key = util.key_pressed()
        engine.player_movement(level_two_board, player, key)
        engine.player_inventory(level_two_board, player, inventory)
        if level_two_board[player['PLAYER_height']][player['PLAYER_width']] == colored('/', 'yellow'):
            util.clear_screen()
            break
        if key == 'q':
            is_running = False
        while key == 'i':
            util.clear_screen()
            ui.display_board(level_two_board)
            ui.print_inventory(inventory)
            key = util.key_pressed()
            util.clear_screen()
        util.clear_screen()
    # first position on level three
    player = engine.create_player(2, 1)
    # level three loop
    while is_running:
        engine.put_player_on_board(level_three_board, player)
        ui.display_board(level_three_board)
        ui.print_characteristics(player_characteristics)
        key = util.key_pressed()
        engine.player_movement(level_three_board, player, key)
        engine.player_inventory(level_three_board, player, inventory)
        if level_three_board[player['PLAYER_height']][player['PLAYER_width']] == colored('/', 'yellow'):
            util.clear_screen()
            break
        if key == 'q':
            is_running = False
        while key == 'i':
            util.clear_screen()
            ui.display_board(level_three_board)
            ui.print_inventory(inventory)
            key = util.key_pressed()
            util.clear_screen()
        util.clear_screen()
    # first position on boss level
    player = engine.create_player(3, 1)
    # boss level loop
    while is_running:
        boss_level_board = engine.boss_level()
        engine.put_player_on_board(boss_level_board, player)
        ui.display_board(boss_level_board)
        ui.print_characteristics(player_characteristics)
        key = util.key_pressed()
        engine.player_movement_boss_level(boss_level_board, player, key)
        engine.player_inventory(boss_level_board, player, inventory)
        if boss_level_board[player['PLAYER_height']][player['PLAYER_width']] == colored('/', 'yellow'):
            util.clear_screen()
            break
        if key == 'q':
            is_running = False
        while key == 'i':
            util.clear_screen()
            ui.display_board(boss_level_board)
            ui.print_inventory(inventory)
            key = util.key_pressed()
            util.clear_screen()
        util.clear_screen()


if __name__ == '__main__':
    main()
