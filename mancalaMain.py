from makeMove import *
from playerOne import *
from playerTwo import *
from Board import *
from winner_winner import *
from miniMax import *
from saveLoad import *

#------------------------------------------------------------------------------
def iswinner(stonesAmount):
    final_board,win,end =winner(stonesAmount,False)
    if(u_in=='q'or u_in=='Q'or end==1):
        gameOn = False
        Board(final_board,True) ##mehtagen neshel your turn hena law feh winner
        return 0
    return 1
#------------------------------------------------------------------------------
moveCharP1 = ['a','b','c','d','e','f']
moveCharP2 = ['f','e','d','c','b','a']    
stonesAmount = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
#------------------------------------------------------------------------------
# board=[4,4,4,4,4,4,0,       4,4,4,4,4,4,0]
final_board=[]
#      a,b,c,d,e,f,man_p1,  f,e,d,c,b,a, man_p2
valid=True
playagain=False
gameOn = True
end=0
p1=0
p1again=0
p2=0
p2again=0
# Board(stonesAmount,True)
#------------------------------------------------------------------------------

loadGame = input("please enter (Y) if you want to load the last game, or any key to continue: "+'\n')
if loadGame == 'y' or loadGame == 'Y':
    stonesAmount,gameMode,Stealing,gameDepth = saveLoad(stonesAmount,'0','0','0',False,True)
else:
    gameMode = input("Please enter (1) for 1vs1, (2) for 1vsPC or (3) for PCvs1: "+ '\n' )
    gameDiff = input('\n'+"Please enter (1) for EASY mode, (2) for MEDIUM mode or (3) for HARD mode: "+'\n')
    Stealing = input('\n'+"Please enter (1) for STEALING mode or (2) for NORMAL mode: " + '\n')
    if Stealing == '1':
        stealing=True     
    else:
        stealing=False
    if gameDiff == '1':
        gameDepth = 2
    elif gameDiff == '2':
        gameDepth = 6
    elif gameDiff == '3':
        gameDepth = 10    




if gameMode == str(1):

    while(gameOn):

    ##player1
        while(~(valid)):
            p1=1
            u_in=0
            Board(stonesAmount,True)
            u_in=input("player_1: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
            print("")
            if u_in =='q':
                gameOn=False
                break
            elif u_in == 's':
                saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                gameOn=False
                break
            stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,stealing)
            Board(stonesAmount,True)
            if valid==True:
                break
            
        if p1==1:
            endORcont=iswinner(stonesAmount)
            p1=0
            if endORcont==0:
                break
            
        while(playagain):
            p1again=1
            u_in=input("player_1: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
            print("")
            if u_in =='q':
                gameOn=False
                break
            elif u_in == 's':
                saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                gameOn=False
                break  
            stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,stealing)
            #lw ana gwaha w galy hole invalid
            if valid == False:
                playagain=True
                continue
            Board(stonesAmount,True)         
            if playagain==False:
                break
            
        if p1again==1:
            endORcont=iswinner(stonesAmount)
            pagain=0
            if endORcont==0:
                break
    #------------------------------------------------------------------------------
    ##player2
        while(~(valid)):
            u_in=0
            p2=1
            Board(stonesAmount,False)
            u_in=input("player_2: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
            print("")
            if u_in =='q':
                gameOn=False
                break
            elif u_in == 's':
                saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                gameOn=False
                break  
            stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in),False,stealing)
            Board(stonesAmount,False)
            if valid==True:
                break
            
        if p2==1:
            endORcont=iswinner(stonesAmount)
            p2=0
            if endORcont==0:
                break
            
        while(playagain):
            p2again=1
            u_in=input("player_2: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
            print("")
            if u_in =='q':
                gameOn=False
                break
            elif u_in == 's':
                saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                gameOn=False
                break  
            print("")
            stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in), False,stealing)
            #lw ana gwaha w galy hole invalid
            if valid == False:
                playagain=True
                continue
            Board(stonesAmount,False)        
            if playagain==False:
                break
            
        if p2again==1:
            endORcont=iswinner(stonesAmount)
            p2again=0
            if endORcont==0:
                break
            
            
            
            
elif gameMode == str(2):
    
        while(gameOn):
        ##player1
            while(~(valid)):
                        
                Board(stonesAmount,True)
                p1=1
                u_in=0
                u_in=input("player_1: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
                print("")
                if u_in =='q':
                    gameOn=False
                    break
                elif u_in == 's':
                    saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                    gameOn=False
                    break
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,stealing)
                Board(stonesAmount,True)
                if valid==True:
                    break
                
            if p1==1:
                endORcont=iswinner(stonesAmount)
                p1=0
                if endORcont==0:
                    break
                
            while(playagain):
                p1again=1
                u_in=input("player_1: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
                print("")
                if u_in =='q':
                    gameOn=False
                    break    
                elif u_in == 's':
                    saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                    gameOn=False
                    break
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,stealing)
                Board(stonesAmount,True)
                #lw ana gwaha w galy hole invalid
                if valid == False:
                    playagain=True
                    continue
                # Board(stonesAmount,True)         
                if playagain==False:
                    break
                
            if p1again==1:
                endORcont=iswinner(stonesAmount)
                pagain=0
                if endORcont==0:
                    break
                #------------------------------------------------------------------------------
        ##player2
            while(~(valid)):
                Board(stonesAmount,False)
                p2=1
                
                _,moveChar = miniMax(stonesAmount, gameDepth, -math.inf, math.inf, isMaximizing=True, playAgain=False)
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(moveChar),False,stealing)
                Board(stonesAmount,False)
                if valid==True:
                    break

                
            if p2==1:
                endORcont=winner(stonesAmount)
                p2=0
                if endORcont==0:
                    break
                
            while(playagain):
                p2again=1
                _,moveChar = miniMax(stonesAmount, gameDepth, -math.inf, math.inf, isMaximizing=True, playAgain=False)
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(moveChar),False,stealing)
                if valid == False:
                    playagain=True
                    continue
                Board(stonesAmount,False)        
                if playagain==False:
                    break
                
            if p2again==1:
                endORcont=winner(stonesAmount)
                p2again=0
                if endORcont==0:
                    break
                
                
            
elif gameMode == str(3):
    
        while(gameOn):
        ##player1
            while(~(valid)):
                p1=1
                _,moveChar = miniMax(stonesAmount, gameDepth, -math.inf, math.inf, isMaximizing=True, playAgain=False)
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(moveChar),True,stealing)
                Board(stonesAmount,True)
                if valid==True:
                    break
                
            if p1==1:
                endORcont=winner(stonesAmount)
                p1=0
                if endORcont==0:
                    break
                
            while(playagain):
                _,moveChar = miniMax(stonesAmount, gameDepth, -math.inf, math.inf, isMaximizing=True, playAgain=False)
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(moveChar),True,stealing)
                #lw ana gwaha w galy hole invalid
                if valid == False:
                    playagain=True
                    continue
                Board(stonesAmount,True)         
                if playagain==False:
                    break
                
            if p1again==1:
                endORcont=winner(stonesAmount)
                pagain=0
                if endORcont==0:
                    break
        #------------------------------------------------------------------------------
        ##player2
            while(~(valid)):
                u_in=0
                p2=1
                print("")
                u_in=input("player_2: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
                print("")
                if u_in =='q':
                    gameOn=False
                    break
                elif u_in == 's':
                    saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                    gameOn=False
                    break  
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in),False,stealing)
                Board(stonesAmount,False,True)
                if valid==True:
                    break
                
            if p2==1:
                endORcont=iswinner(stonesAmount)
                p2=0
                if endORcont==0:
                    break
                
            while(playagain):
                p2again=1
                u_in=input("player_2: enter a valid letter to PLAY, (S) to SAVE or (Q) to QUIT: "+ '\n' )
                print("")
                if u_in =='q':
                    gameOn=False
                    break
                elif u_in == 's':
                    saveLoad(stonesAmount,gameMode,stealing,gameDepth,True,False)
                    gameOn=False
                    break
                stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in), False,stealing)
                #lw ana gwaha w galy hole invalid
                if valid == False:
                    playagain=True
                    continue
                Board(stonesAmount,False)        
                if playagain==False:
                    break
                
            if p2again==1:
                endORcont=iswinner(stonesAmount)
                p2again=0
                if endORcont==0:
                    break
        
#------------------------------------------------------------------------------



















