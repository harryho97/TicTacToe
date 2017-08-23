#return a 3*3 list of 0
def newBoard():
    board=[[0]*3 for i in range(3)]
    return board



#print the board
def displayBoard(board):
    for x in range(3):
      for y in range(3):
         if y==2:
             print(board[x][y])
         else:
             print(board[x][y],"| ",sep=' ',end='')



#to play the game with a playerID and the position to place the chess
def playOneTime(board,x,y,playerID):
    if board[x][y]==0:
        board[x][y]=playerID
        return True
    else:
        print("Occupied!")
        return False

#to check if anyone has already won the game
def checkVictory(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=0 :
            return True
        elif board[0][i]==board[1][i]==board[2][i]!=0:
            return True
        elif board[0][0]==board[1][1]==board[2][2]!=0:
            return True
        elif board[0][2]==board[1][1]==board[2][0]!=0:
            return True
    return False

