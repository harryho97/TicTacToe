from board import *

#save the game file
def saveGame(board):
    gameFile=open("saveFile.txt","w")
    for x in range (3):
        for y in range(3):
            gameFile.write(str(board[x][y]))
        gameFile.write("\n")
    gameFile.close()


#load the game file
def loadGame():
    board=[[0]*3 for i in range(3)]
    x,y=0,0
    for line in open('saveFile.txt','r'):
        for n in line:
            if not n=='\n':
                board[x][y]=int(n)
                y=y+1
        y=0
        x=x+1
    return board

