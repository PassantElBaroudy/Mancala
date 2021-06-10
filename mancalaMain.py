from makeMove import *
from playerOne import *
from playerTwo import *
from Board import *
from winner_winner import *
# from evalHeuristics import *
# from miniMax import *
# #from Board import *
# import math
#------------------------------------------------------------------------------
def iswinner(stonesAmount):
    final_board,win,end =winner(stonesAmount)
    if(u_in=='q'or u_in=='Q'or end==1):
        gameOn = False
        Board(final_board,True,False) ##mehtagen neshel your turn hena law feh winner
        return 0
    return 1
#------------------------------------------------------------------------------
moveCharP1 = ['a','b','c','d','e','f']
moveCharP2 = ['f','e','d','c','b','a']    
stonesAmount = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
#------------------------------------------------------------------------------
board=[4,4,4,4,4,4,0,       4,4,4,4,4,4,0]
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
Board(stonesAmount,True,False)
#------------------------------------------------------------------------------
while(gameOn):
    
##player1
    while(~(valid)):
        p1=1
        u_in=0
        u_in=input("player_1: enter a valid letter to play or Q to Quit: "+ '\n' )
        print("")
        if u_in =='q':
            gameOn=False
            break
        stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,False)
        Board(stonesAmount,True,False)
        if valid==True:
            break
        
    if p1==1:
        endORcont=iswinner(stonesAmount)
        p1=0
        if endORcont==0:
            break
        
    while(playagain):
        p1again=1
        u_in=input("player_1: enter a valid letter to play or Q to Quit: "+ '\n' )
        print("")
        if u_in =='q':
            gameOn=False
            break    
        stonesAmount, valid, playagain = makeMove(stonesAmount,playerOne(u_in),True,False)
        #lw ana gwaha w galy hole invalid
        if valid == False:
            playagain=True
            continue
        Board(stonesAmount,True,False)         
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
        u_in=input("player_2: enter a valid letter to play or Q to Quit: "+ '\n' )
        print("")
        if u_in=='q':
            gameOn=False
            break
        stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in),False,False)
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
        u_in=input("play again(user_2):  " )
        print("")
        stonesAmount, valid, playagain = makeMove(stonesAmount,playerTwo(u_in), False,False)
        #lw ana gwaha w galy hole invalid
        if valid == False:
            playagain=True
            continue
        Board(stonesAmount,False,True)        
        if playagain==False:
            break
        
    if p2again==1:
        endORcont=iswinner(stonesAmount)
        p2again=0
        if endORcont==0:
            break
#------------------------------------------------------------------------------




















