from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    clear_output()
test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)
# display_board(test_board)
def player_input():
    marker= ''
    while marker != 'X' and marker != 'O':
        marker = input ('player 1: choose X or O').upper()
        if marker == 'X':
            return ('X','O')
        else :
            return ('O' , 'X')
player1_marker, player2_marker = player_input()
def place_marker(board, marker,positon):
    board[positon] = marker
# place_marker(test_board,'$',8)
# display_board(test_board)
def win_check(board,mark):
   ( board[1] == mark and board[2] == mark and board[3]== mark)