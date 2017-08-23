__author__ = 'jason'
from board import *
from computer import *
from player import *
from saveGame import *
from pygame.color import THECOLORS
import pygame, sys
from pygame.locals import *
fpsClock = pygame.time.Clock()
mySurface = pygame.display.set_mode((640,480))
backgoundImage = pygame.image.load('2.jpg')
X_Image=pygame.image.load('1x.png')
O_Image=pygame.image.load('2x.png')
ReplayImage=pygame.image.load('111.png')
backgroundImage1 = pygame.image.load('1.jpg')
winner = pygame.image.load('winner.png')
draw = pygame.image.load('draw.png')
loser= pygame.image.load('loser.png')
pygame.display.set_caption('Tic tac toe')
#人人对战平台，player VS player#
def play_player(board):
 pygame.init()
 i=1
 checkN=0
 playerID=1
 FPS=50
 fontObj = pygame.font.Font('freesansbold.ttf',20)
 fontObj1 =pygame.font.Font('freesansbold.ttf',50)
 texteSurface1 = fontObj.render('Save',True,THECOLORS["black"])
 texteRect1 = texteSurface1.get_rect()
 texteRect1.topleft = (580,430)
 texteSurface2 = fontObj.render('Home',True,THECOLORS["black"])
 texteRect2 = texteSurface2.get_rect()
 texteRect2.topleft = (580,450)
 ImageRect3=ReplayImage.get_rect()
 ImageRect3.topleft = (600,0)
 texteSurface4=fontObj1.render('The winner is Mr.',True,THECOLORS["black"])
 texteRect4 = texteSurface4.get_rect()
 texteRect4.topleft = (75,95)
 mySurface.blit(backgoundImage,(0,0))
 if board[0][0]==1:
     mySurface.blit(X_Image,(55,90))
 if board[1][0]==1:
     mySurface.blit(X_Image,(195,80))
 if board[2][0]==1:
     mySurface.blit(X_Image,(345,65))
 if board[0][1]==1:
     mySurface.blit(X_Image,(150,210))
 if board[1][1]==1:
     mySurface.blit(X_Image,(250,210))
 if board[2][1]==1:
     mySurface.blit(X_Image,(390,200))
 if board[0][2]==1:
     mySurface.blit(X_Image,(135,345))
 if board[1][2]==1:
     mySurface.blit(X_Image,(280,350))
 if board[2][2]==1:
     mySurface.blit(X_Image,(430,335))
 if board[0][0]==2:
     mySurface.blit(O_Image,(55,90))
 if board[1][0]==2:
     mySurface.blit(O_Image,(195,80))
 if board[2][0]==2:
     mySurface.blit(O_Image,(345,65))
 if board[0][1]==2:
     mySurface.blit(O_Image,(150,210))
 if board[1][1]==2:
     mySurface.blit(O_Image,(250,210))
 if board[2][1]==2:
     mySurface.blit(O_Image,(390,200))
 if board[0][2]==2:
     mySurface.blit(O_Image,(135,345))
 if board[1][2]==2:
     mySurface.blit(O_Image,(280,350))
 if board[2][2]==2:
     mySurface.blit(O_Image,(430,335))
 while True:
    mySurface.blit(texteSurface1,texteRect1)
    mySurface.blit(texteSurface2,texteRect2)
    mySurface.blit(ReplayImage,ImageRect3)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if checkVictory(board)!=True:
            if checkN!=9:
                if i%2!=0:
                  if event.type ==MOUSEBUTTONDOWN:
                    a,b = event.pos
                    if(a>85and a<180and b>80and b<190  and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>190and a<350and b>90and b<180 and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>360and a<490and b>80and b<150  and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>100and a<250and b>210and b<340 and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>250and a<400and b>200and b<320 and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>400and a<550and b>170and b<310 and playOneTime(board,2,1,playerID)==True):
                        x=390
                        y=200
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>150and a<260and b>340and b<440 and playOneTime(board,0,2,playerID)==True):
                        x=140
                        y=340
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>270and a<420and b>340and b<450 and playOneTime(board,1,2,playerID)==True):
                        x=280
                        y=350
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>430and a<580and b>330and b<440 and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                  elif event.type==KEYDOWN:
                    if(event.key==K_q and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_w and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_e and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_a and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_s and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_d and playOneTime(board,2,1,playerID)==True):
                      if i%2!=0:
                        x=390
                        y=200
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_z and playOneTime(board,0,2,playerID)==True):
                        x=140
                        y=340
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_x and playOneTime(board,1,2,playerID)==True):
                      if i%2!=0:
                        x=280
                        y=350
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_c and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                else:
                  if event.type==MOUSEBUTTONDOWN:
                    a,b = event.pos
                    if(a>85and a<180and b>80and b<190 and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>190and a<350and b>90and b<180 and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>360and a<490and b>80and b<150 and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>100and a<250and b>210and b<340 and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>250and a<400and b>200and b<320 and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>400and a<550and b>170and b<310 and playOneTime(board,2,1,playerID)==True):
                        x=390
                        y=200
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>150and a<260and b>340and b<440 and playOneTime(board,0,2,playerID)==True):
                        x=135
                        y=345
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>270and a<420and b>340and b<450 and playOneTime(board,1,2,playerID)==True):
                        x=280
                        y=350
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>430and a<580and b>330and b<440 and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                  elif event.type ==KEYDOWN:
                    if(event.key==K_q and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_w and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_e and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_a and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_s and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_d and playOneTime(board,2,1,playerID)==True):
                        x=390
                        y=200
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_z and playOneTime(board,0,2,playerID)==True):
                        x=135
                        y=345
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_x and playOneTime(board,1,2,playerID)==True):
                        x=280
                        y=350
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_c and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=1
                        mySurface.blit(O_Image,(x,y))
                        i+=1
                        checkN+=1
            if checkN==9:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(draw,(255,155))
        if checkVictory(board) ==True:
            if  playerID==1:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(O_Image,(450,55))
                mySurface.blit(winner,(255,175))
                mySurface.blit(texteSurface4,texteRect4)
                mySurface.blit(ReplayImage,(600,0))
            if  playerID==2:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(X_Image,(465,70))
                mySurface.blit(winner,(255,175))
                mySurface.blit(texteSurface4,texteRect4)
                mySurface.blit(ReplayImage,(600,0))
        if event.type == MOUSEBUTTONDOWN:
            a,b = event.pos
            if(a>580 and a<640 and b>0 and b<100):
                play_player(newBoard())
            if(a>550and a<640 and b>450 and b<480 ):
                Themain_menu()
        if event.type == MOUSEBUTTONDOWN:
            a,b = event.pos
            if(a>550and a<640and b>410 and b<450):
                saveGame(board)
    pygame.display.update()
    fpsClock.tick(FPS)

#人机对战，player VS computer#
def play_computer(board,playerID):
 new=playerID
 i=1
 checkN=0
 pygame.init()
 FPS=50
 fontObj = pygame.font.Font('freesansbold.ttf',20)
 texteSurface1 = fontObj.render('Save',True,THECOLORS["black"])
 texteRect1 = texteSurface1.get_rect()
 texteRect1.topleft = (580,430)
 texteSurface2 = fontObj.render('Home',True,THECOLORS["black"])
 texteRect2 = texteSurface2.get_rect()
 texteRect2.topleft = (580,450)
 ImageRect3=ReplayImage.get_rect()
 ImageRect3.topleft = (600,0)
 mySurface.blit(backgoundImage,(0,0))
 if board[0][0]==1:
     mySurface.blit(X_Image,(55,90))
 if board[1][0]==1:
     mySurface.blit(X_Image,(195,80))
 if board[2][0]==1:
     mySurface.blit(X_Image,(345,65))
 if board[0][1]==1:
     mySurface.blit(X_Image,(100,210))
 if board[1][1]==1:
     mySurface.blit(X_Image,(250,210))
 if board[2][1]==1:
     mySurface.blit(X_Image,(390,200))
 if board[0][2]==1:
     mySurface.blit(X_Image,(135,345))
 if board[1][2]==1:
     mySurface.blit(X_Image,(280,350))
 if board[2][2]==1:
     mySurface.blit(X_Image,(430,335))
 if board[0][0]==2:
     mySurface.blit(O_Image,(55,90))
 if board[1][0]==2:
     mySurface.blit(O_Image,(195,80))
 if board[2][0]==2:
     mySurface.blit(O_Image,(345,65))
 if board[0][1]==2:
     mySurface.blit(O_Image,(100,210))
 if board[1][1]==2:
     mySurface.blit(O_Image,(250,210))
 if board[2][1]==2:
     mySurface.blit(O_Image,(390,200))
 if board[0][2]==2:
     mySurface.blit(O_Image,(135,345))
 if board[1][2]==2:
     mySurface.blit(O_Image,(280,350))
 if board[2][2]==2:
     mySurface.blit(O_Image,(430,335))
 while True:
    mySurface.blit(texteSurface1,texteRect1)
    mySurface.blit(texteSurface2,texteRect2)
    mySurface.blit(ReplayImage,ImageRect3)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if checkVictory(board)!=True:
            if checkN!=9:
                if playerID%2!=0:
                  if event.type ==MOUSEBUTTONDOWN:
                    a,b = event.pos
                    if(a>85and a<180and b>80and b<190and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>190and a<350and b>90and b<180and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>360and a<490and b>80and b<150and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>100and a<250and b>210and b<340and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>250and a<400and b>200and b<320and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>400and a<550and b>170and b<310and playOneTime(board,2,1,playerID)==True):
                        x=390
                        y=200
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>150and a<260and b>340and b<440and playOneTime(board,0,2,playerID)==True):
                        x=135
                        y=345
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>270and a<420and b>340and b<450and playOneTime(board,1,2,playerID)==True):
                        x=280
                        y=350
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(a>430and a<580and b>330and b<440and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                  elif event.type==KEYDOWN:
                    if(event.key==K_q and playOneTime(board,0,0,playerID)==True):
                        x=55
                        y=90
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_w and playOneTime(board,1,0,playerID)==True):
                        x=195
                        y=80
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_e and playOneTime(board,2,0,playerID)==True):
                        x=345
                        y=65
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_a and playOneTime(board,0,1,playerID)==True):
                        x=100
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_s and playOneTime(board,1,1,playerID)==True):
                        x=250
                        y=210
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_d and playOneTime(board,2,1,playerID)==True):
                      if i%2!=0:
                        x=390
                        y=200
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_z and playOneTime(board,0,2,playerID)==True):
                        x=135
                        y=345
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_x and playOneTime(board,1,2,playerID)==True):
                      if i%2!=0:
                        x=280
                        y=350
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                    if(event.key==K_c and playOneTime(board,2,2,playerID)==True):
                        x=430
                        y=335
                        playerID=2
                        mySurface.blit(X_Image,(x,y))
                        i+=1
                        checkN+=1
                else:
                     computerPlay(board,playerID)
                     playerID=1
                     i+=1
                     checkN+=1
                     if board[0][0]==1:
                         mySurface.blit(X_Image,(55,90))
                     if board[1][0]==1:
                         mySurface.blit(X_Image,(195,80))
                     if board[2][0]==1:
                         mySurface.blit(X_Image,(345,65))
                     if board[0][1]==1:
                         mySurface.blit(X_Image,(100,210))
                     if board[1][1]==1:
                         mySurface.blit(X_Image,(250,210))
                     if board[2][1]==1:
                         mySurface.blit(X_Image,(390,200))
                     if board[0][2]==1:
                         mySurface.blit(X_Image,(135,345))
                     if board[1][2]==1:
                         mySurface.blit(X_Image,(280,350))
                     if board[2][2]==1:
                         mySurface.blit(X_Image,(430,335))
                     if board[0][0]==2:
                         mySurface.blit(O_Image,(55,90))
                     if board[1][0]==2:
                         mySurface.blit(O_Image,(195,80))
                     if board[2][0]==2:
                         mySurface.blit(O_Image,(345,65))
                     if board[0][1]==2:
                         mySurface.blit(O_Image,(100,210))
                     if board[1][1]==2:
                         mySurface.blit(O_Image,(250,210))
                     if board[2][1]==2:
                         mySurface.blit(O_Image,(390,200))
                     if board[0][2]==2:
                         mySurface.blit(O_Image,(135,345))
                     if board[1][2]==2:
                         mySurface.blit(O_Image,(280,350))
                     if board[2][2]==2:
                         mySurface.blit(O_Image,(430,335))
            else:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(draw,(255,155))
        if checkVictory(board) == True:
            if playerID==1:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(loser,(255,155))
            else:
                mySurface.blit(backgroundImage1,(0,0))
                mySurface.blit(winner,(255,155))
        if event.type == MOUSEBUTTONDOWN:
            a,b = event.pos
            if(a>580 and a<640 and b>0 and b<100):
                play_computer(newBoard(),new)
            if(a>550and a<640 and b>450 and b<480 ):
                Themain_menu()
        if event.type == MOUSEBUTTONDOWN:
            a,b = event.pos
            if(a>550and a<640and b>420 and b<450):
                saveGame(board)
    pygame.display.update()
    fpsClock.tick(FPS)

#选择人与电脑谁先界面，chose player or computer who is first#
def play_computer2():
    pygame.init()
    FPS=50
    fontObj = pygame.font.Font('freesansbold.ttf',20)
    texteSurface1 = fontObj.render('Player first!',True,THECOLORS["black"])
    texteRect1 = texteSurface1.get_rect()
    texteRect1.topleft = (215,215)
    texteSurface2 = fontObj.render('Computer first!',True,THECOLORS["black"])
    texteRect2 = texteSurface2.get_rect()
    texteRect2.topleft = (215,300)
    texteSurface3 = fontObj.render('Back menu!',True,THECOLORS["black"])
    texteRect3 = texteSurface3.get_rect()
    texteRect3.topleft = (215,385)
    fontObj2 = pygame.font.Font('freesansbold.ttf',15)
    texteSurface9 = fontObj2.render('the dada studio',True,THECOLORS["black"])
    texteRect9=texteSurface9.get_rect()
    texteRect9.topleft = (230,460)
    while True:
        mySurface.blit(backgroundImage1,(0,0))
        mySurface.blit(texteSurface1,texteRect1)
        mySurface.blit(texteSurface2,texteRect2)
        mySurface.blit(texteSurface3,texteRect3)
        mySurface.blit(texteSurface9,texteRect9)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                a,b = event.pos
                if(a>190 and a<420 and b>200 and b<260):
                    play_computer(newBoard(),1)
                if(a>190 and a<420 and b>260 and b<350):
                    play_computer(newBoard(),2)
                if(a>190 and a<420 and b>350 and b<430):
                   Themain_menu()
        pygame.display.update()
        fpsClock.tick(FPS)

#制作人界面，One more thing#
def Theother_menu():
    pygame.init()
    FPS=50
    fontObj1 = pygame.font.Font('freesansbold.ttf',48)
    texteSurface = fontObj1.render('XX&OO',True,THECOLORS["black"])
    texteRect = texteSurface.get_rect()
    texteRect.topleft = (90,50)
    fontObj = pygame.font.Font('freesansbold.ttf',25)
    texteSurface2 = fontObj.render('ver 1.0 beta',True,THECOLORS["black"])
    texteRect2 = texteSurface2.get_rect()
    texteRect2.topleft = (90,100)
    texteSurface3 = fontObj.render('Designed by: JasonYan',True,THECOLORS["black"])
    texteRect3 = texteSurface3.get_rect()
    texteRect3.topleft = (90,215)
    texteSurface4 = fontObj.render('HarryHo',True,THECOLORS["black"])
    texteRect4 = texteSurface4.get_rect()
    texteRect4.topleft = (253,250)
    texteSurface5 = fontObj.render('GaoWei',True,THECOLORS["black"])
    texteRect5 = texteSurface5.get_rect()
    texteRect5.topleft = (253,285)
    texteSurface6 = fontObj.render('Home',True,THECOLORS["black"])
    texteRect6=texteSurface6.get_rect()
    texteRect6.topleft = (560,450)
    texteSurface7 = fontObj.render('Connect us:',True,THECOLORS["black"])
    texteRect7=texteSurface7.get_rect()
    texteRect7.topleft = (90,330)
    texteSurface8 = fontObj.render('twitter:@dada.studio',True,THECOLORS["black"])
    texteRect8=texteSurface8.get_rect()
    texteRect8.topleft = (250,365)
    fontObj2 = pygame.font.Font('freesansbold.ttf',15)
    texteSurface9 = fontObj2.render('the dada studio',True,THECOLORS["black"])
    texteRect9=texteSurface9.get_rect()
    texteRect9.topleft = (230,460)
    while True:
        mySurface.blit(backgroundImage1,(0,0))
        mySurface.blit(texteSurface,texteRect)
        mySurface.blit(texteSurface2,texteRect2)
        mySurface.blit(texteSurface3,texteRect3)
        mySurface.blit(texteSurface4,texteRect4)
        mySurface.blit(texteSurface5,texteRect5)
        mySurface.blit(texteSurface6,texteRect6)
        mySurface.blit(texteSurface7,texteRect7)
        mySurface.blit(texteSurface8,texteRect8)
        mySurface.blit(texteSurface9,texteRect9)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                a,b = event.pos
                if(a>580 and a<640 and b>450 and b<480):
                    Themain_menu()
        pygame.display.update()
        fpsClock.tick(FPS)

#主界面，The main menu#
def Themain_menu():
    pygame.init()
    FPS=50
    fpsClock = pygame.time.Clock()
    fontObj1 = pygame.font.Font('freesansbold.ttf',50)
    texteSurface1 = fontObj1.render('XX&OO',True,THECOLORS["black"])
    texteRect1 = texteSurface1.get_rect()
    texteRect1.topleft = (220,50)
    fontObj = pygame.font.Font('freesansbold.ttf',25)
    texteSurface2 = fontObj.render('Player VS Player',True,THECOLORS["black"])
    texteRect2 = texteSurface2.get_rect()
    texteRect2.topleft = (200,195)
    texteSurface3 = fontObj.render('Player VS Computer',True,THECOLORS["black"])
    texteRect3 = texteSurface3.get_rect()
    texteRect3.topleft = (180,245)
    texteSurface4 = fontObj.render('Load the Game',True,THECOLORS["black"])
    texteRect4 = texteSurface4.get_rect()
    texteRect4.topleft = (215,295)
    texteSurface5 = fontObj.render('Quit',True,THECOLORS["black"])
    texteRect5 = texteSurface5.get_rect()
    texteRect5.topleft = (270,345)
    texteSurface6 = fontObj.render('About',True,THECOLORS["black"])
    texteRect6=texteSurface6.get_rect()
    texteRect6.topleft = (260,400)
    fontObj2 = pygame.font.Font('freesansbold.ttf',15)
    texteSurface9 = fontObj2.render('the dada studio',True,THECOLORS["black"])
    texteRect9=texteSurface9.get_rect()
    texteRect9.topleft = (245,460)
    pygame.display.set_caption('Tic tac toe')
    while True:
        mySurface.blit(backgroundImage1,(0,0))
        mySurface.blit(texteSurface1,texteRect1)
        mySurface.blit(texteSurface2,texteRect2)
        mySurface.blit(texteSurface3,texteRect3)
        mySurface.blit(texteSurface4,texteRect4)
        mySurface.blit(texteSurface5,texteRect5)
        mySurface.blit(texteSurface6,texteRect6)
        mySurface.blit(texteSurface9,texteRect9)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                   a,b = event.pos
                   if(a>160 and a<460 and b>180 and b<230):
                        play_player(newBoard())
                   if(a>160 and a<460 and b>230 and b<280):
                        play_computer2()
                   if(a>160 and a<460 and b>280 and b<330):
                    if loadGame()==False:
                        play_player(newBoard())
                    else:
                        board2= loadGame()
                        play_player(board2)
                   if(a>160 and a<460 and b>340 and b<380):
                        sys.exit()
                   if(a>160 and a<460 and b>390 and b<430):
                        Theother_menu()
        pygame.display.update()
        fpsClock.tick(FPS)
Themain_menu()
#创建主页面的菜单#
