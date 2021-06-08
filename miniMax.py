from evalHeuristics import *

def miniMax(stonesAmount, depth, alpha, beta, isMaximizing=True):

    if depth == 0:
        return evalHeuristics(stonesAmount)
        
    if isMaximizing:
        maxEval = -math.inf
        
        for i in range(6):
            newState =  makeMove(stonesAmount,moveCharP1[i],True)          #3ayez makeMove teraga3 door anhy player
            Eval = miniMax(newState, depth - 1, alpha, beta, False)        #ab3at lel makeMove fih stealing wala la2
            maxEval = max(maxEval, Eval)                                   #ne7ot ehtmal en yekon el pocket fady
            alpha = max(alpha, Eval)                                       #return heuristics if game is over
            if beta <= alpha:
                break
        return maxEval
        
        
    else:
        minEval = math.inf
        
        for i in range(6):
            newState = makeMove(stonesAmount,moveCharP2[i],False)
            Eval = miniMax(newState, depth - 1, alpha, beta, True)
            minEval = min(minEval, Eval)
            beta = min(beta, Eval)
            if beta <= alpha:
                break
        return minEval
