import os
import platform
import random

# Declaring global variables
board_positions = [' ' for num in range(0, 10)]
players = ['X', 'O']
player = ''

def clear_output():
    if 'Windows' in platform.system():
        os.system('cls')
    else:
        os.system('clear')

def start_player(players):
    return random.choice(players)

def get_round_player(round_player):
    return 'Player 1' if round_player == player else 'Player 2'

def build_board(board_positions):
    print('     |     |                  |     |     ')
    print('  7  |  8  |  9            {pos7}  |  {pos8}  |  {pos9}  '.format(pos7=board_positions[7], pos8=board_positions[8], pos9=board_positions[9]))
    print('_____|_____|_____        _____|_____|_____')
    print('     |     |                  |     |     ')
    print('  4  |  5  |  6            {pos4}  |  {pos5}  |  {pos6}  '.format(pos4=board_positions[4], pos5=board_positions[5], pos6=board_positions[6]))
    print('_____|_____|_____        _____|_____|_____')
    print('     |     |                  |     |     ')
    print('  1  |  2  |  3            {pos1}  |  {pos2}  |  {pos3}  '.format(pos1=board_positions[1], pos2=board_positions[2], pos3=board_positions[3]))
    print('     |     |                  |     |     \n')

def position_available(board_positions, position):
    return board_positions[position] == ' '

def make_move(board_positions, round_player):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not position_available(board_positions, position):
        try:
            position = int(input(get_round_player(round_player) + ' choose your position (1-9): '))
        except:
            print('Choose a valid position!')
    
    board_positions[position] = round_player

def check_winner(board_positions, round_player):
    return ((board_positions[7] == board_positions[8] == board_positions[9] == round_player) or # Rows
           (board_positions[4] == board_positions[5] == board_positions[6] == round_player) or # Rows
           (board_positions[1] == board_positions[2] == board_positions[3] == round_player) or # Rows
           (board_positions[3] == board_positions[6] == board_positions[9] == round_player) or # Columns
           (board_positions[2] == board_positions[5] == board_positions[8] == round_player) or # Columns
           (board_positions[1] == board_positions[4] == board_positions[7] == round_player) or # Columns
           (board_positions[7] == board_positions[5] == board_positions[3] == round_player) or # Diagonals
           (board_positions[9] == board_positions[5] == board_positions[1] == round_player)) # Diagonals

def get_next_round_player(round_player):
    return 'O' if round_player == 'X' else 'X'

def check_full_board(board_positions):
    return True if not ' ' in board_positions[1:] else False

while True:
    clear_output()

    while player not in players:
        clear_output()
        print('Welcome to Tic Tac Toe game!\n')

        try:
            player = input('Choose between X or O: ').upper()
        except:
            print('You have to choose X or O !')

    round_player = start_player(players)
    playing = True
    print(get_round_player(round_player) + ' starts playing. \n')
    input('Press ENTER to continue')

    while playing:
        clear_output()
        build_board(board_positions)
        make_move(board_positions, round_player)

        if check_winner(board_positions, round_player):
            clear_output()
            build_board(board_positions)
            print('The winner is ' + get_round_player(round_player) + '!')
            playing = False
        else:
            if check_full_board(board_positions):
                clear_output()
                build_board(board_positions)
                print('\nDraw!')
                playing = False
            else:
                round_player = get_next_round_player(round_player)

    play_again = ''
    
    while play_again not in ['yes', 'no']:
        try:
            play_again = input('Do you want to play again? Yes or No ').lower()
        except:
            print('You have to choose between Yes or No')

    if play_again == 'no':
        break

    board_positions = [' ' for num in range(0, 10)]
    player = ''