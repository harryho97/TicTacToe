from random import randint
from board import *



#the AI for the computer
def computerPlay(board,playerID):
    x=3
    y=3
    if board[0][0]==board[0][1] !=0 and board[0][2]==0:
            x=0
            y=2
    elif board[0][0]==board[0][2]!=0 and board[0][1]==0:
            x=0
            y=1
    elif board[0][1]==board[0][2]!=0 and board[0][0]==0:
            x=0
            y=0
    elif board[1][0]==board[1][1]!=0 and board[1][2]==0:
            x=1
            y=2
    elif board[1][0]==board[1][2]!=0 and board[1][1]==0:
            x=1
            y=1
    elif board[1][1]==board[1][2]!=0 and board[1][0]==0:
            x=1
            y=0
    elif board[2][0]==board[2][1]!=0 and board[2][2]==0:
            x=2
            y=2
    elif board[2][0]==board[2][2]!=0 and board[2][1]==0:
            x=2
            y=1
    elif board[2][1]==board[2][2]!=0 and board[2][0]==0:
            x=2
            y=0
    elif board[0][0]==board[1][0]!=0 and board[2][0]==0:
        x=2
        y=0
    elif board[0][0]==board[2][0]!=0 and board[1][0]==0:
        x=1
        y=0
    elif board[1][0]==board[2][0]!=0 and board[0][0]==0:
        x=0
        y=0
    elif board[0][1]==board[2][1]!=0 and board[1][1]==0:
        x=1
        y=1
    elif board[0][1]==board[1][1]!=0 and board[2][1]==0:
        x=2
        y=1
    elif board[1][1]==board[2][1]!=0 and board[0][1]==0:
        x=0
        y=1
    elif board[2][2]==board[1][2]!=0 and board[0][2]==0:
        x=0
        y=2
    elif board[2][2]==board[0][2]!=0 and board[1][2]==0:
        x=1
        y=2
    elif board[1][2]==board[0][2]!=0 and board[2][2]==0:
        x=2
        y=2
    elif board[0][0]==board[1][1]!=0 and board[2][2]==0:
        x=2
        y=2
    elif board[0][0]==board[2][2]!=0 and board[1][1]==0:
        x=1
        y=1
    elif board[1][1]==board[2][2]!=0 and board[0][0]==0:
        x=0
        y=0
    elif board[0][2]==board[1][1]!=0 and board[2][0]==0:
        x=2
        y=0
    elif board[0][2]==board[2][0]!=0 and board[1][1]==0:
        x=1
        y=1
    elif board[1][1]==board[2][0]!=0 and board[0][2]==0:
        x=0
        y=2
    elif board[1][1]==0:
        x=1
        y=1
    elif board[0][0]==0:
        x=0
        y=0
    elif board[0][2]==0:
        x=0
        y=0
    elif board[2][0]==0:
        x=2
        y=0
    elif board[2][2]==0:
        x=2
        y=2
    else:
        x=randint(0,2)
        y=randint(0,2)
    while board[x][y]!=0:
        x=randint(0,2)
        y=randint(0,2)
    playOneTime(board,x,y,playerID)
    return board[x][y]

#the main function to manage the game of computer
def computerGame():
    board=newBoard()
    playerID=3-eval(input("Enter 1 for you start first,enter 2 for computer start first"))
    computerPlay(board,playerID)









