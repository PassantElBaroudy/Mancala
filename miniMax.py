from evalHeuristics import *
import math
from makeMove import *
from evalHeuristics import *
from playerOne import *
from playerTwo import *
from winner_winner import *


moveCharP1 = ['a','b','c','d','e','f']
moveCharP2 = ['f','e','d','c','b','a']   


def miniMax(stonesAmount, depth, alpha, beta, stealing=True, isMaximizing=True, playAgain=False):

    if depth == 0:
        return evalHeuristics(stonesAmount,playAgain,isMaximizing),-200
    
    elif (winner((stonesAmount),True)[2]==1):
        return evalHeuristics(winner((stonesAmount),True)[0],playAgain,isMaximizing),-200    
        
    if isMaximizing:
        maxEval = -math.inf
        
        for i in range(6):
            
            
            newState, valid,playAgain =  makeMove(stonesAmount,playerTwo(moveCharP2[i]),False, True)          #3ayez makeMove teraga3 door anhy player
         
            if valid:
                Eval,_ = miniMax(newState, depth - 1, alpha, beta, stealing, playAgain, playAgain)  #ab3at lel makeMove fih stealing wala la2                
               
                if maxEval != max(maxEval, Eval):
                    optimalMove = moveCharP2[i]
                    
                maxEval = max(maxEval, Eval)                                                                         #ne7ot ehtmal en yekon el pocket fady
                alpha = max(alpha, Eval)      
                                                                                                                            #return heuristics if game is over
                if beta <= alpha:
                    break
        return maxEval,optimalMove

        
        
    else:
        minEval = math.inf
        
        for i in range(6):
            
            
            newState,valid,playAgain = makeMove(stonesAmount,playerOne(moveCharP1[i]),True, True)
            
            if valid:
                Eval,_ = miniMax(newState, depth - 1, alpha, beta, stealing, not playAgain, playAgain)      
                minEval = min(minEval, Eval)
                beta = min(beta, Eval)
                
                if beta <= alpha:
                    break
                
        return minEval,-400



    