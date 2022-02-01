from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        
        for j in range(3):
            print("|  ", board[i][j],"  ", end="")
            
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")
    return


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move: "))
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        board[i][j] = "O"
                        display_board(board)
                        return
            print ("Invalid move")
        except:
            print ("Enter an integer number from 0 to 9")
    


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    empty_list = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                empty_list.append((i,j)) 
    return empty_list


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    result1, result2=[], []
    
    for i in range(3):
        if board[i].count("X") == 3:
            return "You lose"
        elif board[i].count("O") == 3:
            return "You win!"
        result1.append(board[i][i])
        result2.append(board[i][2-i]) 
        if result1.count("X") == 3 or result2.count("X") == 3:
            return "You lose"
        elif result1.count("O") == 3 or result2.count("O") == 3:
            return "You win!"                       
        result3=[]
        for j in range(3):
            result3.append(board[j][i])
        if result3.count("X") == 3:
            return "You lose"
        elif result3.count("O") == 3:
            return "You win!"      
    if sign == False:
        return "The game end with a tie"
    else:
        return False    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        comp_move = randrange(1,10)
        for i in range(3):
            for j in range(3):
                if board[i][j] == comp_move:
                    board[i][j] = "X"
                    display_board(board)
                    return


board = [[1,2,3], [4,5,6], [7,8,9]]
 #board[row][column]
board[1][1] ="X"
display_board(board)
player = "O"
while True:
    if player == "O":
        enter_move(board)
    else:
        draw_move(board)    
    empty_list = make_list_of_free_fields(board)
    winner = victory_for(board, len(empty_list) >=1)
    if winner:
        print (winner)
        break
    if player == "O":
        player = "X"
    else:
        player = "O"
