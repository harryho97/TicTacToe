from board import *
from random import randint
from computer import *


#ask player for the position the place the chess
def playerPlay(board,playerID):
    displayBoard(board)
    x=eval(input("Please choose a square! Input the x coordinate(1-3):"))-1
    while x!=0 and x!=1 and x!=2:
        x=eval(input("Please choose a square! Input the x coordinate(1-3):"))-1
    y=eval(input("Please choose a square! Input the y coordinate(1-3):"))-1
    while y!=0 and y!=1 and y!=2:
        y=eval(input("Please choose a square! Input the y coordinate(1-3):"))-1
    while not playOneTime(board,x,y,playerID):
        x=eval(input("Please choose a square! Input the x coordinate(1-3):"))-1
        y=eval(input("Please choose a square! Input the y coordinate(1-3):"))-1


#to indicate if the board is fully occupied
def gameOver(board):
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]!=0:
                count+=1
    if count==9 and not checkVictory(board):
        return True
    else:
        return False





#calling back 2 functions to check if the game is over,also printing the information of the game
def displayInformation(board,playerID):
    if checkVictory(board):
        print("Player",3-playerID,"Win the Game!")
        return True
    if gameOver(board):
        print("Fully occupied!")
        return True
    print("NOW IS PLAYER",playerID,"PLAYING!")





#switch the player
def turnPlayer(playerID):
    playerID=3-playerID
    return playerID



#the main function to manage the game with player
def playerGame():
    board=newBoard()
    playerID=1
    selection=eval(input("Who do you want the Player2 to be ? 1 for the computer,2 for another person:)"))
    if selection==1:
        chooseOrder=eval(input("Please choose who play first ,1 for yourself,2 for computer:)"))
        if chooseOrder==1:
            while not displayInformation(board,playerID):
                if playerID==1:
                    playerPlay(board,playerID)
                    playerID=turnPlayer(playerID)
                else:
                    computerPlay(board,playerID)
                    playerID=turnPlayer(playerID)
        else:
            while not displayInformation(board,playerID):
                if playerID==1:
                    computerPlay(board,playerID)
                    playerID=turnPlayer(playerID)
                else:
                    playerPlay(board,playerID)
                    playerID=turnPlayer(playerID)

    else:
        while not displayInformation(board,playerID):
            playerPlay(board,playerID)
            playerID=turnPlayer(playerID)

