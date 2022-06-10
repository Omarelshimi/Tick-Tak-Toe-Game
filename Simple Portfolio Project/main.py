#Planning
# Step 1 - Create visual board in console
# Step 2 - Assign values from 1 - 9 for each tile on the board
# Step 3 - 

#Global Variables
player = 1
game = True

#Board Positons
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

#Function Displays Board
def displayBoard(board):
    
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print('--------------')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('--------------')
    print(f'{board[7]}|{board[8]}|{board[9]}')
        

#Check if postion is available
def checkPosition(i):
    if board[i] == '-':
        return True
    else:
        return False

# Game Function
def play():
    while (game == True):
        if player == 1 and checkPosition() == True:
            pos = input("Player 1's chance")
            board[pos] = "X"
            displayBoard() 
            
play()