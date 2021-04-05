#----------Global Variables----------

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# checking whether the game is still on
game_still_on = True

# gives info about winner
winner = None

# gives info of current player('O' goes first)
current_player = 'O'

# FUNCTIONS:

# definig all conditions for playing 'tictactaoe'
def start_game():
        
    display_board()
    
    # loop until game ends   
    while game_still_on:
        
        #  handle a trun    
        handle_turn(current_player)
        
        # check if game ends      
        check_if_game_ends()
        
        # flip to other player
        flip_turn()
    
    # declaring the winner            
    if winner == 'X' or winner == 'O':
        print(winner + ' won..!!!')
    elif winner == None:
        print("It's a tie ..!!!")
            
# displaying board on screen       
def display_board():
    print('\n')
    print('\n')
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print('\n')
    
# Handle a turn for an arbitrary player    
def handle_turn(player):
    
    # getting player's position
    print(player + "'s turn :")
    
    # making sure that user enters valid input
    player_position = input('Choose a position from 1-9: ')
    valid_input = False
    
    while not valid_input:
        while player_position not in ['1','2','3','4','5','6','7','8','9']:
            
            player_position = input('Choose a position from 1-9: ')
        # setting index position as per board
        player_position = int(player_position) - 1
        
        # make sure spot is available
        if board[player_position] == '-':
            valid_input = True
        else:
            print('Postion already taken! Please choose a new postion:')
    
    # put the game piece on board
    board[player_position] = player
    
    # display the board
    display_board()
        
# check if game is over
def check_if_game_ends():
    check_winner()
    check_tie()

# check to see who won
def check_winner():
    
    # set global variables
    global winner
    
    # check if there was a winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# checking rows for winner
def check_rows():
    
    # set global variables
    global game_still_on
    
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    
    if row_1 or row_2 or row_3:
        game_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
        
 # checking columns for winner       
def check_columns():
    
    # set global variables
    global game_still_on
    
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    
    if column_1 or column_2 or column_3:
        game_still_on = False
        
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
        
 # checking diagonals for winner       
def check_diagonals():
    global game_still_on
    
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    
    if diagonal_1 or diagonal_2:
        game_still_on = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    else:
        return None

# checking if there is a tie
def check_tie():
    
    global game_still_on
    
    if '-' not in board:
        game_still_on = False
        return True
    else:
        return False

# to filp the turns in the game
def flip_turn():
    
    global current_player
    
    if current_player == 'O':
        current_player = 'X'
    elif current_player =='X':
        current_player = 'O'
        
# start playing the game
start_game()



    


    

