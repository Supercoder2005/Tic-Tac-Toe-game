import random 

print("Welcome to Tic-Tac-Toe")
print("----------------------")

possibleNumbers=[1,2,3,4,5,6,7,8,9]  #it is basically for the grid of gameboard 
gameBoard = [[1,2,3],[4,5,6],[7,8,9]] #it is a 2D array having 3 rows and 3 columns 
rows = 3
columns = 3

def printGameBoard():
    for x in range (rows):
        print("\n+---+---+---+")
        print("|",end="")
        for y in range(columns):
            print("",gameBoard[x][y],end=" |")
    print("\n+---+---+---+")

def modifyArray(num,turn):   # it will modify the gameboard according to the position (here num) given by user 
    num -= 1
    if(num==0):
        gameBoard[0][0]=turn 
    elif(num==1):
        gameBoard[0][1]=turn 
    elif(num==2):
        gameBoard[0][2]=turn 
    elif(num==3):
        gameBoard[1][0]=turn 
    elif(num==4):
        gameBoard[1][1]=turn 
    elif(num==5):
        gameBoard[1][2]=turn 
    elif(num==6):
        gameBoard[2][0]=turn 
    elif(num==7):
        gameBoard[2][1]=turn 
    elif(num==8):
        gameBoard[2][2]=turn 

def checkForWinner(gameBoard):
    # X axis
    
    #1st row
    if(gameBoard[0][0]=='X' and gameBoard[0][1]=='X' and gameBoard[0][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[0][1]=='O' and gameBoard[0][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    #2nd row
    elif(gameBoard[1][0]=='X' and gameBoard[1][1]=='X' and gameBoard[1][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[1][0]=='O' and gameBoard[1][1]=='O' and gameBoard[1][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    #3rd row
    elif(gameBoard[2][0]=='X' and gameBoard[2][1]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[2][0]=='O' and gameBoard[2][1]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'

    # Y axis 

    #1st column
    elif(gameBoard[0][0]=='X' and gameBoard[1][0]=='X' and gameBoard[2][0]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][0]=='O' and gameBoard[2][0]=='O'):
        print("O has won !!!")
        return 'O'
    
    #2nd column
    elif(gameBoard[0][1]=='X' and gameBoard[1][1]=='X' and gameBoard[2][1]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][1]=='O' and gameBoard[1][1]=='O' and gameBoard[2][1]=='O'):
        print("O has won !!!")
        return 'O'

    #3rd column
    elif(gameBoard[0][2]=='X' and gameBoard[1][2]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][2]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    # Diagonal 

    #left diagonal
    elif(gameBoard[0][0]=='X' and gameBoard[1][1]=='X' and gameBoard[2][2]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][1]=='O' and gameBoard[2][2]=='O'):
        print("O has won !!!")
        return 'O'
    
    #right diagonal
    elif(gameBoard[0][2]=='X' and gameBoard[1][1]=='X' and gameBoard[2][0]=='X'):
        print("X has won !!!")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][1]=='O' and gameBoard[2][0]=='O'):
        print("O has won !!!")
        return 'O'
    
    return None

def isDraw():
    # Check if all positions are filled and there's no winner
    return all(isinstance(cell, str) for row in gameBoard for cell in row)

leaveloop = False # used just to end the game 
turnCounter = 0  # keeps the ytreack whether it's my turn or computer's turn

while(leaveloop == False):

    # it's the player's turn 
    if(turnCounter % 2 ==1):
        printGameBoard()
        numberPicked = int(input("\n Choose a number between 1 to 9:"))
        if (numberPicked>=1 and numberPicked<=9):
            modifyArray(numberPicked,'X')
            possibleNumbers.remove(numberPicked)
        else:
            print("Invalid input , plrase try again")
        turnCounter += 1
         
    # it's the computer's turn 
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers) # computer will choice randomly from the possibleNumber list 
            print("\nCpu Choice:",cpuChoice)
            if cpuChoice in possibleNumbers:
                modifyArray(cpuChoice,'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break 

# Check for a winner
    winner = checkForWinner(gameBoard)
    if winner:
        printGameBoard()
        print(f"\n{winner} has won the game!")
        leaveloop = True  # End the loop when there is a winner
        break

# Check for a draw
    if isDraw():
        printGameBoard()
        print("\nIt's a draw!")
        leaveloop = True  # End the loop on draw
        break

        





