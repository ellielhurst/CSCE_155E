import numpy as np
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)

size = int(input("What size is your board? "))
board = np.full((size,size),' ')

def create_board():
    count = 0
    for x in range(0,size):
        for y in range(0,size):
            if count < 1/5 * size * size:
                dice = random.randint(1,5)
                if dice == 1:
                    board[x][y] = '#'
                    count += 1
                else:
                    board[x][y] = '~'
            else:
                board[x][y] = '~'

def print_array():
    for x in range(0,size):
        for y in range(0,size):
            print(Fore.CYAN+ str(board[y][x]), end="")
        print()

def enter_coord():
    coord_x, coord_y = [int(i) for i in input("Pick a coordinate to launch missile!").split()]
    if 0 <= coord_x <= size - 1 and 0<= coord_y <= size - 1:
        if board[coord_x][coord_y] == '#':
            board[coord_x][coord_y] = 'X' 
            print(Fore.RED + 'You hit a ship!')
        elif board[coord_x][coord_y] == '~':
            board[coord_x][coord_y] = 'O'
            print(Fore.RED + 'You missed!')
    else:
        print('Not a valid coordinate, try again.')

def check_game_continue():
    for x in range(0,size):
        for y in range(0,size):
            if board[x][y] == '#':
                return True
    print('Game end!!!!!')
    return False

create_board()
print_array()
while check_game_continue():
    enter_coord()
    print_array()
