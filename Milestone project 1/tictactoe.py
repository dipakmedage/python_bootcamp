import random
 
def display_board(board):
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' | ')
    print("-------------")
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' | ')
    print("-------------")
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' | ')

#display_board(['']*10)


def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player1 choose either x or O ?').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
#player_input()


def place_marker(board,marker,positon):
    board[positon]=marker



#player1_marker,player2_marker=preference_user()

test_board = ['#','X','O','X','O','X','O','X','O','X']
# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board,mark):
    
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or # row3
    (board[4]==mark and board[5]==mark and board[6]==mark) or # row2
    (board[7]==mark and board[8]==mark and board[9]==mark) or # row 1
    (board[7]==mark and board[4]==mark and board[1]==mark) or #column 1
    (board[8]==mark and board[5]==mark and board[2]==mark) or #column 2
    (board[9]==mark and board[6]==mark and board[3]==mark) or #column 3
    (board[7]==mark and board[5]==mark and board[3]==mark) or #diag 1
    (board[9]==mark and board[5]==mark and board[1]==mark) #diag 2
    )
#print(win_check(test_board,'X'))
 
def choose_first():
    if random.randint(0,1)==0:
         return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,positon):
    return board[positon]==' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose your next position (1-9) '))
    return position

def replay():
    return input('Do you want to play again ?Enter Yes or No').lower().startswith('y')

print('Welcome to Tic tac toe!')

#Actual logic

while True:
    #reset board
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first.')

    play_game=input('Are you ready to play? Enter Yes or No')

    if play_game.lower()[0]=='y':
        game_on='True'
    else:
        game_on='False'
    while game_on:
        if turn == 'Player 1':
            #player 1 turn
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulation! player 1 you have won ')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw')
                    break
                else:
                    turn='Player 2'
        else:
            #player 2 turn
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('player 2 won!')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw')
                    break
                else:
                    turn='Player 1'
    if not replay():
        break


        