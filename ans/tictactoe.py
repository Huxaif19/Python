import random
def player_input():
    marker= ''
    while not (marker =='X' or marker == 'O'):
        marker = input('player1: choose X or O').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O','X')
def choose_first():
    filp = random.randint(0,1)
    if filp == 0:
        return 'player 1'
    else :
        return 'player 2'
def space_check(board, position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check    (board,position):
        position = int(input("choose a position:(1-9) "))
    return position
def replay():
    choice= input('play again(y orn)')
    return choice == 'y'
def welcome():
    while True:
        the_board = [' ']*10
        player_1_marker,player_2_marker = player_input()
        turn = choose_first
        print(turn + ' will go first')
        play_game= input ("ready to play? y or n")
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn == 'player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player_1_marker, position)
                if win_check(the_board, player_1_marker):
                    display_board(the_board)
                    print ('player 1 has won the game')
                    game_on = False
                else:
                    if full_board_check(the_board):
                            display_board(the_board)
                            print("tie game!")
                            break
                    else :
                        turn = 'player_2'
                        display_board(the_board)
                        position = player_choice(the_board)
                        place_marker(the_board,player_1_marker, position)
                        if win_check(the_board, player_1_marker):
                            display_board(the_board)
                            print ('player 1 has won the game')
                            game_on = False
                        else:
                            if full_board_check(the_board):
                                display_board(the_board)
                                print("tie game!")
                                break
        if not replay():
            break